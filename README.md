### Overview

Weight Tracker is a Flask application you can use to track and then predict your weight based on your habits.

I got sick of having to track all my food down to the calorie when I can predict outcomes based on overall trends and tracking a few key metrics - weight, body fat %, and a few body measurements.

### Requirmements

MongoDB >= 3.0.4
Python >= 3.3.5
Flask >= 0.10.1
flask-bootstrap >= 3.3.5.2
flask-wtf >= 0.12
pymongo >= 3.0.3
wtf >= 2.0.2


### Running Weight Tracker

Download, install and then run [MongoDB](https://www.mongodb.org/)

Rename config/example-config.ini to config/config.ini

At a minimum, fill in the details for your MongoDB installation in the MongoDB section.

In the root directory, run the following command (on Mac or Linux) to make the index.py file executable
  
  chmod +x ./index.py

Run the index.py file to start Weight Tracker

  ./index.py

Start tracking your stats!