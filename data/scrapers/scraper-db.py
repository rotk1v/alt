import requests
import json
from bs4 import BeautifulSoup
import sys
import os

result_location_arg = sys.argv[1]

url = "https://www.dagbladet.no/"
source = "Dagbladet"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = []

for article in soup.find_all('article'):
    url = article.find("a").get("href")
    header = article.find("h3", {"class": "headline"})

    titleArr = []
    for elem in header:
        titleArr.append(elem.text.strip())
    title = " ".join(titleArr)

    articles.append({"title": title, "url": url, "previewUrl": "",
                    "paywall": False, "source": source})

json_object = json.dumps(articles, indent=4)

with open(os.path.join(result_location_arg, "results-db.json"), "w") as outfile:
    outfile.write(json_object)
