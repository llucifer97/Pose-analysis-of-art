#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ashmolean  website
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests  
import os


# In[20]:


URL = ['http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/50/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/75/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/100/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/125/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/150/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/175/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/200/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/225/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/250/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/275/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/300/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/325/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/350/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/375/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/400/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/425/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/450/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/475/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/500/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/525/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/550/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/575/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/600/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/625/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/650/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/675/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/700/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/725/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/750/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/775/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/800/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/825/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/850/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/875/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/900/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/925/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/950/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/975/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/1000/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid','http://collections.ashmolean.org/collection/browse-9148/per_page/25/offset/1025/sort_by/random/sort_order/asc/category/paintings/start/520/end/1720/view_as/grid']


# In[22]:


len(URL)


# In[ ]:


for i in range(40)


# In[25]:


r = requests.get(URL) 
r.content
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify())


# In[23]:


all_images = soup.find_all('div')
len(all_images)


# In[24]:


all_images


# In[6]:


img = []
for image in all_images:
    #print('https://www.wga.hu' +  image['href'])
    s =  image['src']
    if s[-4:] == ".jpg":
        img.append(s)
        print(s)
    else:
        print('not to be printed')

# In[11]:


def makeDir(dirName):
    if not os.path.exists('/home/ayushraj/Desktop/' + dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")


# In[12]:


makeDir('Ashmolean')


# In[9]:


def download_image(x):
    for i in range(len(x)):
        # URL of the image to be downloaded is defined as image_url 
        r = requests.get(img[i]) # create HTTP response object 
        os.chdir('/home/ayushraj/Desktop/Ashmolean')  
        # send a HTTP request to the server and save 
        # the HTTP response in a response object called r 
        with open("Ashmolean" + str(2) + str(i) + ".jpg",'wb') as f: 

            # Saving received content as a png file in 
            # binary format 

            # write the contents of the response (r.content) 
            # to a new file in binary mode. 
            f.write(r.content) 

# In[10]:


len(img)

