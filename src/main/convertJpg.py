#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import magic
import glob
import pdf2image
import os


# In[ ]:


filePath = 'tmp/tmp*'
fileLists = sorted(glob.glob(filePath))


# In[ ]:


def convert_pdf_to_jpg(fileName, page) :
    saveFileName = fileName.rsplit('.')[0] + '.jpg'
    
    image = pdf2image.convert_from_path(fileName, dpi=600)
    image.save(saveFileName, 'JPEG')    


# In[ ]:


for fileName in fileLists :
    with open(fileName, mode='rb') as f :
        binary = f.read()
    
    mimeType = magic.from_buffer(binary, mime=True)
    if mimeType == 'image/png' :
        print('png')
    elif mimeType == 'image/gif' :
        print('gif')
    elif mimeType == 'application/pdf' :
        print('pdf')
        convert_pdf_to_jpg(fileName, 1)
    else :
        print('unknown format!')


# In[ ]:




