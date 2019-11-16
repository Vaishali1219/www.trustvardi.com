#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[4]:


df=pd.read_csv(r'E:\MY PROJECTS\Python\trustvardi.com\CategoryLinks.csv')
df


# In[5]:


l = len(df)
print(l)


# In[6]:


links = []
for i in range(l):
    links.append(df.loc[i]['LINKS'])
links


# In[7]:


for link in links:
    url = link
    category = link.replace('https://www.trustvardi.com/category/', '')
    print(category)


# In[8]:


sub_links = []
cat = []
filename = r'E:\MY PROJECTS\Python\trustvardi.com\Profile_Links.csv'
f = open(filename, "a+")
for link in links:
    url = link
    category = link.replace('https://www.trustvardi.com/category/', '')
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    p = soup.find_all("a", {"class":"page-link"})
    pages = len(p)
    for i in range(1, (pages+1)):
        main_link = "{}?page={}".format(link, i)
        rq = requests.get(main_link)
        soupy = BeautifulSoup(rq.text)
        li = soupy.find_all("div", {"class":"margin-left-10 margin-right-10 pdng-top-10 pdng-bottom-10 flex align-item-center border-bottom-light-grey"})
        for x in li:
            temp = x.find("a")
            sub_links.append("https://www.trustvardi.com{}".format(temp.get("href")))
            cat.append(category)
            row = "https://www.trustvardi.com{}, {}\n".format(temp.get("href"), category)
            f.write(row)
f.close()


# In[9]:


no = len(sub_links)
df = pd.DataFrame({'Links':sub_links, "Category":cat}, index=None)
df


# In[10]:


df.to_csv(r'C:\Users\vaish\Untitled Folder 1\profile_links.csv')


# In[ ]:




