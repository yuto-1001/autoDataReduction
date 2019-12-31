#!/usr/bin/env python
# coding: utf-8

# In[31]:


import urllib.request as rq


# In[41]:


if __name__ == "__main__" :
    
    url = input("Enter the URL of image:")
    fileName = "./tmp/tmp.png"
    
    rq.urlretrieve(url, fileName)


# In[ ]:




