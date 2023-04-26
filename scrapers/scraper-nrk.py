import requests
import json
from bs4 import BeautifulSoup
import sys
import os

result_location_arg = sys.argv[1]

url = "https://www.nrk.no/"
source = "NRK"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = []

for article in soup.select('div[data-ec-name]'):
    anchor = article.find("a")
    if anchor == None:
        continue
    url = anchor.get("href")

    titleContainer = anchor.select_one("span[role='text']")
    if titleContainer == None:
        continue
    title = ' '.join(titleContainer.text.split())

    articles.append({"title": title, "url": url, "previewUrl": "",
                    "paywall": False, "source": source})

json_object = json.dumps(articles, indent=4)

with open(os.path.join(result_location_arg,  "results-nrk.json"), "w") as outfile:
    outfile.write(json_object)
