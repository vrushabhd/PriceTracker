import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/Test-Exclusive-668/dp/B07HGH88GL/ref=lp_4363159031_1_5?s=electronics&ie=UTF8&qid=1591192831&sr=1-5"
# shoping website link here
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}


def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()[
        1:].strip().replace(',', '')
    # print(price.strip())
    converted_price = float(price[0:5])
    print(converted_price)
    print(title.strip())
    # print(converted_price)

    if(converted_price < 14000):  # add price you  want to track

        send_mail()# sending mail


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("", "")  # your email and password respectively.
    subject = "Price fell Down!"
    body = "cehck the amzon link " + URL
    msg = f"Subject:{subject}\n\n{body }"
    server.sendmail("", "", msg)  # Receiver and sender email respectively.
    print("HEY EMAIL HAS BEEN SENT")
    server.quit()


while(True):

    check_price()
    time.sleep(60)  # mention the time after which it will start executing.
