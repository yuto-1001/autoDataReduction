#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request as rq
import magic
import json

def download_tmp_file(url, number) :
    fileName = './tmp/tmp' + str(number)
    dicFile = './mimeDic.json'

    try :
        data = rq.urlopen(url).read()
        fileType = magic.from_buffer(data, mime=True)

        with open(dicFile) as dic :
            mimeDic = json.load(dic)

        extension = mimeDic[fileType]
        fileName += extension

        with open(fileName, mode='wb') as file :
            file.write(data)
        return True
    
    except Exception as e :
        print(e)
        return False

if __name__ == '__main__' :
    url = input('Enter the URL of image:')
    print(download_tmp_file(url, 4))


# In[ ]:




