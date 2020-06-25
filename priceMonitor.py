# -*- coding: utf-8 -*-
"""
Created on Thursday 25 June 2020 21:45:33

@author: Sk_Saddy
"""

import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup
import smtplib
import time

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input("URL - ")
url = 'https://www.flipkart.com/canon-eos-3000d-dslr-camera-single-kit-18-55-lens-16-gb-memory-card-carry-case/p/itmf3dhjyznuhayu?pid=CAMF3DHJURPEMNRN&lid=LSTCAMF3DHJURPEMNRNYD4BKP&fm=neo%2Fmerchandising&iid=M_058270cd-5294-4d1a-85a4-80b2bb5999c4_3.IGIE9IAM3GJO&ssid=c3lj1z1rts0000001593071160741&otracker=hp_omu_Top%2BOffers_3_3.dealCard.OMU_Top%2BOffers_IGIE9IAM3GJO_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_3_NA_view-all_3&cid=IGIE9IAM3GJO'


def check_price():
    # Retrieve html code
    html = urllib.request.urlopen(url, context=ctx).read()

    # Beautified format
    soup = BeautifulSoup(html, 'html.parser')

    #   retrieving price
    price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text()
    conv_price = price[1:7].replace(',', '')
    conv_price = int(conv_price)
    print('Price:\n', conv_price)

    if conv_price < "EXPECTED PRICE":
        send_mail()
        return True


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()   # encrypts the connection
    server.ehlo()

    server.login('SENDER-EMAIL-ID', 'SENDER-PASSWORD')

    subject = 'Price dropped !'
    body = """
        go check your item, click on the flipkart link 
        https://www.flipkart.com/canon-eos-3000d-dslr-camera-single-kit-18-55-lens-16-gb-memory-card-carry-case/p/itmf3dhjyznuhayu?pid=CAMF3DHJURPEMNRN&lid=LSTCAMF3DHJURPEMNRNYD4BKP&fm=neo%2Fmerchandising&iid=M_058270cd-5294-4d1a-85a4-80b2bb5999c4_3.IGIE9IAM3GJO&ssid=c3lj1z1rts0000001593071160741&otracker=hp_omu_Top%2BOffers_3_3.dealCard.OMU_Top%2BOffers_IGIE9IAM3GJO_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_3_NA_view-all_3&cid=IGIE9IAM3GJO
    """
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'SENDER-EMAIL-ID',
        'RECEIVER-EMAIL-ID',
        msg
    )
    print("Email has been sent!")

    server.quit()


while True:
    print("checking...")
    check = check_price()
    if check:
        break
    time.sleep(60*60*3)

