from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import json
products = json.load(open("products.json"))
def lcscscraper(url,span,fronttext):
    now = datetime.now()
    current_time = now.time()
    current_date = now.date()
    result=requests.get(url)
    spannum = span
    doc=BeautifulSoup(result.text,"html.parser")
    tag = doc.find_all("span")[spannum]
    print(fronttext+" "+str(current_date)+" "+str(current_time)+" "+tag.string)
    with open(fronttext+".txt",'a') as f:
        f.write(fronttext+" "+str(current_date)+" "+str(current_time)+" "+tag.string+'\n')


def autoscrapper():
    while True:
        for i in products:
          lcscscraper(i["url"], i["span"], i["fronttext"])
        time.sleep(120)

autoscrapper()






