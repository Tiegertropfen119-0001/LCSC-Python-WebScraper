from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
import json
import os
import pandas as pd
import config

products = json.load(open("products.json"))

# creates folder if not exists
isExist = os.path.exists(config.fileLocation)
if not isExist:
    os.makedirs(config.fileLocation)

def lcscscraper(url, span, fronttext):
    now = datetime.now()
    current_time = now.time()
    current_date = now.date()
    result = requests.get(url)
    spannum = span

    doc = BeautifulSoup(result.text, "html.parser")
    tag = doc.find_all("span")[spannum]
    price = tag.string

    # create or load the Excel file
    filename = config.fileLocation + fronttext + ".xlsx"
    if os.path.isfile(filename):
        df = pd.read_excel(filename)
    else:
        df = pd.DataFrame(columns=['datetime', ' ' , ' ' ,'price'])

    # add new row to the Excel file
    new_row = {'datetime': str(current_date) + " " + str(current_time), 'price': price}
    df = df.append(new_row, ignore_index=True)

    # save the Excel file
    writer = pd.ExcelWriter(filename, engine='openpyxl', mode='w')
    df.to_excel(writer, index=False)
    writer.save()
    writer.close()

    print(fronttext+" "+str(current_date)+" "+str(current_time)+" "+price)


def autoscrapper():
    while True:
        for i in products:
            lcscscraper(i["url"], i["span"], i["fronttext"])
        time.sleep(config.delayBetweenPriceCheck)

if __name__ == '__main__':
    autoscrapper()
