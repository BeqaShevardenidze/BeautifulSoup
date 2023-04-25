import os

def Cls():
    os.system("cls")
Cls()

import requests
from bs4 import BeautifulSoup

# url = "https://zoommer.ge/mobilurebi-2"
url = "https://zoommer.ge/mobilurebi-2?orderby=11"
response = requests.get(url)
# print(response.text)
# f = open("response.txt", "w", encoding="utf-8")
# f.write(response.text)
# f.close()


soup = BeautifulSoup(response.text, "lxml")
# f = open("soup.txt", "w", encoding="utf-8")
# f.write(str(soup))
# f.close()


data = soup.find("div", class_="lg_3 lp_3 md_4 sm_6 xs_6 product_item")         #soup-ში ეძებს ყველა div elements
# f = open("data.txt", "w", encoding="utf-8")
# f.write(str(data))
# f.close()

# name = data.find("h4").text
# result = open("result.txt", "w", encoding="utf-8")
# result.write("სახელი = " + name + "\n")
# result.close()

# frice = data.find(class_="product_new_price").text
# result = open("result.txt", "a", encoding="utf-8")
# result.write("ფასი = " + frice)
# result.close()

product_link = data.find(class_="product_top_div", href="")
print(product_link)