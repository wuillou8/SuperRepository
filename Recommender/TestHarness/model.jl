

abstract MODEL

type RandomModel <: MODEL
	#myparams::String
end

function modelsFactory( modelname::String, data::Any )
	@switch modelname begin
		"RANDOM"; return RandomModel()
		"model not implemented yet" |> println
	end
end
