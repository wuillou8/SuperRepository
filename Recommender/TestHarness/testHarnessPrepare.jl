using JSON
using Dates
#using Lazy
#using StatsBase
#using Dates
#using PyPlot

include("JuliaCode/classes.jl")


# Instantiate test harness
    __TH = createTest("testfile.txt")

# preparing Data
    dataformatt = "DataBase/dataformatt.json" #data.json
    testdatapath = "DataBase/data4test.json"
    traindatapath = "DataBase/data4train.json"
    outtest = open(testdatapath,"w+")
    outtrain = open(traindatapath,"w+")


    STDIN = open(dataformatt,"r+")
    __bedata = DataUsage[]
    while !eof(STDIN)
        sent_type, tent_type, sent_id, tent_id, action, value, time =
                readline(STDIN) |>
                (_ -> filter(x -> !(x in ['\n']),_)) |> JSON.parse |>
                ( _ ->   begin
                              _["source_entity_type"],
                              _["target_entity_type"],
                              _["source_entity_id"],
                              _["target_entity_id"],
                              _["action"],
                              _["value"],
                              _["time"]
                         end )

        obj = DataUsage(sent_type, tent_type, sent_id, tent_id, action, value, time)
        if time < datetime2unix(__TH.T2)
            write(outtrain, JSON.json(obj)*"\n")
        else
            write(outtest, JSON.json(obj)*"\n")
        end

        push!(__bedata, DataUsage(sent_type, tent_type, sent_id, tent_id, action, value, time))
    end


close(outtrain)
