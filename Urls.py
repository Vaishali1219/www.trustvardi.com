#!/usr/bin/env python
# coding: utf-8

# In[96]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[97]:


url = "https://www.trustvardi.com/category"


# In[98]:


r = requests.get(url)


# In[99]:


soup = BeautifulSoup(r.text)


# In[100]:


links = []


# In[101]:


li = soup.find("div",{"class":"category-inner-container"})
y = li.find_all("a")
for l in y:
    t = l.get("href")
    links.append("https://www.trustvardi.com{}".format(t))
links


# In[102]:


arr = np.array(links)
no = len(links)
ar = arr.reshape(no,1)
df = pd.DataFrame(ar)
df.rename(columns={0: 'Links'}, inplace=True)
df


# In[103]:


df.to_csv(r'E:\MY PROJECTS\Python\trustvardi.com\CategoryLinks.csv', index=False)


# In[104]:


temp = []


# In[105]:


lin = soup.find("div",{"class":"category-inner-container"})
g = lin.find_all("a")
for l in g:
    t = "https://www.trustvardi.com{}".format(l.get("href"))
    if t not in links:
        temp.append("https://www.trustvardi.com{}".format(t))
arry = np.array(temp)
n = len(temp)
ary = arry.reshape(n,1)
dtf = pd.DataFrame(ary)
dtf.rename(columns={0: 'Links'}, inplace=True)
dtf


# In[109]:


filename = r'E:\MY PROJECTS\Python\trustvardi.com\CategoryLinks.csv'
f = open(filename, "a+")
if len(temp) != 0:
    for i in range((len(temp)+1)):
        row = "{}".format(dtf.loc[i]['Links'])
        print(row)
        f.write(row)
f.close()


# In[ ]:





# In[ ]:




