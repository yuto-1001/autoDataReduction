#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request as rq
import magic
import json
import PyPDF2
import io


# In[ ]:


count = 0


# In[ ]:


def downloadPdf(url, page='all') :
    try :
        global count
        
        data = rq.urlopen(url).read()
        fileType = magic.from_buffer(data, mime=True)
        
        if fileType != 'application/pdf' :
            return False
        
        with open('./tmp/pdf_tmp.pdf', mode='wb') as f :
            f.write(data)
        
        maxPage = PyPDF2.PdfFileReader('./tmp/pdf_tmp.pdf').getNumPages()
        
        pagesList = []
        
        if page == 'all' :
            pagesList = list(range(maxPage))
            print('page == all')
            
        else :
            tmpList = [x.strip() for x in page.split(',')]
            print('page != all')
            for value in tmpList :
                if '-' in value :
                    rng = value.split('-')
                    
                    tmp = rng[0]
                    if len(tmp) == 0 :
                        tmp = 0
                    rngFirst = int(tmp)
                    
                    tmp = rng[len(rng) - 1]
                    if len(tmp) == 0 :
                        tmp = maxPage
                    rngEnd = int(tmp)
                    
                    if  type(rngFirst) == int and type(rngEnd) == int :
                        pagesList += range(rngFirst, min(maxPage, rngEnd))
                
                elif type(value) == int :
                    pagesList += min(maxPage, value)
                
        with open('./tmp/pdf_tmp.pdf', mode='rb') as pdfData :
            for pageNum in pagesList :
                fileName = './tmp/tmp' + str(count) + '.pdf'

                merger = PyPDF2.PdfFileMerger()
                merger.append(pdfData, pages=(pageNum, pageNum + 1))

                merger.write(fileName)
                merger.close()

                count += 1
        
        return True
        
    except Exception as e :
        print(e)
        return False 


# In[ ]:


if __name__ == '__main__' :
    url = input('Enter the URL of image:')
    print(downloaPdf(url, page='0, -2'))

