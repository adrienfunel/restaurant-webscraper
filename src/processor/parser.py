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

        # item['price'] = restaurant.find('span', class_='LFfaIs45Z1IbvWK_HRaH').split('AwKuroa75vy0Y4mLkyMr')[0].text
        item['price'] = 4 - restaurant.find('span', class_='AwKuroa75vy0Y4mLkyMr').text.count('$')

        cuis_loc = restaurant.find('div', class_='u9ONW2kqbJZxSOxtuBJq').text
        item['cuisine'] = cuis_loc.split('•')[1]
        item['location'] = cuis_loc.split('•')[2]

        data[i] = pd.Series(item)
    return data.T
