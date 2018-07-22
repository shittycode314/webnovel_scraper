# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:02:14 2018

@author: Henry
"""

import requests
from bs4 import BeautifulSoup
import re
import json

def getQidianToC(site, src):
    re_book_id = re.compile(r'webnovel.com/book/(\d*)/?.*')
    match = re.search(re_book_id, site)
    if not match:
        print ("Table of contents URL %s is invalid" % site)
    book_id = match.group(1)
    chapter_info = requests.get('https://www.webnovel.com/apiajax/chapter/GetChapterList?bookId=%s' %book_id)
    js_ch = json.loads(chapter_info.text)    
    file = open(src, "w+", encoding = 'utf-8')
    for chapters in js_ch['data']['volumeItems']:
        for x in chapters['chapterItems']:
            file.write(x["name"] + "==>>https://www.webnovel.com/book/" + book_id +"/" + x["id"] + "\n")
    file.close()
    