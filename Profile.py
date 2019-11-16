#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv(r'C:\Users\vaish\Untitled Folder 1\profile_links.csv')
df


# In[3]:


l = len(df)
print(l)


# In[20]:


links = []
cat = []
for i in range(l):
    links.append(df.loc[i]['Links'])
    cat.append(df.loc[i]['Category'])


# In[31]:


title = []
rating = []
description = []
websites = []
feat = []
pop = []
adds = []
pho = []


# In[32]:


for link in links:
    url = link
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    heading = soup.find("h1", {"class":"heading heading-2"})
    tit = heading.text
    title.append(tit)
    rate = soup.find("div", {"class":"rating-container-star-rating"})
    ratin = rate.text
    rating.append(ratin)
    desc = soup.find("div", {"class":"medium-text fnt-14"})
    descript = desc.text
    description.append(descript)
    website = soup.find_all("a", {"rel":"nofollow"})
    for x in website:
        path = x.get("href")
    if path:
        print(path)
        websites.append(path)
    else:
        websites.append(None)
    features = []
    f = soup.find_all("div", {"class":"flex align-item-center margin-right-10 white-space margin-bottom-10"})
    for y in f:
        #print(y.text)
        features.append(y.text)
    feat.append(features)
    popular = []
    p = soup.find_all("div", {"class":"margin-right-10 category-icons"})
    for t in p:
        #print(t.text)
        popular.append(t.text)
    pop.append(popular)
    ad = []
    add = soup.find_all("div", {"class":"medium-text fnt-14 margin-top-10"})
    for x in add:
        ad.append(x.text)
    if len(ad) != 0:
        address = ad[0]
    else:
        address = None
    if len(ad) > 1:
        phone = ad[1]
    else:
        phone = None
    adds.append(address)
    pho.append(phone)
#print(websites)


# In[33]:


print("{}, {}, {}, {}, {}, {}, {}, {}".format(len(title), len(rating), len(description), len(websites), len(feat), len(pop), len(adds), len(pho)))


# In[34]:


df1 = pd.DataFrame({"Title":title, "Rating":rating, "Description":description, "Website":websites,"Address":adds, "Phone":pho}, index=None)
df1


# In[35]:


df1.to_csv(r'E:\MY PROJECTS\Python\trustvardi.com\Profile_Datas.csv')


# In[18]:


#arr = np.array(["{}".format(title), "{}".format(description), "{}".format(address), "{}".format(phone), "{}".format(link), "{}".format(features), "{}".format(popular), "{}".format(rating), "{}".format(E)])
#arr


# In[19]:


#li = ["{}".format(title), "{}".format(description), "{}".format(address), "{}".format(phone), "{}".format(link), features, popular, "{}".format(rating), "{}".format(E)]


# In[20]:


print(arr)


# In[21]:


#filename = "pro.csv"
#f = open(filename, "w")

#headers = "Title, Description, Address, Phone, Website, Features, Categories, Rating, Positive_Experiences\n"
#f.write(headers)


# In[ ]:


#st = ''
#word = ''
#for data in li:
    #if (type(data) is list):
        #for w in data:
            #word += " -> {},".format(w)
        #st += "{},".format(word)
        #word = ''
    #else:
        #st += "{},".format(data)
        
#print(st)


# In[50]:


#f.write("{}\n".format(st))
#f.close()


# In[23]:


#ar = arr.reshape(1,9)
#df = pd.DataFrame(ar,[0], ['Title', 'Description', 'Address', 'Phone', 'Website', 'Features', 'Categories', 'Ratings', 'Positive_Experience'])
#df


# In[62]:


#df.to_csv(r'C:\Users\vaish\Untitled Folder 1\profiles.csv')


# In[ ]:




