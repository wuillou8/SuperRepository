
# coding: utf-8

# In[34]:

#=
    Dealing with the communication with NLTK(Python) -- Julia
=#
using PyCall
@pyimport nltk
@pyimport nltk.stem as nltk_stem
# example
tokens = ["player","playa","wife's","playas", "pleyaz", "players", "fishs", "betrayers"] 


# In[39]:

# Porter Stemming
@pyimport nltk_stem.porter as nltk_stem_porter
porter = nltk_stem_porter.PorterStemmer()
[ pycall(porter["stem"], PyAny, i) for i in tokens ]


# In[60]:

# Lancaster Stemming
lancaster = nltk_stem.LancasterStemmer()
using Lazy
@>> tokens map(x->pycall(lancaster["stem"], PyAny,x))


# In[55]:

# Snowball Stemming 
snowball = nltk_stem.SnowballStemmer("english")
[ pycall(snowball["stem"], PyAny, i) for i in tokens ]
tokens |> a -> map(x->pycall(snowball["stem"], PyAny, x) ,a)

