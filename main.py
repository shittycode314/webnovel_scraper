from writeSupplements import *
from SinglePageToC import *
from QidianToC import *
from NovelUpdatesToC import *
from ToCHelper import *
from getChapters import *

writeScriptFile()
writeCssFile()

'''--------------------TABLE OF CONTENTS INPUTS---------------------'''
'''REQUIRED-----------------'''
tocPage = "" #PAGE WITH TABLE OF CONTENTS
src = "src.txt"

'''SINGLE PAGE + NU ---------------'''
req = [] #KEY WORDS (SO not TO PICK UP RANDOM LINKS)
banned = [] #Same principle

'''NU ONLY----------------------'''
sources = []
pages = (1,1,)

'''ToC Helper for NU links to announcement posts rather than the actual chapter (WTF NU) '''
linkClass = ""
linkId = ""
linkReq=[]
linkBanned=[]

'''----------------------ACTUAL CHAPTER SCRAPING INPUTS--------------------'''
'''USEFUL FOR NU AND WUXIAWORLD''' 
linkSupplement = "" #USE IF THE LINKS ON THE SITE DON"T INCLUDE FULL URL

'''NECESSARY AND VARIES'''
contentClass = "" #CLASS OF DIV IN WHICH THE TEXT IS POSTED
contentId = "" #ID OF DIV IN WHICH TEXT IS POSTED
classIndex = 0 #1 for Wuxiaworld due to kindle alert

'''NOT REQUIRED- USE IF TOC DOESN'T CONTAIN CHAPTER TITLE (SUCH AS NU)'''
titleClass = ""
titleId = ""

#Helpful for linking NU novels by different authors (set to false in that cause)
overwrite = True

#contentClass = "cha-words" #Qidian
#contentClass = "fr-view" #WuxiaWorld

'''Self explanitory- only use one getToc depending on format'''

#getSinglePageToc(tocPage, src, req, banned)

#getQidianToC(tocPage, src)

#getNovelupdatesToC(tocPage, src, pages, sources, banned, req)

#ToCHelper(src, linkClass, linkId, linkReq, linkBanned)

#writeToc(src)

#getChapters(src, linkSupplement, contentClass, contentId, classIndex, titleClass, titleId, overwrite)




