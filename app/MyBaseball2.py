from bs4 import BeautifulSoup
import requests


bb_page = "https://www.espn.com/mlb/standings"
response = requests.get(bb_page)

bb_soup = BeautifulSoup(response.content, 'html.parser')

x = bb_soup.text

b = x.find('"groups":[{"name":"American League","children":')
e = x.find('"requestedDates":{"season":2018,"seasontype":2}')
d = x[b:e]

al, nl, dummy = d.split('}]}]},')

print(nl)
