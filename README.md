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
* [parsedatetime](https://github.com/bear/parsedatetime) >= 1.5


### Running Weight Tracker

Install all of the required Python libraries.

    pip install flask
    pip install flask-script
    pip install WTForms
    pip install mongoengine
    pip install flask_mongoengine
    pip install parsedatetime

Download, install and then run [MongoDB](https://www.mongodb.org/)

Rename config/example-config.ini to config/config.ini

At a minimum, fill in the details for your MongoDB installation in the MongoDB section of the config file.

In the root directory, run the following command (on Mac or Linux) to make the manage.py file executable
  
    chmod a+x ./manage.py

Run the index.py file to start Weight Tracker

    python manage.py runserver

Start tracking your stats by browsing to [http://localhost:5000](http://localhost:5000)

### Features

* Track weight, body fat percentage, and     three body measurements
* Add and manage inspirational phrases
* Track what you eat and drink, along with your mood at the time
* Track your exercise along with motivation levels

### Developer-Specific Features
* Basic code generator to generate the model, view, and list, new and show templates.


### The ToDo List

* Add tiny habits (track the tiny habits you want to implement in your life)
* Add goals
    * Your big why + emotional significance
    * Point A: starting point (SMART)
    * Point B: define your goal (SMART)
* Add supplement intake tracking; currently this is part of food intake
* Add charty goodness to the homepage to show progress
  * How much time between meals per day, as a trend
  * Show all of the food and beverage consumed in a single day
* Add a randomly pulled inspiration to the homepage
* Add a predictive model for weight
* Add a resource section
* Add satiety to the food journal: level of hunger before/after eating

### Weight Tracker Code Generator

The code generator is found in the codegen folder.

1. Given the name of the object to create and the fields, the script will generate the:
  * Model
  * View
  * Templates: list, new, show
2. Once the files are generated:
    * Manually register the blueprint in __init__.py
    * Add the paths to the navigation in templates/base.html
    * Update the model with any field-level restrictions
