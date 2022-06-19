import pandas as pd
from bs4 import BeautifulSoup


def parse_webpage(source):
    """Parse content from various tags from OpenTable restaurants listing"""
    data, item = pd.DataFrame(), {}
    soup = BeautifulSoup(source, 'lxml')
    for i, restaurant in enumerate(soup.find_all('div', class_='ZqTsEGHydE3f5jJAHXtS')):
        print("Found {} restaurants in the page".format(len(restaurant)))
        item['name'] = restaurant.find('a', class_='CZSRtRus5QKZeZX0z27m')['aria-label']
        print(item['name'])


