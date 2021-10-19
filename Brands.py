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

# coding: utf-8

link1 = "https://www.gsmarena.com/makers.php3"
def maksoup(url):#extract the table of Mobiles finders
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_data(soup):
    list = []
    get_table = soup.find('table')
    list_data = get_table.find_all('td')
    for item in list_data:
        try :
            data = {}
            txt = item.find('a').text
            reject = item.find('span').text
            data['Brand'] = txt.replace(reject , "")
            data['link'] = item.find('a').attrs["href"]
            list.append(data)
        except :
            pass
    
    return list
Mysoup = maksoup(link1)
data = get_data(Mysoup)
print(data)
pandas.DataFrame(data).to_csv("Brands.csv")


print(get_data(maksoup(link1)))