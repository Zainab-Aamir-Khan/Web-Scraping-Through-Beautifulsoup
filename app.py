from bs4 import BeautifulSoup
import requests

response = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(response.content, 'lxml')
books = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
for book in books:
    bookName = books.h3.a['title']
    print(bookName)




