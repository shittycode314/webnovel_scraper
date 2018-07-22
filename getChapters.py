import requests
from bs4 import BeautifulSoup
import string

src = "src.txt"
linkSupplement = "" #USE IF THE LINKS ON THE SITE DON"T INCLUDE FULL URL
contentClass = "" #CLASS OF DIV IN WHICH THE TEXT IS POSTED
contentId = "" #ID OF DIV IN WHICH TEXT IS POSTED

#CONVERT FILENAMES AND TEXT
def fix(obj):
    return obj.encode('utf8', 'ignore').decode('utf8', 'ignore')

def fixName(name):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in name if c in valid_chars)
    filename = filename.replace(' ','_')
    return filename

def writeToc(src):
    with open(src, "r",  encoding = "utf-8") as file:
        pages = list(filter(None, file.read().split("\n")))    
        
    with open("toc.html", "w+", encoding = 'utf-8') as tocFile:
        tocFile.write("<html><head><link rel='stylesheet' type='text/css' href='style.css'><title> Table of Contents</title></head><body>")
        tocFile.write("<h1>Table of Contents</h1><br>")
        for x in pages:
            title, url = x.split("==>>")
            tocFile.write("<p><a href = '"+fixName(title)+".html'>"+title+"</a></p>")


def getChapters(src, linkSupplement, contentClass, contentId, classIndex, titleClass, titleId, overwrite):
    
    with open(src, "r",  encoding = "utf-8") as file:
        pages = list(filter(None, file.read().split("\n")))   
        
    for i, x in enumerate(pages):
        title, url = x.split("==>>")
        print("Scraping " + title)
        try:
            prevTitle = fixName(pages[i-1].split("==>>")[0])+".html"
        except:
            prevTitle = ""
        try:
            nextTitle = fixName(pages[i+1].split("==>>")[0])+".html"
        except:
            nextTitle = ""
        
        if not overwrite:
            try:
                file = open(fixName(title)+".html", 'r',  encoding='utf-8')
                continue
            except:
                pass
                
        
        file = open(fixName(title)+".html", 'w+',  encoding='utf-8')
        
        try:
            url = linkSupplement+url
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            if contentId:
                content = str(soup.find("div", id = contentId))
            else:
                content = str(soup.find_all("div", {"class": contentClass})[classIndex])
                
        except Exception as e:
            print("Failed to scrape chapter " + title)
            print("Exception: "+ str(e))
            break
        
        if titleId:
                title = fix(soup.find("div", id = contentId).text)
        elif titleClass:
                title = fix(soup.find("div", {"class": contentClass}).text)
        
        file.write("<html><head><link rel='stylesheet' type='text/css' href='style.css'><title> "+title+ "</title></head><body>")
        file.write("<h1>"+title+"</h1><br>")

        try:
            file.write(fix(content))
        except Exception as e:
            print("Failed to write to file " + title)
            print("Exception: "+ str(e))
            continue
            
        file.write("<div id = 'links'><a id = 'prev' href = '"+prevTitle+"'>Previous Chapter</a> | ")
        file.write("<a id = 'toc' href = 'toc.html'>Table of Contents</a> | ")
        file.write("<a id = 'next' href = '"+ nextTitle+"'>Next Chapter</a></div>")
        
        file.write("<script src='script.js'></script>")
        file.write("<br><p>Scraped by Chenry</p></body></html>")
        file.close()

