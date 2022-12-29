from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time
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
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY85-20PU_C965497.html",35,"Attiny-85")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY13A-PU_C94341.html",35,"Attiny-13")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY84A-PU_C145560.html",35,"Attiny-84")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATMEGA328-PU_C613508.html",35,"ATMEGA328")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY44A-PU_C1337333.html",35,"ATTINY44A-PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY88-PU_C613519.html",35,"ATTINY88-PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY861A-PU_C147903.html",35,"ATTINY861A-PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY261A-PU_C144317.html",35,"ATTINY261A-PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATTINY2313A-PU_C112165.html",35,"ATTINY2313A-PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATMEGA8535L-8PU_C185629.html",35,"ATMEGA8535L-8PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATMEGA16A-PU_C30504.html",35,"ATMEGA16A-PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATMEGA644P-20PU_C5127752.html",35,"ATMEGA644P-20PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATMEGA8-16PU_C112958.html",35,"ATMEGA8-16PU")
        lcscscraper("https://www.lcsc.com/product-detail/Microcontroller-Units-MCUs-MPUs-SOCs_Microchip-Tech-ATMEGA88PA-PU_C28443.html",35,"ATMEGA88PA-PU")
        time.sleep(120)


autoscrapper()  






