module LDA

        # Cluster class
	type MyCluster
                pos::Array{Float64,1}
		dim::Int
		size::Int
		disp::Array{Float64, }
                label::Int

                # constructor
                function MyCluster(posi::Array{Float64,1}, size::Int, dim::Int, label::Int)
                        # check dim
                        length(posi) == dim ? pos = posi : throw("error: clust.dim != sizeof(pos_array)")
                        # generate random points
			disp = Array(Float64, (size,dim))
			arr = randn!(disp) 
                        # shift points accordingly
                        for i in 1:dim
                                arr[:, i] += pos[i]
                        end
                        new(pos, dim, size, disp, label)
		end
	end

        # function computing the x,y-averages
        function f_mean (m_clus::MyCluster)
                f_mean = Array{Float64, (m_clus.dim,1)}
                for d in 1:m_clus.dim
                        for x = m_clus.disp[:, d]
                                f_mean[d] += x
                        end
                end
                return f_mean / m_clus.size
        end

end
