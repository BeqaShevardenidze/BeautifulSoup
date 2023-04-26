def f_mymarket():
    import os

    def Cls():
        os.system("cls")
    Cls()


    import requests
    from bs4 import BeautifulSoup

    url = "https://www.mymarket.ge/ka/search/69/teqnika/mobiluri-kavshirgabmuloba/mobiluri-telefoni/?Brands=90&CatID=69&Page=1&SortID=4"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find("div").text

    # for i in range(len(data)):
        # product = data.find("a", class_="h100")

if __name__ == "__main__":
    f_mymarket()