# MLB Game Predictor App

A command-line Python application which processes user inputs and Major League Baseball team record data from [ESPN'S MLB Standings](https://www.espn.com/mlb/standings) in order to provide predictions as to which team which team would win a user entered matchup.

## Installation

First, "fork" this upstream repository under your own control.

Then download your forked version of this repository using the GitHub.com online interface or the Git command-line interface. If you are using command-line Git, you can download it by "cloning" it:

```sh
git clone https://github.com/YOUR_USERNAME/Free-Style.git
```

After downloading your forked repository, navigate into its root directory:

```sh
cd baseball/
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

All commands below assume you are running them from this repository's root directory.

## Usage

Run the recommendation script:

```sh
# Homebrew-installed Python 3.x on Mac OS:
python3 app/my_baseball_app.py

# All others:
python app/my_baseball_app.py
```

## Testing

Run tests:

```sh
pytest
```
