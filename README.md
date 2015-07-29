### Overview

Weight Tracker is a Flask application you can use to track and then predict your weight based on your habits.

I got sick of having to track all my food down to the calorie when I can predict outcomes based on overall trends and tracking a few key metrics - weight, body fat %, and a few body measurements along with supplements and eating habits.

### Requirements

* [MongoDB](https://www.mongodb.org/) >= 3.0.4
* [Python](http://continuum.io/downloads) >= 3.3.5
* [Flask](http://flask.pocoo.org/) >= 0.10.1
* [flask-bootstrap](http://pythonhosted.org/Flask-Bootstrap/) >= 3.3.5.2
* [flask-wtf](https://flask-wtf.readthedocs.org/en/latest/) >= 0.12
* [pymongo](https://api.mongodb.org/python/current/) >= 3.0.3
* [wtf](https://pypi.python.org/pypi/WTForms) >= 2.0.2


### Running Weight Tracker

Install all of the required Python libraries.

Download, install and then run [MongoDB](https://www.mongodb.org/)

Rename config/example-config.ini to config/config.ini

At a minimum, fill in the details for your MongoDB installation in the MongoDB section of the config file.

In the root directory, run the following command (on Mac or Linux) to make the index.py file executable
  
    chmod +x ./index.py

Run the index.py file to start Weight Tracker

    ./index.py

Start tracking your stats by browsing to [http://localhost:5000](http://localhost:5000)

### The ToDo List

* Add supplement intake tracking
* Add a food journal
* Add pagination to the measurement history
* Add a predictive model for weight