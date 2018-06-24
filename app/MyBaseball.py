from bs4 import BeautifulSoup
import requests
#import json


bb_page = "https://www.espn.com/mlb/standings"
response = requests.get(bb_page)

bb_soup = BeautifulSoup(response.content, 'html.parser')
#name_box = bb_soup.find('span', attrs={'class': 'Nav__Text flex-expand clr-gray-04 n8 pl3'})
#name = name_box.text.strip()
#print(name)
#name_box = bb_soup.find("groups")
#name_box = bb_soup.find('span', attrs={'class': 'Nav__Text flex-expand clr-gray-04 n8 pl3'})
#name = name_box.text.strip()
#print("here", name_box)

#response_body = json.loads(bb_soup.text)

#x = bb_soup.find("boot")
x = bb_soup.text

if '"groups":[{"name":"American League","children":' in x: 
    print("Yes")
print(x.find('"groups":[{"name":"American League","children":'))
print(x.find('"requestedDates":{"season":2018,"seasontype":2}'))
b = x.find('"groups":[{"name":"American League","children":')
e = x.find('"requestedDates":{"season":2018,"seasontype":2}')
print(x[b:e])
#print(x[98637:113117])

#import urllib3
#bb_http = urllib3.PoolManager()
#bb_req = bb_http.request('GET', bb_page)
#print(bb_req.status)
#bb_soup = BeautifulSoup(bb_req, 'html.parser')
#print(response_body)
