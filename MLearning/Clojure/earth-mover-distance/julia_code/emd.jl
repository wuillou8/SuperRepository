include("classes.jl")

""" Russel algo for near optimal basis to transportation problem. """

function preprocess (sgn1::Signature, sgn2::Signature, dist::Function)
    
    # init Cost matrix size:
    # If costs > demand or inversely, add an additional weight on the demand resp. cost side and fill it with the diff.
    # The costs are zero for the appended col resp. row.
    if (abs( 1e-06 > (sum(sgn1.weights) - sum(sgn2.weights)))) #sum(sgn1.weights) - sum(sgn2.weights))
        C = fill(0., (length(sgn1.features), length(sgn2.features)))
    elseif (sum(sgn1.weights) > sum(sgn2.weights))
        C = fill(0., (length(sgn1.features), length(sgn2.features) + 1))
        push!(sgn2.weights, sum(sgn1.weights) - sum(sgn2.weights))
    else
        C = fill(0., (length(sgn1.features) + 1, length(sgn2.features)))
        push!(sgn1.weights, sum(sgn2.weights) - sum(sgn1.weights))
    end
    # create Costs matrix
    for i = 1:length(sgn1.features)
        for j = 1:length(sgn2.features)
            C[i,j] = distance(sgn1.features[i], sgn2.features[j]) 
        end
    end
    
    # Defs objets for computation:
    # we use an indices table for the algo.
    i_x = convert(Vector{Int64},[i for i in 1:size(C)[1]])
    i_y = convert(Vector{Int64},[i for i in 1:size(C)[2]])
    
    # we store the transaction on a cost matrix.
    m_final = fill(0, size(C))
    Russel_decomposition(C, i_x, i_y, sgn1.weights, sgn2.weights, m_final)
end


function russel_f(m::Russel_decomposition)

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
    
    # step 3 : reset activity level
    min = minimum([m.a[i_max] m.b[j_max]])
    
    # step 4 : substract activity 
    m.a[i_max] = m.a[i_max] - min
    m.b[j_max] = m.b[j_max] - min
    
    m.r_matrix[i_max, j_max] = min
    
    m.i_a = filter(x -> (x in find(x -> x>0.000001, m.a)), m.i_a)
    m.i_b = filter(x -> (x in find(x -> x>0.000001, m.b)), m.i_b)
    
    m
end

function reduce_cost(m::Russel_decomposition)
    cost = 0
    for i = 1:size(m.c_matrix)[1]
        for j = 1:size(m.c_matrix)[2]
            cost = cost + m.r_matrix[i,j]*m.c_matrix[i,j]
        end
    end
    # emd = \sum_ij cost_ij x f_ij / \sum_ij f_ij )
    cost/sum(m.r_matrix)
end

function emd_russel(sgn1::Signature, sgn2::Signature, dist::Function)
    # preprocess
    R_decomp = preprocess(sgn1, sgn2, distance)
    # run
    it = 0
    while ((sum(R_decomp.a) + sum(R_decomp.b)) > 0.00001)
        russel_f(R_decomp)
        #println(it, " ", (sum(R_decomp.a) + sum(R_decomp.b)))
        it += 1
    end
    println("costs : ", reduce_cost(R_decomp), " iterations: ", it)
    R_decomp
end
