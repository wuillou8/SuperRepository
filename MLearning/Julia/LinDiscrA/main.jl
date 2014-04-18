using LDA
using PyPlot

include("utilities.jl")
include("lda.jl")

#########################################################
#	--Main--					#
#	Implementation of Lin Disc. Algo on a set 	#
#	of self-generated points.			#
#########################################################

        # construct cluster by hand (point clouds)
        Dim = 2
        posC1, N1 = [5.5,10.55], 100
        posC2, N2 = [-5.5,2.55], 150
        posC3, N3 = [-0.5,8.55], 150
        posC4, N4 = [2.5,4.55], 150

        # create clusters
        clust1 = LDA.MyCluster(posC1,N1,Dim,1)
        clust2 = LDA.MyCluster(posC2,N2,Dim,2)
        clust3 = LDA.MyCluster(posC3,N3,Dim,3)
        clust4 = LDA.MyCluster(posC4,N4,Dim,4)

        #compute cluster centerd
        mu1= Array{Float64, 1}
        mu1 = LDA.f_mean(clust1)
        #mu2_x, mu2_y = LDA.f_mean(clust2)
        #mu3_x, mu3_y = LDA.f_mean(clust3)
        #mu4_x, mu4_y = LDA.f_mean(clust4)

        # group points within a unique array
        cloud = [ clust1.disp ; clust2.disp ; clust3.disp; clust4.disp ]

        # plotting
        x, y = cloud[:, 1], cloud[:, 2]
        plot ( x, y, marker="+", linestyle=" ")
        title("Points distribution before running LDA")
