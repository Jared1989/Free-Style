from bs4 import BeautifulSoup
import requests
import pdb
import json
from datetime import datetime
import itertools
import os
import csv

class team_opts:

    def __init__(self, team_abbrev, team_list, team_stats, team_ext_stats):
        self.team_abbrev = team_abbrev
        self.team_list = team_list
        self.team_stats = team_stats
        self.team_ext_stats = team_ext_stats

    def get_team_id(self):
        for tl in self.team_list:
            if tl['abbrev'] == self.team_abbrev:
                return tl['id']

    def get_team_name(self, num):
        return self.team_list[num - 1]['name']

    def get_team_stat(self, num, stat):
        return self.team_stats[num - 1][stat]

    def get_team_stat_range(self, num, home_away):
        result = self.team_stats[num - 1][home_away].split('-')
        return float(result[0]) / (float(result[0]) + float(result[1]))

    def get_team_stat_range_ext(self, num, day_night):
        result = self.team_ext_stats[num - 1][day_night].split('-')
        return float(result[0]) / (float(result[0]) + float(result[1]))

    def __del__(self):
        return True

def get_teams(request_url):

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
                team_abbrev = spans[1].text
                team_name = spans[2].text
                team_id += 1
                team = {"id" : team_id, "abbrev": team_abbrev, "name": team_name}
                teams.append(team)
            except IndexError as e:
                # Do nothing
                dummy = 0

    return teams

def get_stats(request_url, labels):

    response = requests.get(request_url, request_url)

    soup = BeautifulSoup(response.content, 'html.parser')

    stat_id = 0
    stats = []
    stats_tables = soup.find_all("table", "Table2__table-scroller Table2__right-aligned Table2__table")
    for table in stats_tables:
        rows = table.find_all("tr", "Table2__tr")
        for row in rows:
            cells = row.find_all("td")
            stat_values = []
            ctr = 0
            listdata = {}
            for cell in cells:
                if ctr == 0 and cell.text not in labels:
                    listdata.update({"id" : stat_id + 1})
                    stat_id += 1
                if cell.text not in labels:
                    listdata.update({labels[ctr] : cell.text})
                ctr += 1
            if len(listdata) != 0:
                stats.append(listdata)

    return stats

def write_products_to_file(filename="teams.csv", teams=[]):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(teams)} TEAMS")

    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['id', 'abbrev', 'name', 'W', 'L', 'PCT', 'GB', 'HOME', 'AWAY', 'RS', 'RA', 'DIFF', 'STRK', 'L10', 'DAY', 'NIGHT', '1-RUN', 'XTRA', 'ExWL'])
        writer.writeheader() # uses fieldnames set above
        for t in teams:
            writer.writerow(t)

def merge_data(team_data, reg_data, ext_data):
    teams = []
    for (n, s, e) in zip(team_data, reg_data, ext_data):
        if n['id'] == s['id'] and n['id'] == e['id']:
            New_Value = {'id':n['id'], 'abbrev':n['abbrev'], 'name':n['name'], 'W':s['W'], 'L':s['L'], 'PCT':s['PCT'], 'GB':s['GB'], 'HOME':s['HOME'], 'AWAY':s['AWAY'], 'RS':s['RS'], 'RA':s['RA'], 'DIFF':s['DIFF'], 'STRK':s['STRK'], 'L10':s['L10'], 'DAY':e['DAY'], 'NIGHT':e['NIGHT'], '1-RUN':e['1-RUN'], 'XTRA':e['XTRA'], 'ExWL':e['ExWL']}
            teams.append(dict(New_Value))
            #print(n['id'], n['abbrev'], n['name'], s['W'], s['L'], s['PCT'], s['GB'], s['HOME'], s['AWAY'], s['RS'], s['RA'], s['DIFF'], s['STRK'], s['L10'], e['DAY'], e['NIGHT'], e['1-RUN'], e['XTRA'], e['ExWL'])
    #print(teams)
    write_products_to_file("teams.csv", teams)

def print_data(info):

    for item in info:
        print(item)

def print_team_list(info):

    print("")
    print("Abbreviation / Name")
    print("-------------------")
    print("")
    for item in info:
        print(item["abbrev"] + " : " +  item["name"])
    print("")

def search_team_abbrev(team_info, abbrev_validate):
    for tl in team_info:
        if tl['abbrev'] == abbrev_validate:
            return True
    return False

def get_team_abbrevs(team_info):

    team_vs = input("Please enter two team's abbreviations separated by commas (e.g. NYM, NYY), 'DONE' to quit, or 'HELP' for Team List: ")
    if ", " in team_vs:
        team_vs = team_vs.upper().split(", ")
    elif "," in team_vs:
        team_vs = team_vs.upper().split(",")
    elif " " in team_vs:
        team_vs = team_vs.upper().split(" ")
    else:
        team_vs = [team_vs.upper()]

    if team_vs[0].upper() == "DONE":
        return team_vs 

    if team_vs[0].upper() == "HELP":
        print_team_list(team_info) 
        return team_vs
    
    if len(team_vs) > 2:
        print("Only two teams can be compared at a time.")
        for ctr in range(len(team_vs) - 1, 1, -1):
            print("Removing ", team_vs[ctr])
            team_vs.pop(ctr)
    elif len(team_vs) == 1:
        tvs = input("Only one team entered " + team_vs[0] + ". Please enter a second team: ")
        team_vs.append(tvs.upper())

    spot = 0
    for tvs in team_vs:
        while not search_team_abbrev(team_info, tvs):
            tvs = input("Oh, invalid team abbreviation " + tvs + ". Expecting an abbreviation like 'NYM'. Please try again: ").upper()
            team_vs[spot] = tvs
        spot += 1

    while team_vs[0] == team_vs[1]:
        tvs = input("Oh, your two teams cannot be " + team_vs[1] + ". Please try again: ")
        while not search_team_abbrev(team_info, tvs):
            tvs = input("Oh, invalid team abbreviation " + tvs + ". Expecting an abbreviation like 'NYM'. Please try again: ").upper()
        team_vs[1] = tvs

    return team_vs

def get_home_away(team_abbrev):
    home_away = input("Is this a home game or away game for " +  team_abbrev + " (H/A)?: ").upper()
    while home_away not in "HA":
         print("Invalid entry. Please try again.")
         home_away = input("Is this a home game or away game for " +  team_abbrev + " (H/A)?: ").upper()
    return home_away

def get_day_night(team_abbrev):
    day_night = input("Is this a day game or night game for " +  team_abbrev + " (D/N)?: ").upper()
    while day_night not in "DN":
         print("Invalid entry. Please try again.")
         day_night = input("Is this a day game or night game for " +  team_abbrev + " (D/N)?: ").upper()
    return day_night

def location_time(value1, value2, item1a, item1b, item2a, item2b, Team1, Team2):
    #print(value1, value2, item1a, item1b, item2a, item2b, Team1, Team2)
    if value1 == value2:  
        #print("Here 1")  
        if item1a > item2b:
            #print("Here 1a")  
            result = Team1
        elif item1a < item2b:
            result = Team2
            #print("Here 1b")  
        else:
            result = "Tie"
            #print("Here 1c")  
    else:
        #print("Here 2")  
        if item1b > item2a:
            #print("Here 2a")  
            result = Team1
        elif item1b < item2a:
            result = Team2
            #print("Here 2b")  
        else:
            result = "Tie"
            #print("Here 2c")  
    return result

def print_results(team_data_1, team_id_1, team_data_2, team_id_2, home_away, day_night, file_value):

    Team1 = team_data_1.get_team_name(team_id_1)
    Team2 = team_data_2.get_team_name(team_id_2)
    Percent1 = float(team_data_1.get_team_stat(team_id_1, 'PCT'))
    Percent2 = float(team_data_2.get_team_stat(team_id_2, 'PCT'))
    RS1 = float(team_data_1.get_team_stat(team_id_1, 'RS'))
    RS2 = float(team_data_2.get_team_stat(team_id_2, 'RS'))
    RA1 = float(team_data_1.get_team_stat(team_id_1, 'RA'))
    RA2 = float(team_data_2.get_team_stat(team_id_2, 'RA'))
    DIFF1 = float(team_data_1.get_team_stat(team_id_1, 'DIFF'))
    DIFF2 = float(team_data_2.get_team_stat(team_id_2, 'DIFF'))
    Home1 = float(team_data_1.get_team_stat_range(team_id_1, 'HOME'))
    Home2 = float(team_data_2.get_team_stat_range(team_id_2, 'HOME'))
    Away1 = float(team_data_1.get_team_stat_range(team_id_1, 'AWAY'))
    Away2 = float(team_data_2.get_team_stat_range(team_id_2, 'AWAY'))
    L101 = float(team_data_1.get_team_stat_range(team_id_1, 'L10'))
    L102 = float(team_data_2.get_team_stat_range(team_id_2, 'L10'))
    STRK1 = team_data_1.get_team_stat(team_id_1, 'STRK')
    STRK2 = team_data_2.get_team_stat(team_id_2, 'STRK')
    Day1 = float(team_data_1.get_team_stat_range_ext(team_id_1, 'DAY'))
    Day2 = float(team_data_2.get_team_stat_range_ext(team_id_2, 'DAY'))
    Night1 = float(team_data_1.get_team_stat_range_ext(team_id_1, 'NIGHT'))
    Night2 = float(team_data_2.get_team_stat_range_ext(team_id_2, 'NIGHT'))

    HomeAway = location_time(home_away, "H", Home1, Away1, Home2, Away2, Team1, Team2)
    DayNight = location_time(day_night, "D", Day1, Night1, Night2, Day2, Team1, Team2)

    print("")
    print("-------------------------------------------------------------------------------------------")
    print("Teams:   ", Team1.center(20), " vs ", Team2.center(20), " ", "(" + day_night + ")")
    print("-------------------------------------------------------------------------------------------")
    print("RS:      ", '{0:.0f}'.format(RS1).center(20), " vs ", '{0:.0f}'.format(RS2).center(20))
    print("RA:      ", '{0:.0f}'.format(RA1).center(20), " vs ", '{0:.0f}'.format(RA2).center(20))
    print("DIFF:    ", '{0:.0f}'.format(DIFF1).center(20), " vs ", '{0:.0f}'.format(DIFF2).center(20))
    print("Percent: ", '{0:.3f}'.format(Percent1).center(20), " vs ", '{0:.3f}'.format(Percent2).center(20))
    print("Home:    ", '{0:.3f}'.format(Home1).center(20), " vs ", '{0:.3f}'.format(Home2).center(20))
    print("Away:    ", '{0:.3f}'.format(Away1).center(20), " vs ", '{0:.3f}'.format(Away2).center(20))
    print("L10:     ", '{0:.3f}'.format(L101).center(20), " vs ", '{0:.3f}'.format(L102).center(20))
    print("STRK:    ", STRK1.center(20), " vs ", STRK2.center(20))
    print("Day:     ", '{0:.3f}'.format(Day1).center(20), " vs ", '{0:.3f}'.format(Day2).center(20))
    print("Night:   ", '{0:.3f}'.format(Night1).center(20), " vs ", '{0:.3f}'.format(Night2).center(20))
    print("-------------------------------------------------------------------------------------------")
    print("Field:   ", HomeAway)
    print("Time:    ", DayNight)
    print("-------------------------------------------------------------------------------------------")
    print("")

    file_value.write("\r\n")
    file_value.write("-------------------------------------------------------------------------------------------" + "\r\n")
    file_value.write("Teams:   " + " " + Team1.center(20) + " " + " vs " + " " + Team2.center(20) + " " + "(" + day_night + ")" + "\r\n")
    file_value.write("-------------------------------------------------------------------------------------------" + "\r\n")
    file_value.write("RS:      " + " " + '{0:.0f}'.format(RS1).center(20) + " " + " vs " + " " + '{0:.0f}'.format(RS2).center(20) + "\r\n")
    file_value.write("RA:      " + " " + '{0:.0f}'.format(RA1).center(20) + " " + " vs " + " " + '{0:.0f}'.format(RA2).center(20) + "\r\n")
    file_value.write("DIFF:    " + " " + '{0:.0f}'.format(DIFF1).center(20) + " " + " vs " + " " + '{0:.0f}'.format(DIFF2).center(20) + "\r\n")
    file_value.write("Percent: " + " " + '{0:.3f}'.format(Percent1).center(20) + " " + " vs " + " " + '{0:.3f}'.format(Percent2).center(20) + "\r\n")
    file_value.write("Home:    " + " " + '{0:.3f}'.format(Home1).center(20) + " " + " vs " + " " + '{0:.3f}'.format(Home2).center(20) + "\r\n")
    file_value.write("Away:    " + " " + '{0:.3f}'.format(Away1).center(20) + " " + " vs " + " " + '{0:.3f}'.format(Away2).center(20) + "\r\n")
    file_value.write("L10:     " + " " + '{0:.3f}'.format(L101).center(20) + " " + " vs " + " " + '{0:.3f}'.format(L102).center(20) + "\r\n")
    file_value.write("STRK:    " + " " + STRK1.center(20) + " " + " vs " + " " + STRK2.center(20) + "\r\n")
    file_value.write("Day:     " + " " + '{0:.3f}'.format(Day1).center(20) + " " + " vs " + " " + '{0:.3f}'.format(Day2).center(20) + "\r\n")
    file_value.write("Night:   " + " " + '{0:.3f}'.format(Night1).center(20) + " " + " vs " + " " + '{0:.3f}'.format(Night2).center(20) + "\r\n")
    file_value.write("-------------------------------------------------------------------------------------------" + "\r\n")
    file_value.write("Field:   "+ " " + HomeAway + "\r\n")
    file_value.write("Time:    "+ " " + DayNight + "\r\n")
    file_value.write("-------------------------------------------------------------------------------------------" + "\r\n")
    file_value.write("\r\n")

def open_picks_file():
    filename=datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'-picks'+'.txt'
    file_value=open(filename,'w')
    return file_value

def close_picks_file(file_value):
    file_value.close()

def run():

    request_address = "https://www.espn.com/mlb/standings"
    team_data = []
    team_data = get_teams(request_address)
    #print_data(team_data)

    request_address = "https://www.espn.com/mlb/standings"
    headings = ['W', 'L', 'PCT', 'GB', 'HOME', 'AWAY', 'RS', 'RA', 'DIFF', 'STRK', 'L10']
    reg_data = []
    reg_data = get_stats(request_address, headings)
    #print_data(reg_data)

    request_address = "https://www.espn.com/mlb/standings/_/view/expanded"
    headings = ['W', 'L', 'PCT', 'GB', 'DAY', 'NIGHT', '1-RUN', 'XTRA', 'ExWL']
    ext_data = []
    ext_data = get_stats(request_address, headings)
    #print_data(ext_data)

    merge_data(team_data, reg_data, ext_data)

    fv = open_picks_file()

    team_abbrevs = []
    team_abbrevs = get_team_abbrevs(team_data)
    while team_abbrevs[0].upper() != "DONE":

        if team_abbrevs[0].upper() != "HELP":
            ha = get_home_away(team_abbrevs[0])
            dn = get_day_night(team_abbrevs[0])

            team_data_1 = team_opts(team_abbrevs[0], team_data, reg_data, ext_data)
            team_data_2 = team_opts(team_abbrevs[1], team_data, reg_data, ext_data)

            team_id_1 = team_data_1.get_team_id()
            team_id_2 = team_data_2.get_team_id()

            print_results(team_data_1, team_id_1, team_data_2, team_id_2, ha, dn, fv)

        team_abbrevs = get_team_abbrevs(team_data)

    close_picks_file(fv)

if __name__ == "__main__":
    run()
