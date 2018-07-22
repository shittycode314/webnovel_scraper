# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:03:10 2018

@author: Henry
"""
import requests
from bs4 import BeautifulSoup

def ToCHelper(src, linkClass, linkId, req, banned):
    with open(src, "r",  encoding = "utf-8") as file:
        pages = list(filter(None, file.read().split("\n")))   
        
    file = open(src, "w+",  encoding = "utf-8") 
    
    for i, x in enumerate(pages):
        title, url = x.split("==>>")
        print("Scraping " + url)

        
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            if linkId:
                wrapper = soup.find("div", id = linkId)
            else:
                wrapper = soup.find("div", {"class": linkClass})
            
            links = wrapper.find_all("a")
            
            for link in links:
                text = link.text
                good = True
                for x in banned:
                    if x.lower() in text.lower():
                        good = False
                        
                for x in req:
                    if x.lower() not in text.lower():
                        good = False
                if good:
                    file.write(title+"==>>"+link['href']+"\n")
                    break;
                
        except:
            file.write(title+"==>>"+url)

    file.close()