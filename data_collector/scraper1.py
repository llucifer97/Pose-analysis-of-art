#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
from bs4 import BeautifulSoup
import requests  
import os


# In[5]:


data = pd.read_excel('./catalog.xls')  


# In[6]:


data.info()


# In[8]:


data['URL'].tail(6)



# In[9]:


data.columns


# In[10]:


data.sort_values(['SCHOOL', 'TIMEFRAME'], ascending = False)


# In[11]:


data.count()


# In[12]:


url = data.iloc[: ,6 ]


# In[13]:


url.head()


# In[14]:


url[1]


# In[18]:


i = 0
x = url[i]
arr = []
for i in range(46713):
    x = url[i]
    arr.append(x)
    ++i


# In[23]:


len(arr)


# In[20]:


#web scraper
URL = arr[0]
r = requests.get(URL) 
#print(r.content) 


# In[21]:


soup = BeautifulSoup(r.content, 'html5lib') 
#print(soup.prettify()) 


# In[22]:


all_images = soup.find_all('a')
for image in all_images:
    print('https://www.wga.hu' +  image['href'])

# In[31]:


il= [] 
for i in range(37806,46713): 
    URL = arr[i] 
    r = requests.get(URL)

    #print(r.content) 

    soup = BeautifulSoup(r.content, 'html5lib') 
#print(soup.prettify()) 

    all_images = soup.find_all('a')
    for image in all_images:
        #print('https://www.wga.hu' +  image['href'])
        s = 'https://www.wga.hu' +  image['href'] 
        if s[-4:] == ".jpg":
            il.append(s)
            print(i)
            print(s)
        else:
            print('not to be printed')


# In[ ]:


def download_image(x):
    for i in range(len(x)):
        # URL of the image to be downloaded is defined as image_url 
        r = requests.get(il[i]) # create HTTP response object 
        os.chdir('/home/ayushraj/Desktop/13mayubuntuformat/gsocdataset/wgadata9')  
        # send a HTTP request to the server and save 
        # the HTTP response in a response object called r 
        with open("wgadata"  + str(i) + ".jpg",'wb') as f: 

            # Saving received content as a png file in 
            # binary format 

            # write the contents of the response (r.content) 
            # to a new file in binary mode. 
            f.write(r.content) 


# In[ ]:


download_image(il)


