# restaurant-webscraper
Solution to collect alternative data on restaurants and deliver trading insights 

## Description and motivation
I recently went to New York and was amazed by the number and diversity of restaurants in the city.
TheInternet pages collecting data about restaurants are great source for alternative data collection.
Information about the restaurants features, bookings and users reviews can provide precious insights for a business that desires to understand the consumers behaviours or to get further information about food and beverages.
This service uses Selenium to open a browser a scrap restaurants information from it.
It loads and extract the HTML source code, then utilises Beautifulsoup to extract specific features from the pages.


## Technical Specifications

### Setup
Mark `src/` as Root directory.
All dependencies are listed in `requirements.txt`. To install them in your environment run:
```
pip install -r requirements.txt
```

I recommend you create a virtual environment to run the service in it.

### Run the service
To run the service, navigate to the `src/` directory and run:
```
python main.py
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