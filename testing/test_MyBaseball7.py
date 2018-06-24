from app.MyBaseball7 import *

def test_search_team_abbrev():
    team_info = [{"abbrev" : "NYM"}, {"abbrev" : "ATL"}, {"abbrev" : "MIA"}, {"abbrev" : "WSH"}, {"abbrev" : "PHI"}]
    result = search_team_abbrev(team_info, "NYM")
    assert result == True

def test_location_time():
    value1 = "D"
    value2 = "D"
    item1a = 100
    item1b = 200
    item2a = 300
    item2b = 150
    Team1 = "Marlins"
    Team2 = "Rays"
    result = location_time(value1, value2, item1a, item1b, item2a, item2b, Team1, Team2)
    assert result == "Rays"
