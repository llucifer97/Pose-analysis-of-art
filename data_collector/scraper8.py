#!/usr/bin/env python
# coding: utf-8

# In[3]:


#new.xlxs wga data
import pandas as pd
from bs4 import BeautifulSoup
import requests  


# In[4]:


data = pd.read_excel('new.xls')  


# In[5]:


data.info()


# In[6]:


data['URL'].tail(600)


# In[ ]:





# In[7]:


data.columns


# In[8]:


data.sort_values(['SCHOOL', 'TIMEFRAME'], ascending = False)


# In[9]:


data.count()


# In[10]:


url = data.iloc[: ,6 ]


# In[11]:


url.head()


# In[12]:


url[1]


# In[14]:


i = 0
x = url[i]
arr = []
for i in range(687):
    x = url[i]
    arr.append(x)
    ++i


# In[15]:


arr[7]


# In[16]:


#web scraper
URL = arr[0]
r = requests.get(URL) 
#print(r.content) 


# In[17]:


soup = BeautifulSoup(r.content, 'html5lib') 
#print(soup.prettify()) 


# In[18]:


all_images = soup.find_all('a')
for image in all_images:
    print('https://www.wga.hu' +  image['href'])


# In[22]:


#webscraper
il = []
for i in range(687):
    print(i)

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
            print(s)
        else:
            print('not to be printed')
        


# In[ ]:





# In[ ]:


#downloading data
image = arr[]


# In[ ]:





# In[24]:


il[6]


# In[25]:


len(il)


# In[26]:


def download_image(x):
    for i in range(len(x)):
        # URL of the image to be downloaded is defined as image_url 
        r = requests.get(il[i]) # create HTTP response object 
        os.chdir('/home/ayushraj/Desktop/newgadata')  
        # send a HTTP request to the server and save 
        # the HTTP response in a response object called r 
        with open("newgadata"  + str(i) + ".jpg",'wb') as f: 

            # Saving received content as a png file in 
            # binary format 

            # write the contents of the response (r.content) 
            # to a new file in binary mode. 
            f.write(r.content) 


# In[27]:


def makeDir(dirName):
    if not os.path.exists('/home/ayushraj/Desktop/' + dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")


# In[28]:


import os
makeDir('newgadata')
download_image(il)


# In[244]:


il[10783]

