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

def test_get_teams():
    request_address = "https://www.espn.com/mlb/standings"
    result = get_teams(request_address)
    assert len(result) == 30

def test_get_stats1():
    request_address = "https://www.espn.com/mlb/standings"
    headings = ['W', 'L', 'PCT', 'GB', 'HOME', 'AWAY', 'RS', 'RA', 'DIFF', 'STRK', 'L10']
    result = get_stats(request_address, headings)
    assert len(result) == 30

def test_get_stats2():
    request_address = "https://www.espn.com/mlb/standings/_/view/expanded"
    headings = ['W', 'L', 'PCT', 'GB', 'DAY', 'NIGHT', '1-RUN', 'XTRA', 'ExWL']
    result = get_stats(request_address, headings)
    assert len(result) == 30
