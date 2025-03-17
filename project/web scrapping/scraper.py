import requests
from bs4 import BeautifulSoup
URL = "http://books.toscrape.com/"
def scrape_books():
    response = requests.get(URL)
    if requests.status_codes == 200:
        print("Failed to retrieve the webpage")
        return
    soup = BeautifulSoup(response.text,"html.parser")
    books = soup.find_all("article",class_="product_pod")
    data = []
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p",class_="price_color").text
        data.append([title,price])
        return data
    




