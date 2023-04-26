import requests
import json
from bs4 import BeautifulSoup
import sys
import os

result_location_arg = sys.argv[1]

url = "https://www.tb.no/"
source = "TB"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = []

url_base = "https://tb.no"
for article in soup.find_all('article'):
    anchor = article.find("a")
    url = anchor.get("href")
    if url.startswith("/"):
        url = url_base + url

    title = anchor.find("h2").text

    paywallContainer = anchor.find(
        "svg", class_=lambda c: c and "premium-logo" in c.split())
    paywall = False
    if paywallContainer is not None:
        paywall = True

    articles.append({"title": title, "url": url, "previewUrl": "",
                    "paywall": paywall, "source": source})

json_object = json.dumps(articles, indent=4)

with open(os.path.join(result_location_arg, "results-tb.json"), "w") as outfile:
    outfile.write(json_object)
