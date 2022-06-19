import pandas as pd
from bs4 import BeautifulSoup
import re


def parse_webpage(source):
    """Parse content from various tags from OpenTable restaurants listing"""
    data, item = pd.DataFrame(), {}
    soup = BeautifulSoup(source, 'lxml')
    for i, restaurant in enumerate(soup.find_all('div', class_='BhIFAK4B5RMKaTMhR78N')):
        print("Found {} restaurants in the page".format(len(restaurant)))
        item['name'] = restaurant.find('a', class_='CZSRtRus5QKZeZX0z27m')['aria-label'].replace(' restaurant', '')

        rating = restaurant.find('div', class_='vJWFYZLiWZbHIB0Hwa83')
        item['rating'] = float(rating['aria-label'].split()[0]) if rating else 'NA'

        reviews = restaurant.find('a', class_='z6Naf_ZXDiazhb9aJLoe')
        item['reviews'] = int(re.search('\d+', reviews.text).group()) if reviews else 'NA'

        item['price'] = 4 - restaurant.find('span', class_='AwKuroa75vy0Y4mLkyMr').text.count('$')

        cuis_loc = restaurant.find('div', class_='u9ONW2kqbJZxSOxtuBJq').text
        item['cuisine'] = cuis_loc.split('•')[1]
        item['location'] = cuis_loc.split('•')[2]

        data[i] = pd.Series(item)
    return data.T


def get_last_page(source):
    """Function to find the last page with data available"""
    soup = BeautifulSoup(source, 'lxml')
    try:
        page_nb = int(soup.find('a', class_='JINvM1QBDFqby0Geg27_ yGrkuQrH99UKfIE4YXQJ lq_cIcdgZyPE1fNfg6uz mnvRsuAUHkGrXs3xjRoy').text)
    except AttributeError:
        page_nb = None

    if page_nb:
        return page_nb
    else:
        return 1
