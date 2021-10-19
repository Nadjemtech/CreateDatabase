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


def get_page(link,page):
    last = link.split('-')[-1]
    num = re.findall(r'[0-9]', last)
    numF=''
    for i in num: 
        numF+=i

    link = link.replace(last,f'f-{numF}-0-p')
    final = link+str(page)+'.php'
    return final


link1 = "https://www.gsmarena.com/"
list = []
def maksoup(url):#extract the table of Mobiles finders
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def phone_list(Plink):#return list of Phones of any brand_url
    phones = []
    for i in range(16):
        try:
            pagelink = get_page(Plink , i+1)
            print(pagelink)
            soup = maksoup(pagelink)
            content = soup.find('div' ,class_='makers')
            list = content.find_all('a')

            for item in list:
                try :
                    phone = item.attrs["href"]
                    phones.append(phone)
                except :
                    print ('Mession Field!! ')
        except:
            break
    return phones

print(phone_list('https://www.gsmarena.com/samsung-phones-9.php'))