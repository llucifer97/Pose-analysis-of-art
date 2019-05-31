#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests  
import os


# In[28]:





# In[ ]:





# In[31]:


r = requests.get('http://www.christianiconography.info/') 


# In[32]:





# In[39]:


all_images = soup.find_all('a')
arr = []
len(all_images)


# In[36]:


for i in range():
    url = all_images[i]
    arr.append(url)
    print(url)
    


# In[7]:


arr[4]


# In[8]:


il = []
for image in arr:
    #print('https://www.wga.hu' +  image['href'])
    s = 'https://iconographic.warburg.sas.ac.uk/vpc/VPC_search/' +  image['href'] 
    il.append(s)
    print(s)
      
          


# In[9]:


res = requests.get(il[4]) 


# In[ ]:





# In[10]:


gesturesoup = BeautifulSoup(res.content, 'html5lib') 
#print(soup.prettify()) 


# In[11]:


gesture = gesturesoup.find_all('a')
ges = []


# In[12]:


arrges = []
for i in range(5,len(gesture)):
    url = gesture[i]
    arrges.append(url)
    #print(url)
    
    


# In[13]:


ilges = []
for image in arrges:
    #print('https://www.wga.hu' +  image['href'])
    sges = 'https://iconographic.warburg.sas.ac.uk/vpc/VPC_search/' +  image['href'] 
    ilges.append(sges)
    #print(sges)
      


# In[ ]:





# In[14]:


#finding all the <a> tag under antique section
res = requests.get(il[0])
antiquesoup = BeautifulSoup(res.content, 'html5lib') 
antique = antiquesoup.find_all('a')


# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:


res1 = requests.get(ilges[4]) 


# In[17]:


res1.content
gesturesoupimg = BeautifulSoup(res1.content, 'html5lib') 
#print(gesturesoupimg.prettify()) 


# In[18]:


gestureimg = gesturesoupimg.find_all('img')


# In[19]:


ilimg = []
for image in gestureimg:
    #print('https://www.wga.hu' +  image['href'])
    s = 'https://iconographic.warburg.sas.ac.uk/vpc/VPC_search/' +  image['src'] 
    ilimg.append(s)
    print(s)


# In[20]:


ilimg = []
for i in range(len(ilges)):
    res1 = requests.get(ilges[i]) 
    gesturesoupimg = BeautifulSoup(res1.content, 'html5lib') 
    imge = gesturesoupimg.find_all('img')
    print(i)

    for image in imge:
        #print('https://www.wga.hu' +  image['href'])
        s = 'https://iconographic.warburg.sas.ac.uk/vpc/VPC_search/' +  image['src']
        if s[-5:] == ".jpg?":
            ilimg.append(s)
            print(s)
        else:
            print('not to be printed')


# In[21]:


def makeDir(dirName):
    if not os.path.exists('/Documents/' + dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")


# In[22]:


def download_image(x):
    for i in range(len(x)):
        # URL of the image to be downloaded is defined as image_url 
        r = requests.get(ilimg[i]) # create HTTP response object 
        os.chdir('/home/ayushraj/Desktop/warburgData')  
        # send a HTTP request to the server and save 
        # the HTTP response in a response object called r 
        with open("gesture" + str(i) + ".jpg",'wb') as f: 

            # Saving received content as a png file in 
            # binary format 

            # write the contents of the response (r.content) 
            # to a new file in binary mode. 
            f.write(r.content) 
    


# In[23]:


download_image(ilimg[2])


# In[24]:


def image_url(src):
    res = requests.get(src)
    res.content
    soup = BeautifulSoup(res1.content, 'html5lib') 
    #print(gesturesoupimg.prettify()) 
    typeimg = soup.find_all('img')
    return typeimg

    


# In[25]:


def image_full_url():
    ilimg = []
    for image in gestureimg:
        #print('https://www.wga.hu' +  image['href'])
        s = 'https://iconographic.warburg.sas.ac.uk/vpc/VPC_search/' +  image['src'] 
        ilimg.append(s)
        print(s)


# In[ ]:





# In[ ]:





# In[71]:





# In[72]:


s = 'https://artmuseum.princeton.edu/search/collections?keys=&title=&display_name=&classification=1&collection=599&year_range_op=contains&year_range%5Bvalue%5D=&year_range%5Bmin%5D=&year_range%5Bmax%5D=&credit_line=&invno=&peopleid=&sort_bef_combine=date_begin+ASC'


# In[73]:


type(s)


# In[74]:



s = link.split("/") 
s[-3] = n


# In[75]:


s


# In[61]:


n = '170,'

