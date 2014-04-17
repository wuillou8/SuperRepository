module LDA

	type MyCluster
		posx::Float64
		posy::Float64
		dim::Int
		size::Int
		disp::Array{Float64, }
                label::Int
                function MyCluster(posxy::Array{Float64,1},size::Int, dim::Int, label::Int)
			posx = posxy[1]
			posy = posxy[2]
			disp = Array(Float64, (size,dim))
			arr = randn!(disp) 
			# shift points accordingly
			arr[1:size] += posx
			arr[(size+1):end] += posy
                        new(posx, posy, dim, size, disp, label)
		end
	end
        # function computing the x,y-averages
        function f_mean (m_clus::MyCluster)

                meanx = 0
                meany = 0
                for x = m_clus.disp[:, 1]
                        meanx += x
                end
                for y = m_clus.disp[:, 2]
                        meany += y
                end

                return meanx/m_clus.size , meany/m_clus.size
        end

end
