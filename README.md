### Overview

Weight Tracker is a Flask application you can use to track and then predict your weight based on your habits.

I got sick of having to track all my food down to the calorie when I can predict outcomes based on overall trends and tracking a few key metrics - weight, body fat %, and a few body measurements along with supplements and eating habits.


### Requirements

* [Python](http://continuum.io/downloads) >= 3.3.5
* [MongoDB](https://www.mongodb.org/) >= 3.0.4
* [Flask](http://flask.pocoo.org/) >= 0.10.1
* [flask-script](https://github.com/smurfix/flask-script) >= 2.0.5
* [WTForms](https://github.com/wtforms/wtforms) >= 2.0.2
* [mongoengine](http://mongoengine.org/) >= 0.10.0
* [flask-mongoengine](https://github.com/MongoEngine/flask-mongoengine) >= 0.7.1


### Running Weight Tracker

Install all of the required Python libraries.

    pip install flask
    pip install flask-script
    pip install WTForms
    pip install mongoengine
    pip install flask_mongoengine

Download, install and then run [MongoDB](https://www.mongodb.org/)

Rename config/example-config.ini to config/config.ini

At a minimum, fill in the details for your MongoDB installation in the MongoDB section of the config file.

In the root directory, run the following command (on Mac or Linux) to make the manage.py file executable
  
    chmod a+x ./manage.py

Run the index.py file to start Weight Tracker

    python manage.py runserver

Start tracking your stats by browsing to [http://localhost:5000](http://localhost:5000)

### Features

* Track weight, body fat percentage, and three body measurements
* Add and manage inspirational phrases
* Track what you eat and drink, along with your mood at the time


### The ToDo List

* Add supplement intake tracking
* Add charty goodness to the homepage to show progress
* Add a randomly pulled inspiration to the homepage
* Add a predictive model for weight
