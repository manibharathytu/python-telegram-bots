from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import http.cookiejar
import json
import urllib.request, urllib.error, urllib.parse

def get_soup(url,header):
    #return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),
    # 'html.parser')
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url,headers=header)),
        'html.parser')

def get_image_links(query) :
    
    query= query.split()
    query='+'.join(query)
    url="http://www.bing.com/images/search?q=" + query + "&FORM=HDRSC2"

    
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)

    ActualImages=[]# contains the link for Large original images, type of  image
    image_name_list=[]
    for a in soup.find_all("a",{"class":"iusc"}):
      
        mad = json.loads(a["mad"])
        turl = mad["turl"]
        m = json.loads(a["m"])
        murl = m["murl"]

        image_name = urllib.parse.urlsplit(murl).path.split("/")[-1]
       # image_name_list.append(image_name)

        ActualImages.append((image_name, turl, murl))

    print("there are total" , len(ActualImages),"images")




    pics_list=[]
    for i, (image_name, turl, murl) in enumerate(ActualImages):
        
        pics_list.append(turl)
    return pics_list
    #print(pics_list)
