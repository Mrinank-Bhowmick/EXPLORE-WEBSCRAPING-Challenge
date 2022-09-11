import requests
from bs4 import BeautifulSoup

# Get the html from the BBC website
url = "https://www.bbc.com/news"
r = requests.get(url)
html = r.text

soup = BeautifulSoup(html, "html.parser")

news = soup.find_all("a", class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor")

for n in news:
    print("Title: "+n.text)
    print("Link: "+"https://www.bbc.com" + n["href"])
    print()
