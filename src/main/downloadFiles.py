import urllib.request as rq
import magic
import json
import PyPDF2
import io

count = 0

def downloadTmpPdf(data, page='all') :
    try :
        global count
        
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
                
                else :
                    print(value)
                    page = int(value)
                    pagesList.append(min(maxPage, page))
                
        with open('./tmp/pdf_tmp.pdf', mode='rb') as pdfData :
            for pageNum in pagesList :
                fileName = './tmp/tmp' + str(count) + '.pdf'
                print(fileName)

                merger = PyPDF2.PdfFileMerger()
                merger.append(pdfData, pages=(pageNum, pageNum + 1))

                merger.write(fileName)
                merger.close()

                count += 1
        
        return True
        
    except Exception as e :
        print(e)
        return False 

def downloadTmpFile(data, extension) :
    try :
        global count
        
        fileName = './tmp/tmp' + str(count) + extension
        print(fileName)

        with open(fileName, mode='wb') as dwldFile:
            dwldFile.write(data)

        count += 1
        
        return True
        
    except Exception as e :
        print(e)
        return False

def getExtension(data) :
    mimeType = magic.from_buffer(data, mime=True)
    print(mimeType)
    with open('mimeDic.json', mode='r') as dic :
        typeDic = json.load(dic)
        
    if(mimeType in typeDic) :
        return typeDic[mimeType]
    
    return False

def downloadFile(url, pages) :
    print('url:' + url + '    page:' + pages)
    file = rq.urlopen(url).read()
    extension = getExtension(file)
    
    if not extension :
        print("This file can't download this System!")
        return False
    
    elif extension == '.pdf' :
        downloadTmpPdf(file, pages)
    
    else :
        downloadTmpFile(file, extension)

if __name__ == '__main__' :
    with open('downloadUrlList.json', mode='r') as urlList :
        urlDic = json.load(urlList)
    
    for i in range(len(urlDic['url'])) :
        downloadFile(urlDic['url'][i], urlDic['pages'][i])


