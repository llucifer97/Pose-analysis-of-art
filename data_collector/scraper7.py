#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://artmuseum.princeton.edu/


# In[2]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests  
import os


# In[22]:


home_link = 'https://artmuseum.princeton.edu/search/collections?keys=&title=&display_name=&classification=1&collection=599&year_range_op=contains&year_range%5Bvalue%5D=&year_range%5Bmin%5D=&year_range%5Bmax%5D=&credit_line=&invno=&peopleid=&sort_bef_combine=date_begin+ASC'


# In[23]:


s = 'https://artmuseum.princeton.edu/search/collections?keys=&title=&display_name=&classification=1&collection=599&year_range_op=contains&year_range%5Bvalue%5D=&year_range%5Bmin%5D=&year_range%5Bmax%5D=&credit_line=&invno=&peopleid=&sort_bef_combine=date_begin%20ASC&page='
url = []


# In[24]:


for i in range(59):
    print(i)
    u = s + str(i)
    print(u)
    url.append(u)


# In[25]:


url.append(home_link)


# In[37]:


img = []
for i in range(60):
    print(i)
    r = requests.get(url[i]) 
    r.content
    soup = BeautifulSoup(r.content, 'html5lib') 

    all_images = soup.find_all('img')
    
    for image in all_images:
        #print('https://www.wga.hu' +  image['href'])
        s =  image['data-src']
        if s[-4:] == ".jpg":
            img.append(s)
            print(s)
        else:
            print('not to be printed')
    


# In[ ]:





# In[83]:


n = '300,'
def link_modifier(url):
    s = url.split("/")
    s[-3] = n
    t = '/'.join([str(x) for x in s])
    return t
link_modifier(img[2])
    


# In[85]:


for j in range(len(img) + 1):
    link_modifier(img[j])
    print(j)
    print(link_modifier(img[j]))


# In[86]:


def makeDir(dirName):
    if not os.path.exists('/home/ayushraj/Desktop/' + dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")


# In[112]:


def download_image(x):
    for i in range(len(x)):
        # URL of the image to be downloaded is defined as image_url 
        r = requests.get(img[i]) # create HTTP response object 
        os.chdir('/home/ayushraj/Desktop/artmuseum' )  
        # send a HTTP request to the server and save 
        # the HTTP response in a response object called r 
        with open("princeton"  + str(i) + ".jpg",'wb') as f: 

            # Saving received content as a png file in 
            # binary format 

            # write the contents of the response (r.content) 
            # to a new file in binary mode. 
            f.write(r.content) 
        onlyfiles = next(os.walk('/home/ayushraj/Desktop/artmuseum'))[2]
        #dir is your directory path as string
       
        print( 'Downloded:' + str(len(onlyfiles)/len(x)*100))


# In[113]:


makeDir('artmuseum')


# In[114]:


download_image(img)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




