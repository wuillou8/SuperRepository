using DataFrames

function reshape (subdf)
    #===
    function reshaping the dataframe. 
    ===#
    headSubdf = head(subdf,1)
    N, M = size(subdf)[1], size(subdf)[2]
    for i = 1:N
        for j = 1:M
            if  isna(subdf[i, j])
                subdf[i, j] = headSubdf[j][1]
            end
        end
    end
    subdf
end


df = DataFrames.readtable("Daughterproducts_exportCSV.csv")
# hack to force an empty dataframe iwth the same header as df...
dfOut = df[df[:Handle] .== "007Isjair", :]

dfs = [ reshape(subdf) for subdf in groupby(df, :Handle) ]
for tmp_df in dfs
    append!(dfOut,tmp_df)
end

    writetable("DaugtherProductsNewFormat.csv", dfOut)
