import os

def Cls():
    os.system("cls")
Cls()

import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"   #ლინკი

response = requests.get(url)    # საიტზე რექვესთის გაგზავნა
# print(response.text)    # აუბრუნებს საიტის მთლიან html კოდს
# f = open("htmlCode.txt", "w", encoding="utf-8")
# f.write(response.text)
# f.close()


soup = BeautifulSoup(response.text, "lxml")
# f = open("htmlCode.txt", "w", encoding="utf-8")
# f.write(str(soup))
# f.close()


data = soup.find("div", class_="col-lg-4 col-md-6 mb-4")     #soup-ში ეძებს ყველა div elements
# f = open("data.txt", "w", encoding="utf-8")
# f.write(str(data))
# f.close()


name = data.find("h4", class_="card-title").text
print(name)