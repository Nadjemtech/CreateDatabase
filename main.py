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
    phones = []
    for i in range(16):
        
        soup = maksoup(Plink)
        content = soup.find('div' ,class_='makers')
        print('--------------------------------------')
        print(content)
        print('--------------------------------------')
        list = content.find_all('a')
    
        for item in list:
            try :
                phone = item.attrs["href"]
                phones.append(phone)
            except :
                print ('Mession Field!! ')
    return phones


L= Brand_list()#all Brands links
P= []# all phones links
for list in L :
    P = P+phone_list(str(list))

print(P)