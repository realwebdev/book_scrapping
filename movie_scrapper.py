import requests
from bs4 import BeautifulSoup

for i in range(0, 12, 1):
    URL = "https://reelgood.com/movies/source/netflix?offset=" + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    f = open("movies_netflix.txt", "w")
    for link in soup.select('[itemprop=itemListElement] [itemprop=url]'):
        data = link.get('content')
        f.write(data)
        f.write("\n")
