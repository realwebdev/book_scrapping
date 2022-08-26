import json
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"usr/local/bin"
#
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# Selenium accesses the Chrome browser driver in incognito mode and without actually opening a browser window(
# headless argument).
driver = webdriver.Chrome()

driver.get("https://www.goodreads.com/book/popular_by_date")
a = 0

while a < 100:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        load_more_link = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div[1]/div[3]/div/div/button')
    except:
        print("no more books are present")
        break

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)
    # while 1:
    load_more_link.click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("coming out of the loop")
# time.sleep(5)

# def webscrapper():
book_data = {}
book_file = {}

# global book_file, title, author
# url = "https://www.goodreads.com/book/popular_by_date"
# page = requests.get(url).text
page_source = driver.page_source
doc = BeautifulSoup(page_source, "lxml")
# doc.fin
# isbn
all_doc = doc.find_all('article', {'class': 'BookListItem'})
# print(all_doc)
# for i in page:
for search in all_doc:
    title = search.find_all('h3', {"class": "Text Text__title3 Text__umber"})
    for book_content in title:
        book_content.find()
    rank = search.find('h2', {"class": "Text Text__h2 Text__italic Text__subdued"}).text

    author = search.find('div', {"class": "BookListItem__authors"}).text
    description = search.find('span', {
        "class": "Formatted"}).text

    ratings_value = search.find('span', {'class': 'AverageRating__ratingValue'}).text
    ratings_counts = search.find('div', {'class': 'AverageRating__ratingsCount'}).text
    # genre
    # url
    # description = doc.find('h3', {"class": "Text Text__title3 Text__umber"}).text
    # ratings = doc.find('h3', {"class": "Text Text__title3 Text__umber"}).text
    # rank = {"ranking":}
    book_data = {"rank": rank, "Title": title, "Author": author, "Description": description,
                 "Ratings": {"Rating Count": ratings_counts, "Rating Score": ratings_value}}
    # book_file1 = {'hello': 'haseeb'}
    # print(book_file[count + 1])
    print("Title:\t ", title)
    print("Author:\t ", author)
    print("Description:\t ", description)
    print("Rating Value:\t ", ratings_value)
    print("Rating Counts:\t ", ratings_counts, "\n")
    book_file[rank] = book_data

    with open("goodreads_data.json", 'a', encoding='utf-8') as out_file:
        json.dump(book_file, out_file, ensure_ascii=False, indent=4)

        #
        # webscrapper()
