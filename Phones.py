from typing import get_args
import requests
import urllib.request
import time
import pandas as pd
import pandas
from bs4 import BeautifulSoup
import json
import csv
import os
import re
from ToNum import To_Date, To_Num, To_Storage

# coding: utf-8

link1 = "https://www.gsmarena.com/"
list = []
def maksoup(url):#extract the table of Mobiles finders
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup
def Brand_list():#return list of all brands in Brands.csv
    Brand_links = pandas.read_csv("Brands.csv",header=0).to_dict()
    list=[]
    for item in Brand_links.get('link'):
        G = Brand_links['link'][item]
        list.append(link1+G)
    return list
def phone_list(Plink):#return list of Phones of any brand_url
    soup = maksoup(Plink)
    content = soup.find('div' ,class_='makers')
    list = content.find_all('a')
    phones = []
    for item in list:
        try :
            phone = item.attrs["href"]
            phones.append(phone)
        except :
            print ('Mession Field!! ')
    return phones
phone_list('https://www.gsmarena.com/xiaomi-phones-80.php')
def get_data(soup):
    Row = {}
    try:
        content = soup.find('div' ,class_='center-stage')
        try:
            header = soup.find('div',class_='article-info-line page-specs light border-bottom')
            model =header.find('h1',{'class':'specs-phone-name-title'})# Model-hl
            Row['model']=model.string
                
        except:
            Row['model']='None'


        try:#light pattern help help-popularity#span inside
        #print(content)
            released = content.find('span',{'data-spec':'released-hl'})
            Row['relased'] = released.string.replace('Released ','')
            print(released.string)
            #released-hl
            
        except:
            Row['relased'] = 'None'

        try:
            body =content.find('span',{'data-spec':'body-hl'})# body-hl
            Row['body']=body.string
                
        except:
            Row['body']='None'

        try:
            os = content.find('span',{'data-spec':'os-hl'})# os-hl
            Row['os']=os.string
                    
        except:
            Row['os']='None'

        try:
            storage = content.find('span',{'data-spec':'storage-hl'})# storage-hl
            Row['storage'] = To_Storage(storage.string)           
        except:
            Row['storage'] = 'None'

        try:
            displaysize = content.find('span',{'data-spec':'displaysize-hl'})# displaysize-hl
            Row['displaysize']=To_Num(displaysize.string)                
        except:
            Row['displaysize']='None'

        try:
            desplayres = content.find('div',{'data-spec':'displayres-hl'})# displayres-hl
            Row['desplayres'] =To_Storage(desplayres.string)                    
        except:
            Row['desplayres'] ='None'

        try:
            camera = content.find('span',{'data-spec':'camerapixels-hl'})# camerapixels-hl
            Row['camera'] = camera.string                        
        except:
            Row['camera'] = 'None'

        try:
            video = content.find('div',{'data-spec':'videopixels-hl'})# videopixels-hl
            Row['video'] = To_Num(video.string)
        except:
            Row['video'] = 'None'

        try:
            ram = content.find('span',{'data-spec':'ramsize-hl'})# ramsize-hl
            Row['ram'] = ram.string                                    
        except:
            Row['ram'] = 'None'

        try:
            chipset = content.find('div',{'data-spec':'chipset-hl'})# chipset-hl
            Row['chipset'] = chipset.string
        except:
            Row['chipset'] = 'None'

        try:
            battery = content.find('span',{'data-spec':'batsize-hl'})# batsize-hl
            Row['battery'] = battery.string
        except:
            Row['battery'] = 'None'

        try:
            batterysize = content.find('div',{'data-spec':'battype-hl'})# battype-hl
            Row['batterysize'] = batterysize.string
        except:
            Row['batterysize'] = 'None'
        try:
            divphoto = content.find('div',class_='specs-photo-main')# main photo
            photo = divphoto.find('img').get('src')
            Row['photo'] = photo
        except:
            Row['photo'] = 'None'
        try:
            li_peoplelation = content.find('li',class_='light pattern help help-popularity')# main photo
            hits = li_peoplelation.find('span').string
            Row['hits'] = To_Num(hits)
        except:
            Row['hits'] = 'None'
    except:
        pass#return released
    list.append(Row)
    DF= pd.DataFrame(list)
