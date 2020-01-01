#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request as rq
import magic
import json

url = input("Enter the URL of image:")
fileName = "./tmp/tmp"

data = rq.urlopen(url).read()


# In[ ]:


type = magic.from_buffer(data, mime=True)

with open('./mimeDic.json') as f :
    mimeDic = json.load(f)

extension = mimeDic[type]
fileName += extension
fileName


# In[ ]:


with open(fileName, mode='wb') as file :
    file.write(data)


# In[ ]:




