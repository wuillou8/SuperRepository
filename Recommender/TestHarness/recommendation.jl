using JSON
using Dates

include("JuliaCode/classes.jl")
include("JuliaCode/Models.jl")

__modelName = ARGS[1]

# load/instantiate/append model
    __models = "DataBase/trainedmodel$__modelName.json" |>
                JSON.parsefile |> (_ -> modelsFactory(_,  __modelName))

    #println(__models)
    #===
    __models = MODEL[]
    for i = 1:length(__TH.Recommenders)
        __modelName = __TH.Recommenders[i]

        # load/instantiate/append model
        "DataBase/trainedmodel$__modelName$i.json" |>
                   JSON.parsefile |> (_ -> modelsFactory(_,  __modelName)) |>
                                (_ -> begin
                                          push!(__models,_)
                                          "model $__modelName loaded" |> println
                                      end )
    end
    ===#

recommenderList( __model, __testnewsIds, userId, __trainbedata, __testbedata )