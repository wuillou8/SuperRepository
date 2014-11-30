#=
	script checking the tfidf computation with small files
=#
sim_tfidf(v1,v2) = dot(v1,v2) #/sqrt(dot(v1,v1)*dot(v2,v2))

function tf_idfVectorise(_dict, idfvect, arr)
    vec = zeros(size(idfvect)[1])
    [ vec[_dict[i]] += idfvec[_dict[i]] for i in arr ]
    #vec
    vec/dot(vec,vec)
end

dic = readdlm("TOY/dict")[1:end,1]
num = 0
dic = {i => num+=1 for i in dic}
idfvec = readdlm("TOY/tf_idf")[1:end,1];
doc1 = readdlm("doc1")[1:end,1]
doc2 = readdlm("doc2")[1:end,1]

v1=tf_idfVectorise(dic,idfvec,doc1)
v2=tf_idfVectorise(dic,idfvec,doc2)
sim_tfidf(v1,v2)
