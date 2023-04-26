def f_zoomer():
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


    #დათა ///////////////////////////////////////////////////////
    # data = soup.find("div", class_="lg_3 lp_3 md_4 sm_6 xs_6 product_item")         #soup-ში ეძებს ყველა div elements
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

    # product_link = data.find("a", class_="product_link").get("href")    #get მეთოდით მივიღეთ href პარამეტრის მნიშვნელობა
    # result = open("result.txt", "w", encoding="utf-8")
    # result.write("პროდუქტის ლინკი = " + "https://zoommer.ge/"+product_link)
    # result.close()



    # ციკლის გარშე/////////////////////////////////////////////////////
    # result = open("result.txt", "w", encoding="utf-8")
    # name = data.find("h4").text
    # frice = data.find(class_="product_new_price").text
    # product_link = data.find("a", class_="product_link").get("href")

    # result.write("სახელი = " + name + "\n")
    # result.write("ფასი = " + frice + "\n")
    # result.write("პროდუქტის ლინკი = " + "https://zoommer.ge/"+product_link + "\n")
    # result.close()




    num = 0

    data = soup.find_all("div", class_="lg_3 lp_3 md_4 sm_6 xs_6 product_item")

    result = open("result.txt", "w", encoding="utf-8")
    result.close()      #შლის წინა კონტენტს

    for i in data:
        result = open("result.txt", "a", encoding="utf-8")

        name = i.find("h4").text
        frice = i.find(class_="product_new_price").text
        product_link = i.find("a", class_="product_link").get("href")
        if product_link != "":
            num += 1
        print(name + "\n" + frice + "\n" + product_link + "\n")

        result.write("პროდუქტი 1" + str(num) + "\n")
        result.write("სახელი = " + name + "\n")
        result.write("ფასი = " + frice + "\n")
        result.write("პროდუქტის ლინკი = " + "https://zoommer.ge/"+product_link + "\n" + "\n")


    result.close()




if __name__ == "__main__":
    f_zoomer()