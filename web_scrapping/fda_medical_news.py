# Web Scraping - FDA Medical Device News

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.fda.gov/medical-devices/medical-devices-news-and-events/cdrh-new-news-and-updates"

response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

data = []

for heading in soup.find_all(["h2", "h3"]):

    title = heading.get_text(" ", strip=True)

    if len(title) < 10:
        continue

    link = heading.find("a")

    if link:
        href = link.get("href")

        if href and href.startswith("/"):
            href = "https://www.fda.gov" + href

        data.append({
            "title": title,
            "url": href
        })

data = data[:50]

with open("fda_medical_news.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["title", "url"]
    )

    writer.writeheader()
    writer.writerows(data)

print("FDA records:", len(data))

for row in data[:10]:
    print(row["title"])