
# coding: utf-8

# In[1]:

import urllib2
import re
import requests
from bs4 import BeautifulSoup


# In[234]:

web = 'http://www.net-a-porter.com/'
url = urllib2.Request(web)
response = urllib2.urlopen(url)
html = response.read()
# print html


# In[235]:

soup = BeautifulSoup(html)
# print soup.prettify()


# In[269]:

# To find Product Type

names = soup.find_all("a", {"class": "nav-level-1"})
product_types=[]
for name in names:
    p_types = name.get_text()
    product_types.append(p_types)
    
product_types


# In[274]:

# To find Product Range

list1 = soup.find_all("a", {"class": "nav-level-1"})
for name in list1:
    names = name.get("href")
    track =['http://www.net-a-porter.com/'+str(names)]
    for link in track: 
#         print link
        if (link == 'http://www.net-a-porter.com//gb/en/Shop/AZDesigners?cm_sp=topnav-_-designers-_-topbar'):
            url = urllib2.Request(link)
            response = urllib2.urlopen(link)
            html1 = response.read()
            soup1 = BeautifulSoup(html1)
            names2 = soup2.find("ul",id="main-nav")
            list2 = names2.find_all("a")
            for name2 in list2:
                range0 = name2.get_text()
                print range0
                
        
    


# In[275]:

l = str(product_types)
print l
expr = re.findall(r'\W\w\W\W+\w\s\w.', l)
expr


# In[243]:




# In[243]:




# In[266]:




# In[181]:




# In[ ]:



