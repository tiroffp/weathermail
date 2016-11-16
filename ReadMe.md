## WeatherMail

A simple Django app to send weather-based emails

## Setup and Installation 
This project was built using Python 3.5.1, with Django 1.10 and Requests 2.12.1
The two dependancies can be installed with pip via
```
pip install Django
```
and
```
pip install Requests
```

```db.sqlite3``` should already have the 100 most populous cities in the US pre-inserted, but if not, ```load_cities.sql``` can be run in the sqlite shell to insert the values. 
## To Send Mail
```sendmail.py``` can be run via the command line (i.e. ```python sendmail.py```). It requires no other arguements.