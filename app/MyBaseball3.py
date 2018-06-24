from bs4 import BeautifulSoup
import requests
import pdb
import json

request_url = "https://www.espn.com/mlb/standings"
response = requests.get(request_url)

soup = BeautifulSoup(response.content, 'html.parser')

team_id = 0
teams = []
names_tables = soup.find_all("table", "Table2__right-aligned Table2__table-fixed Table2__Table--fixed--left Table2__table")
for table in names_tables:
    cells = table.find_all("td")
    for cell in cells:
        spans = cell.find_all("span")
        try:
            team_name = spans[1].text
            team_abbrev = spans[2].text
            team_id += 1
            team = {"id" : team_id, "abbrev": team_name, "name": team_abbrev}
            teams.append(team)
        except IndexError as e:
            print("UNRECOGNIZED TEAMS DATA:", cell.text) #> "East" ... "Central" ... "West"

for team in teams:
    print(team)

stat_id = 0
stats = []
labels = ['W', 'L', 'PCT', 'GB', 'HOME', 'AWAY', 'RS', 'RA', 'DIFF', 'STRK', 'L10']
stats_tables = soup.find_all("table", "Table2__table-scroller Table2__right-aligned Table2__table")
for table in stats_tables:
    rows = table.find_all("tr", "Table2__tr")
    for row in rows:
        cells = row.find_all("td")
        # maybe lets start with these as a list. how about a list comprehension?
        # otherwise, and perhaps ideally, you could always convert to a dictionary
        # with keys like: "wins", "losses", "win_pct", etc.
        # and individually assign each stat to the proper attribute
        #stat_values = [cell.text for cell in cells] #> ['W', 'L', 'PCT', 'GB', 'HOME', 'AWAY', 'RS', 'RA', 'DIFF', 'STRK', 'L10']
        stat_values = []
        ctr = 0
        listdata = {}
        for cell in cells:
            if cell.text not in labels:
                if ctr != 0:
                    listdata.update({labels[ctr-1] : cell.text})
                else:
                    listdata.update({"id" : stat_id + 1})
                    stat_id += 1
            ctr += 1
        if len(listdata) != 0:
            stats.append(listdata)

for stat in stats:
    print(stat)

# todo: combine the teams list with the stats list
# ... assuming they are in the same order (which should absolutely be verified)
# ... then you can finally work with the rankings data
