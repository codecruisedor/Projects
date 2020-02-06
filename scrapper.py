import requests
from bs4 import BeautifulSoup
import smtplib
import re
import time

#checks the price and sends an email if the price goes down....

def check_price():
    URL = 'https://www.amazon.in/dp/B01IBM5V66/ref=psdc_1375425031_t2_B07436JM87'

    headers = {"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    price = re.sub('[!₹@#$,]', '', price)

    print(float(price))
    if float(price) > 8000:
        send_mail()




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nnisarg55@gmail.com', 'xudmnyablvcltbxx')
    subject = 'Price fell down!!'
    body = 'Check this link: https://www.amazon.in/dp/B01IBM5V66/ref=psdc_1375425031_t2_B07436JM87 '
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'nnisarg55@gmail.com',
        'nnisarg55@gmail.com',
        msg
    )
    print('Email has been sent!!!!!')
    server.quit()


while(True):
    check_price()
    time.sleep(86400)





