# Project Planning

## Problem Statement

### Primary User

The primary user is an amateur sports gambler who bets on Major League Baseball games as part of a survivor pool.  

### User Needs Statement

As a sports gambler who desires to increase his/her odds of winning bets, the user can benefit from a tool that performs statistical analysis to determine which Major League Baseball team has the best odds of winning its daily matchup.  The application specifically addresses the needs of a gambler in a survivor pool.  

In the survivor pool, the goal is to correctly select the winner of one game each day.  The pool ends for the gambler with one of the following outcomes:
1. The gambler loses a bet
2. All other gamblers have lost a bet
3. The gambler and at least one other competitor correctly select 30 winners in a row

### As-is Process Description
1. View Major League Baseball matchups from ESPN.com or another source
2. Determine which team is most likely to win based on personal knowledge
3. Manually select a team for the survivor pool and hope it wins

### To-be Process Description
1. View Major League Baseball matchups from ESPN.com or another source (outside of application)
2. Input daily matchups into application, input which team is playing at home, and input whether it is a day or night game
3. Application prints a report detailing the odds that each entered team will win, the data used to develop these odds, and a recommendation of who the gambler should bet on (minimum of two matchups entered in order to receive a recommendation)
4. Among the eligible teams, manually select the team with the highest probability of winning, enter it into the survivor pool, and hope the selected team wins (outside of application)

### Result

The amateur gambler is currently relying on personal judgment to select teams.  By utilizing this powerful resource, the gambler will be able to make a more educated decision regarding which team to select for the survivor pool.

## Information Requirements

### Information Inputs

1. The list of daily matchups of Major League Baseball Teams (will be entered by the gambler/user in string format)
2. For each matchup, the home team must be known (will be entered by the gambler/user in string format)
3. For each matchup, whether it is a day or night game must be known (will be entered by the gambler/user in string format)
4. The HTML contents of ESPN’s MLB standings website 

### Information Outputs

1. A file containing which teams are favored in their matchups based on key statistics and the odds that each team will win its matchup.  Additionally if more than one matchup is entered, a recommendation of which team to select for the bet will be provided (txt format).

## Technology Requirements

### APIs and Web Service Requirements

The following websites will need to be accessed in order to develop the application.  I have analyzed the websites and viewed the source code.  As of now, I have been able to successfully access the data needed to develop the application.

https://www.espn.com/mlb/standings

https://www.espn.com/mlb/standings/_/view/expanded

### Python Package Requirements

The application requires the user to employ the third-party BeautifulSoup package in order to parse data from the HTML contents of ESPN’s MLB standings website.  Additionally, the application requires the request package to scrape the contents from the websites listed above. Furthermore, the pytest package is needed for testing purposes.  

In addition to these python packages, the application will utilize the datetime, json, os, csv, itertools, glob, and random modules.  These modules are needed for developing the application logic, for creating the presentation of the output, and for creating the desired output files.

### Hardware Requirements

The application will be running on the user's local computer. I won’t be deploying this application to a public server.
