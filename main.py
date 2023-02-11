from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import json
import os
import config


products = json.load(open("products.json"))


def lcscscraper(url,span,fronttext):
    now = datetime.now()
    current_time = now.time()
    current_date = now.date()
    result=requests.get(url)
    spannum = span

    #creates folder if not exists
    isExist = os.path.exists(config.fileLocation)
    if not isExist:
        os.makedirs(config.fileLocation)

    doc=BeautifulSoup(result.text,"html.parser")
    tag = doc.find_all("span")[spannum]
    print(fronttext+" "+str(current_date)+" "+str(current_time)+" "+tag.string)
    with open(config.fileLocation + fronttext + ".txt",'a') as f:
        f.write(config.fileLocation + fronttext + " " + str(current_date) + " " + str(current_time) + " " + tag.string + '\n')


def autoscrapper():
    while True:
        #takes the products from the products.json
        for i in products:
          lcscscraper(i["url"], i["span"], i["fronttext"])
        time.sleep(config.delayBetweenPriceCheck)

autoscrapper()






