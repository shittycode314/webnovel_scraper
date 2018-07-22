import requests
from bs4 import BeautifulSoup

def getSinglePageToc(site, src, req, banned):
    page = requests.get(site)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("a")
    file = open(src, "w+", encoding = 'utf-8')

    for link in links:
        text = link.text.replace("\n","")
        good = True
        for x in banned:
            if x.lower() in text.lower():
                good = False
                break;
        for x in req:
            if x.lower() not in text.lower():
                good = False
                break;
        if not good:
            continue
        file.write(text + "==>>" + link['href']+"\n")
    file.close()