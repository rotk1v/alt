import requests
import json
from bs4 import BeautifulSoup
import sys
import os

result_location_arg = sys.argv[1]

url = "https://www.vg.no/"
source = "VG"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = []

for article in soup.find_all('article', {'class': "article"}):
    articleInfo = article.find("div", {"class": "article-container"})
    container = articleInfo.find("a")
    url = container.get("href").split('?')[0]
    headlineContainer = container.find_all(
        "span", {"class": "d-block"})

    title = ' '.join(span.text.strip().replace("\xa0", " ")
                     for span in headlineContainer).strip()

    imageContainer = articleInfo.find("img", {"class": "article-image"})
    imageUrl = ""

    if imageContainer != None and imageContainer.has_attr("src"):
        imageUrl = imageContainer.get("src")

    if len(title) > 0:
        articles.append({"title": title, "url": url, "previewUrl": imageUrl,
                        "paywall": False, "source": source})


json_object = json.dumps(articles, indent=4)

with open(os.path.join(result_location_arg, "results-vg.json"), "w") as outfile:
    outfile.write(json_object)
