import os

def Cls():
    os.system("cls")
Cls()


import requests
from bs4 import BeautifulSoup

url = "https://jobs.ge/?page=1&q=&cid=6&lid=&jid="
# url = "https://jobs.ge/ge/ads/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# data = soup.find_all("div", class_="regularEntries")

result = open("result.txt", "w", encoding="utf-8")
result.close()

#მუშაობს პოზიცია
name = soup.find_all("a", class_="vip")
for i in range(len(name)):
    print(str(name[i]))
    result = open("result.txt", "a", encoding="utf-8")
    result.write("პოზიცია = " + str(name[i].text) + "\n")
    result.write("ლინკი = " + "https://jobs.ge" + str(name[i].get("href")) + "\n")

    url_2 = "https://jobs.ge" + str(name[i].get("href"))
    response_2 = requests.get(url_2)
    soup_2 = BeautifulSoup(response_2.text, "lxml")
    recrutor = soup_2.find_all("td", class_="dtitle")
    recrutor_span = recrutor[1].find("span").text
    recrutor_a_b = recrutor[1].find("b").text.replace("\n","")
    result.write(str(recrutor_span + recrutor_a_b.replace("	"," ") + ("\n"*2)))

    result.close()