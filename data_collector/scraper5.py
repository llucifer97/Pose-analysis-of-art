#!/usr/bin/env python
# coding: utf-8

# In[33]:


#artstor
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests  


# In[34]:


#link = ['https://library.artstor.org/#/search/europe;size=24;page=1;startDate=500;endDate=1600;sort=0;geography=%5B%22eyJmaWVsZCI6ImhpZXJhcmNoaWVzIiwiZGVwdGgiOjEsImxhYmVscyI6WyJhcnRzdG9yLWdlb2dyYXBoeSIsIkV1cm9wZSJdfQ%3D%3D%22%5D;artclassification_str=%5B%22Paintings%22%5D','https://library.artstor.org/#/search/europe;size=24;page=2;startDate=500;endDate=1600;sort=0;geography=%5B%22eyJmaWVsZCI6ImhpZXJhcmNoaWVzIiwiZGVwdGgiOjEsImxhYmVscyI6WyJhcnRzdG9yLWdlb2dyYXBoeSIsIkV1cm9wZSJdfQ%3D%3D%22%5D;artclassification_str=%5B%22Paintings%22%5D','https://library.artstor.org/#/search/europe;size=24;page=3;startDate=500;endDate=1600;sort=0;geography=%5B%22eyJmaWVsZCI6ImhpZXJhcmNoaWVzIiwiZGVwdGgiOjEsImxhYmVscyI6WyJhcnRzdG9yLWdlb2dyYXBoeSIsIkV1cm9wZSJdfQ%3D%3D%22%5D;artclassification_str=%5B%22Paintings%22%5D','https://library.artstor.org/#/search/europe;size=24;page=4;startDate=500;endDate=1600;sort=0;geography=%5B%22eyJmaWVsZCI6ImhpZXJhcmNoaWVzIiwiZGVwdGgiOjEsImxhYmVscyI6WyJhcnRzdG9yLWdlb2dyYXBoeSIsIkV1cm9wZSJdfQ%3D%3D%22%5D;artclassification_str=%5B%22Paintings%22%5D','https://library.artstor.org/#/search/europe;size=24;page=5;startDate=500;endDate=1600;sort=0;geography=%5B%22eyJmaWVsZCI6ImhpZXJhcmNoaWVzIiwiZGVwdGgiOjEsImxhYmVscyI6WyJhcnRzdG9yLWdlb2dyYXBoeSIsIkV1cm9wZSJdfQ%3D%3D%22%5D;artclassification_str=%5B%22Paintings%22%5D','https://library.artstor.org/#/search/europe;size=24;page=6;startDate=500;endDate=1600;sort=0;geography=%5B%22eyJmaWVsZCI6ImhpZXJhcmNoaWVzIiwiZGVwdGgiOjEsImxhYmVscyI6WyJhcnRzdG9yLWdlb2dyYXBoeSIsIkV1cm9wZSJdfQ%3D%3D%22%5D;artclassification_str=%5B%22Paintings%22%5D','https://library.artstor.org/#/search/europe;size=24;page=7;startDate=500;endDate=1600;sort=0;geography=%5B%22eyJmaWVsZCI6ImhpZXJhcmNoaWVzIiwiZGVwdGgiOjEsImxhYmVscyI6WyJhcnRzdG9yLWdlb2dyYXBoeSIsIkV1cm9wZSJdfQ%3D%3D%22%5D;artclassification_str=%5B%22Paintings%22%5D']


# In[35]:


URL = ['http://www.catalogo.beniculturali.it/sigecSSU_FE/mostraTutteLeSchede.action?numeroPagina=1&valoreRicerca=annunciazione&countSize=1428&numElement=1413&nomeBread=Beni%20culturali&statoCosa1=&statoCosa2=&statoDove1=&statoDove2=&statoQuando1=&statoChi1=&numeroComplessivoPagine=72&mostraSchede=true&contenitore=&flagFisicoGiuridico=0&stringBeneCategoria=','http://www.catalogo.beniculturali.it/sigecSSU_FE/mostraTutteLeSchede.action?numeroPagina=2&valoreRicerca=annunciazione&countSize=1428&numElement=1413&nomeBread=Beni+culturali&statoCosa1=&statoCosa2=&statoDove1=&statoDove2=&statoQuando1=&statoChi1=&numeroComplessivoPagine=72&mostraSchede=true&contenitore=&flagFisicoGiuridico=0&stringBeneCategoria=','http://www.catalogo.beniculturali.it/sigecSSU_FE/mostraTutteLeSchede.action?numeroPagina=3&valoreRicerca=annunciazione&countSize=1428&numElement=1413&nomeBread=Beni+culturali&statoCosa1=&statoCosa2=&statoDove1=&statoDove2=&statoQuando1=&statoChi1=&numeroComplessivoPagine=72&mostraSchede=true&contenitore=&flagFisicoGiuridico=0&stringBeneCategoria=','http://www.catalogo.beniculturali.it/sigecSSU_FE/mostraTutteLeSchede.action?numeroPagina=4&valoreRicerca=annunciazione&countSize=1428&numElement=1413&nomeBread=Beni+culturali&statoCosa1=&statoCosa2=&statoDove1=&statoDove2=&statoQuando1=&statoChi1=&numeroComplessivoPagine=72&mostraSchede=true&contenitore=&flagFisicoGiuridico=0&stringBeneCategoria=','http://www.catalogo.beniculturali.it/sigecSSU_FE/mostraTutteLeSchede.action?numeroPagina=5&valoreRicerca=annunciazione&countSize=1428&numElement=1413&nomeBread=Beni+culturali&statoCosa1=&statoCosa2=&statoDove1=&statoDove2=&statoQuando1=&statoChi1=&numeroComplessivoPagine=72&mostraSchede=true&contenitore=&flagFisicoGiuridico=0&stringBeneCategoria=','http://www.catalogo.beniculturali.it/sigecSSU_FE/mostraTutteLeSchede.action?numeroPagina=7&valoreRicerca=annunciazione&countSize=1428&numElement=1413&nomeBread=Beni+culturali&statoCosa1=&statoCosa2=&statoDove1=&statoDove2=&statoQuando1=&statoChi1=&numeroComplessivoPagine=72&mostraSchede=true&contenitore=&flagFisicoGiuridico=0&stringBeneCategoria=','','','','']


# In[36]:


len(URL)


# In[37]:


URL[1]


# In[39]:


r = requests.get(URL[0]) 
r.content
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify())


# In[41]:


all_images = soup.find_all('img')
all_images

