function getDataUsage(__datapath::String)
    STDIN = open(__datapath,"r+")
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

           push!( __bedata,
                       DataUsage(sent_type, tent_type, sent_id, tent_id, action, value, time) )
    end
    BEData(__bedata)
end
