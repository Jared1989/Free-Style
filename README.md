# MLB Game Predictor App

A command-line Python application which processes user inputs and Major League Baseball team record data from [ESPN'S MLB Standings](https://www.espn.com/mlb/standings) in order to provide predictions as to which team which team should be chosen on a given day in a [MLB Survivor Pool](https://github.com/Jared1989/Free-Style/blob/master/PLANNING.md)

## Installation

First, "fork" this upstream repository under your own control.

Then download your forked version of this repository using the GitHub.com online interface or the Git command-line interface. If you are using command-line Git, you can download it by "cloning" it:

```sh
git clone https://github.com/YOUR_USERNAME/Free-Style.git
```

After downloading your forked repository, navigate into its root directory except the testing instructions:

```sh
cd app/
```

> NOTE: all commands in this document assume you are running them from this root directory.

Install package dependencies using one of the following commands, depending on how you have installed Python and how you are managing packages:

```sh
# Pipenv on Mac or Windows:
pipenv install -r requirements.txt

# Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt

# All others:
pip install -r requirements.txt
```

If you are using Pipenv, enter a new virtual environment (`pipenv shell`) before running any of the commands below.

## Setup

Confirm that the repository contains an app directory and a testing directory
```sh
# The app directory should contain 2 files: `MyBaseball.py` and `__init__.py`

# The testing directory should contain 2 files: `test_MyBaseball7.py` and `__init__.py`
```

## Usage

View the [current day's MLB matchups](http://www.espn.com/mlb/schedule) to determine which games you want to analyze 

Run the recommendation script:

```sh
# Homebrew-installed Python 3.x on Mac OS:
python3 app/MyBaseball7.py

# All others:
python app/MyBaseball7.py
```
If script has been previously run:

```sh
# Enter yes ("y") or no ("n") to whether or not you'd like to delete the pick files
```
If script hasn't previously been run or after the previous step:

```sh
# Among the current day MLB matchups, enter two MLB team name abbreviations separated by a comma and a space (ex: NYM, NYY)

# If you don't know the team name abbreviations, type "help" for a list and then repeat the previous step

# Enter whether the first team you listed is the home team or away team (ex: H)

# Enter whether the game will be played during the day or at night (ex: D)

# Repeat these steps for as many matchups as you'd like

# Once the user is no longer interested in entering matchups, type "Done"
```

Finally, analyze the results in the command prompt and/or the newly created .txt file.  Then leave the application to place your bet in your MLB Survivor Pool.

## Testing

From the repository, navigate into the testing directory:

```sh
cd testing/
```
Run tests:

```sh
pytest
```
