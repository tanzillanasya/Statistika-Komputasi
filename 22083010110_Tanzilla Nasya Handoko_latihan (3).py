#!/usr/bin/env python
# coding: utf-8

# UKURAN PEMUSATAN DATA DAN PENYEBARAN 

# In[13]:


### rata2 untuk pemusatan data
import statistics as st
tinggi =(156,176,153,180,165)
rata2 = st.mean(tinggi)
print("rata2nya adalah",rata2)


# In[12]:


def mean(tinggi):
    tinggi =(156,176,153,180,165)
    return sum(tinggi)/len (tinggi)
print("rata2 nya adalah",rata2)


# In[16]:


tinggi = (156,176,153,180,165)
bb =(20, 5, 10, 3, 15)
total_bb= sum(bb)


# In[17]:


def rata2():
    nilai_bb =(tinggi[i] * bb[i] for i in range(len(tinggi)))
    return sum(nilai_bb)/total_bb
rata2()


# In[7]:


### MEDIAN 
tinggi = [156, 176, 153, 180, 165, 170]
tinggi.sort()
tinggi


def nilai_tengah(tinggi):
    tinggi.sort()
    n = len(tinggi)
    i_tengah = n // 2

    if n % 2 == 1:
       return tinggi[i_tengah]
    else:
      return((tinggi[i_tengah-1] + tinggi[i_tengah])/2)

print("mediannya adalah", nilai_tengah(tinggi))


# In[5]:


tinggi = (156,176,153,180,165,170,165,156,156)
from collections import Counter
tinggi_counter = Counter(tinggi)
print(tinggi_counter)


# In[ ]:


##modus


# In[ ]:





# In[ ]:





# UKURAN PENYEBARAN DATA

# In[8]:


#RANGE
print('nilai inputan tinggi mahasiswa')
tinggi= [int(x) for x in input().split()]
def nilai_range(tinggi):
    return max(tinggi)-min(tinggi)
print('hasil range dari data tinggi adalah', nilai_range(tinggi)) 


# In[10]:


#variance
print('nilai inputan tinggi mahasiswa')
tinggi= [int (x) for x in input().split()]
def varians(tinggi):
    diff = 0
    rata2 = sum(tinggi)/len(tinggi)
print('hasil varian adalah', varians(tinggi))


# In[ ]:




