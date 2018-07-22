# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:01:39 2018

@author: Henry
"""
import requests
from bs4 import BeautifulSoup

def getNovelupdatesToC(site, src, pages, sources, banned, req):
    urls = []
    for i in range(pages[0], pages[1]+1):
        url = site+"/?pg="+str(i)
        print("Scraping "+ url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        rows = soup.find_all("tr")
        for row in rows:
            try:
                author = row.find_all("a")[0].text
                link = row.find_all("a")[1]
            except:
                continue
            
            text = link.text
            good = True
            
            for x in sources:
                good = False
                if x.lower() in author.lower():
                    good = True
                
            for x in banned:
                if x.lower() in text.lower():
                    good = False
                    
            for x in req:
                if x.lower() not in text.lower():
                    good = False
                    
            if not good:
                continue
                
            urls.append(text + "==>>" + "http:"+link['href']+"\n")
            
    file = open(src, "w+", encoding = 'utf-8')    
    for x in reversed(urls):
        file.write(x)
    file.close()