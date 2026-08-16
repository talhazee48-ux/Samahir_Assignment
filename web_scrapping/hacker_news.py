# Web Scraping - Hacker News

import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/"

response = requests.get(url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

data = []

rows = soup.select("tr.athing")

for row in rows:

    title_tag = row.select_one("span.titleline a")

    if title_tag:
        title = title_tag.get_text(strip=True)
        link = title_tag.get("href")

        score_row = row.find_next_sibling("tr")
        score_tag = score_row.select_one("span.score") if score_row else None

        score = score_tag.get_text(strip=True) if score_tag else "0"

        data.append({
            "title": title,
            "url": link,
            "score": score
        })

with open("hacker_news.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["title", "url", "score"]
    )

    writer.writeheader()
    writer.writerows(data)

print("Stories collected:", len(data))

for row in data[:10]:
    print(row)