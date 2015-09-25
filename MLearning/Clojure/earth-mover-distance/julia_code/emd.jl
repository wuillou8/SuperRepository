# Russel algo for near optimal basis to transportation problem

#Houthakker's cost matrix
type Houthakker_matrix
    # cost mat
    #c_matrix_score::Array{Int64,2}
    c_matrix::Array{Float64,2}
    
    # "active" coords.
    i_a::Array{Int64,1}
    i_b::Array{Int64,1}
    
    # supply/demand vects.
    a::Array{Float64,1}
    b::Array{Float64,1}
    
    # result mat.
    r_matrix::Array{Float64,2}
end

function russel_f(m::Houthakker_matrix)

    # step 1 : build w and y
    w = [maximum(m.c_matrix[i,:]) for i in m.i_a]
    y = [maximum(m.c_matrix[:,j]) for j in m.i_b]
    
    # step 2 : build dantzig criterion and find max
    max = 0.
    i_max, j_max = (0,0)
    for i = 1:length(m.i_a)
        for j = 1:length(m.i_b)
            id_i, id_j = m.i_a[i], m.i_b[j]
            if max < (w[i] + y[j] - m.c_matrix[id_i,id_j])
                max = w[i] + y[j] - m.c_matrix[id_i,id_j] 
                i_max, j_max = (id_i,id_j)
            end
        end
    end

println(i_max, j_max, size(m.c_matrix))

    # step 3 : reset activity level
    min = minimum([m.a[i_max] m.b[j_max]])
    
    # step 4 : substract activity 
    m.a[i_max] = m.a[i_max] - min
    m.b[j_max] = m.b[j_max] - min
    
    m.r_matrix[i_max, j_max] = min
    
    m.i_a = filter(x -> !(x in find(x -> x==0, m.a)), m.i_a)
    m.i_b = filter(x -> !(x in find(x -> x==0, m.b)), m.i_b)
    
    m
end

function reduce_cost(res_mat::Houthakker_matrix)
    cost = 0
    for i = 1:size(h_mat.c_matrix)[1]
        for j = 1:size(h_mat.c_matrix)[2]
            cost = cost + res_mat.r_matrix[i,j]*res_mat.c_matrix[i,j]
        end
    end
    cost
end
