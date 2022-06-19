# restaurant-webscraper
Solution to collect alternative data on restaurants and deliver trading insights 

## Description and motivation
I recently went to New York and was amazed by the number and diversity of restaurants in the city.
The Internet pages collecting data about restaurants are great source for alternative data collection.
Information about the restaurants features, bookings and users reviews can provide precious insights for a business that desires to understand the consumers behaviours or to get further information about food and beverages.
This service uses Selenium to open a browser a scrap restaurants information from it.
It loads and extract the HTML source code, then utilises Beautifulsoup to extract specific features from the pages.
I have exposed the service via an API built using Flask, that allows for filtering of the data scraped from the web and can be used to build a data pipeline to feed in any ML models.


## Technical Specifications

### Setup
Mark `src/` as Root directory.
All dependencies are listed in `requirements.txt`. To install them in your environment run:
```
pip install -r requirements.txt
```

I recommend you create a virtual environment to run the service in it.

### Run the service
To run the service, you need to start the Flask app from the `app/` directory and run:
```
python flask_server.py
```


### Extracted features 
The service extracts the following features from the webpages:
```
'name': str,
'rating': float,
'reviews': int,
'price': int,
'cuisine': str,
'location': str
```

### Logging
The logging strategy is set up in `src/common/my_logger.py`. The logging level is **INFO** and contains all information
about the service run and the extracted info. The logging module will create a new `logs/` directory with a log file in the project folder to write
its logs. There are two handler: a file handler to write and store logs, and a stream handler to displays the logs
during execution.
