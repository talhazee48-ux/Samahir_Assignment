# Web Scraping - Quotes and Authors

import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

data = []

quotes = soup.select("div.quote")

for item in quotes:

    text = item.select_one("span.text")
    author = item.select_one("small.author")

    tags = item.select("a.tag")

    if text and author:

        tag_list = []

        for tag in tags:
            tag_list.append(tag.get_text(strip=True))

        data.append({
            "quote": text.get_text(strip=True),
            "author": author.get_text(strip=True),
            "tags": ", ".join(tag_list)
        })

with open("quotes_dataset.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["quote", "author", "tags"]
    )

    writer.writeheader()
    writer.writerows(data)

print("Quotes collected:", len(data))

for row in data[:10]:
    print(row)