#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import magic
import glob
import pdf2image


# In[ ]:


def convertPdf(fileName) :
    saveFileName = fileName.rsplit('.', 1)[0] + '.jpg'
    
    image = pdf2image.convert_from_path(fileName, dpi=600)
    image[0].save(saveFileName, 'JPEG')   
    print(saveFileName)


# In[ ]:


def organizeTmpData(fileList) :
    for fileName in fileList :
        print(fileName)
        with open(fileName, mode='rb') as f :
            binary = f.read()

        mimeType = magic.from_buffer(binary, mime=True)

        if mimeType == 'application/pdf' :
            print('pdf')
            convertPdf(fileName)
            print('compleate!')


# In[ ]:


filePath = './tmp/tmp*'
fileList = sorted(glob.glob(filePath))

organizeTmpData(fileList)


# In[ ]:




