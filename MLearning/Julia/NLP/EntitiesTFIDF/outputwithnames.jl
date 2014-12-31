using MultivariateStats
D = gram2dmat(tfmat.city) 
mds = classical_mds(D, 2)
D = gram2dmat(tfidfmat.city)
mds_idf = classical_mds(D, 2)

restfx =  map(x->x - mds[1,Ncntries], mds[1,1:end])
restfy =  map(x->x - mds[2,Ncntries], mds[2,1:end])
restfidfx =  map(x->x - mds_idf[1,Ncntries], mds_idf[1,1:end])
restfidfy =  map(x->x - mds_idf[2,Ncntries], mds_idf[2,1:end])

fig = figure(figsize=(10,10))

using PyPlot
close("all")

#subplot(121)
title("Reuters News with TF: "*label)
xlabel("posX")
ylabel("posY")
ax = axes()
ax[:set_xlim]([minimum(restfx)-0.01,maximum(restfx)+0.01])
ax[:set_ylim]([minimum(restfy)-0.01,maximum(restfy)+0.01])
for i = 1:Ncntries
    plot(restfx[i], restfy[i])
    scatter(restfx[i], restfy[i], cntriesStat[i]/100, alpha = 0.25)
end

for i = 1:Ncntries
    annotate(cntries[i],xy=[restfx[i], restfy[i]],)
end
savefig("FIGS/Entities/tf_"*label*".png")

close("all")
#subplot(122)
title("Reuters News with TFIDF: "*label)
xlabel("posX")
ylabel("posY")
ax = axes()
ax[:set_xlim]([minimum(restfidfx)-0.05,maximum(restfidfx)+0.05])
ax[:set_ylim]([minimum(restfidfy)-0.05,maximum(restfidfy)+0.05])
for i = 1:Ncntries
    plot(restfidfx[i], restfidfy[i])
    scatter(restfidfx[i], restfidfy[i], cntriesStat[i]/100, alpha = 0.25)
end

for i = 1:Ncntries
    annotate(cntries[i],xy=[restfidfx[i], restfidfy[i]])
end

savefig("FIGS/Entities/tfidf_"*label*".png")
