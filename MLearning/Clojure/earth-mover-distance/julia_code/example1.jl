include("emd.jl")
# python example1

type Feature
    x::Int64
    y::Int64
    z::Int64
end

type Signature 
    features::Vector{Feature}
    weights::Vector{Float64}
end

distance (f1::Feature, f2::Feature) =
    sqrt((f1.x - f2.x)^2  + (f1.y - f2.y)^2 + (f1.z - f2.z)^2)

sgn1 = Signature([Feature(100, 40, 22), Feature(211, 20, 2), Feature(32, 190, 150), Feature(2, 100, 100)],
                [0.4, 0.3, 0.2, 0.1])
sgn2 = Signature([Feature(0, 0, 0), Feature(50, 100, 80), Feature(255, 255, 255)],
                [0.5, 0.3, 0.2])

C = fill(0., (length(sgn1.features), length(sgn2.features)))
for i = 1:length(sgn1.features)
    for j = 1:length(sgn2.features)
        C[i,j] = distance(sgn1.features[i], sgn2.features[j]) 
    end
end



"""Defs:"""
c = C

a = sgn1.weights
b = sgn2.weights

i_x = convert(Vector{Int64},[i for i in 1:size(c)[1]])
i_y = convert(Vector{Int64},[i for i in 1:size(c)[2]])

m_final = fill(0, size(c))

h_mat = Houthakker_matrix(c, i_x, i_y, a, b, m_final)