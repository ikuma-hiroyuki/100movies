import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
request = requests.get(url=URL)
request.raise_for_status()
empire_html = request.text

soup = BeautifulSoup(empire_html, "html.parser")
titles = [title.text for title in soup.find_all(name="h3", class_="title")]

data = pd.DataFrame(titles[::-1])
data.to_csv("movies.txt", index=False, header=False)
