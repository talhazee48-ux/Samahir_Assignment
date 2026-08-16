# Web Scraping - AI Weekly

import requests
from bs4 import BeautifulSoup
import csv

url = "https://aiweekly.co/ai-news-today"

response = requests.get(url, timeout=15)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

data = []

for item in soup.find_all(["h2", "h3"]):
    title = item.get_text(" ", strip=True)

    if len(title) > 15:
        link = item.find("a")

        if link and link.get("href"):
            href = link.get("href")

            if href.startswith("/"):
                href = "https://aiweekly.co" + href

            data.append({
                "title": title,
                "url": href
            })

data = data[:30]

with open("ai_news.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "url"])
    writer.writeheader()
    writer.writerows(data)

print("Articles collected:", len(data))

for row in data[:10]:
    print(row["title"])