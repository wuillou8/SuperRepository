using HttpServer, Logging
using Lumberjack
using JSON
using Dates #Time
using StatsBase
using PyPlot
#using Lazy #, StatsBase

include("JuliaCode/utilities.jl")
include("JuliaCode/classes.jl")
include("JuliaCode/models.jl")

include("__globalModel.jl")
include("JuliaCode/recommender.jl")
include("JuliaCode/IO.jl")
include("__globalFun.jl")
include("JuliaCode/perfomeasures.jl")
include("JuliaCode/tests.jl")
include("JuliaCode/display.jl")


@Logging.configure(level=DEBUG)
# instantiate the computation
g_Comput = GlobalModel()
g_Comput.perfo = PerfoMeasure()

http = try
    HttpHandler() do req::Request, res::Response

    Var = req.resource |>
                    ( _ -> ismatch(r"^/cleanEvents/?", _) ?
                              begin
                                  val = try
                                      cleanfile("DataBase/myfile.txt")
                                      @info("file cleaned")
                                      200
                                  catch e
                                      @warn("kale_connector.jl::cleanEvents $e")
                                      500
                                  end
                                  val
                              end   :

                           ismatch(r"^/addEvents/(\w+)/?$", _) ?
                              begin
                                  val = try
                                      # for now, we copy the events into a file
                                      match(r"^/addEvents/(\w+)/?$", _) |>
                                      (_ -> appendtofile( "DataBase/myfile.txt", _.captures[1]*"\n" ) )
                                      200
                                  catch e
                                      @error("kale_connector.jl::addEvents $e")
                                      500
                                  end
                                  val
                               end   :

                           ismatch(r"^/loaddata/?", _) ?
                               # preload data for a run
                              begin
                                  val = try
                                      match(r"^/loaddata/(\w+)/(\w+)?$",req.resource) |>
                                      (_ -> isa(_, Nothing) ? loaddata() :
                                      loaddata(_.captures[1], _.captures[2]) )
                                      @info("data successfully loaded")
                                      200
                                  catch e
                                      @error("kale_connector.jl::loaddata $e")
                                      500
                                  end
                                  val
                               end   :

                           ismatch(r"^/loadmodel/?", _) ?
                              begin
                                  val = try
                                      loadmodel
                                      @info("model successfully loaded")
                                      200
                                  catch e
                                      @error("kale_connector.jl::loadmodel $e")
                                      500
                                  end
                                  val
                              end   :

                           ismatch(r"^/retrain/?", _) ?
                              begin
                                  val = try
                                      @info("model successfully retrained")
                                      match(r"^/retrain/(\w+)/(\w+)?$",req.resource) |>
                                      (_ -> isa(_, Nothing) ? trainModel() :
                                      isa(_.captures[2], Nothing) ? trainModel(_.captures[1]) :
                                      trainModel(_.captures[1], _.captures[2]) )
                                      #200
                                  catch e
                                      @error("kale_connector.jl::retrain $e")
                                      500
                                  end
                                  val
                                end   :

                           ismatch(r"^/recommend/?", _) ? # recommend/dddd/
                              begin
                                  val = try
                                      match(r"^/recommend/(\w+)/?$", _) |>
                                      (_ -> Recommendation( recommend(g_Comput, _.captures[1] )))
                                       #Recommendation( recommend(g_Comput, _.captures[1])) )
                                  catch e
                                      @error("kale_connector.jl::recommend $e")
                                      500
                                  end
                                  val
                              end   :

                           # recommendation from PredictionIO
                           ismatch(r"^/recommendIO/?", _) ? # recommend/dddd/
                              begin
                                  val = try
                                      match(r"^/recommendIO/(\w+)/?$", _) |>
                                      (_ -> Recommendation( recommend(g_Comput, _.captures[1])) )
                                  catch e
                                      @error("kale_connector.jl::recommendIO $e")
                                      500
                                  end
                                  val
                               end   :

                           # create/append Perfo Analysis
                           ismatch(r"^/testStat/?", _) ?
                              begin
                                  __recommSizes = [ 1, 3, 5, 7, 10, 20, 40, 80, 120, 200];
                         typeof(g_Comput.model) |> println
                                  val = try
                                      @info("Stat successfully built")
                                      push!(g_Comput.perfo.modelNames, getmodelType(g_Comput))
                                      println(g_Comput.perfo.modelNames)

                                      TestPerfos2( g_Comput, __recommSizes )
                                  catch e
                                      @error("kale_connector.jl::testStat $e")
                                      500
                                  end
                                  val
                               end   :

                           # visualise perfo.
                           ismatch(r"^/plot/?", _) ?
                              begin
                                   println(g_Comput.perfo)
                                   vec = [ 1, 3, 5, 7, 10, 20, 40, 80, 120, 200]
                                   name = convert(Vector{String},["Random","Random"])
                                   plotMeanRecRank2(g_Comput.perfo.perfs_ranks, vec, g_Comput.perfo.modelNames) #,__TH.Recommenders)
                                  200
                              end   :

                           : 404
                    )

  Var |> typeof |> println
  #Var |> println

  endsignal = Var |>
  (_ -> isa(_, Int64) ? _ :
        #isa(_, PIOQuery)?  JSON.json(_):
        isa(_, Recommendation) ? JSON.json(_.reclist)
        : begin
              var = try
                  update(g_Comput, _)
                  200
              catch e
                  @error("kale_connector.jl::update $e")
                  500
              end
              var
          end
      )

  #g_Comput |> println
  #println(endsignal)

    return Response(string(endsignal))
end

catch e
    @error("kale_connector.jl::HttpHandler $e")
end


http.events["error"]  = ( client, err ) -> println( err )
http.events["listen"] = ( port )        -> println("Listening on $port...")

server = Server( http )
run( server, 8000 )
