from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    data_one_year = [row for row in data if row['year'] == year]
    makers_one_year = [item['automaker'] for maker in data_one_year for item in data_one_year]
    grouped_makers = [key for key in Counter(makers_one_year).most_common(1)]
    return grouped_makers[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    data_filtered = [row for row in data if row['year'] == year and row['automaker'] == automaker]
    models = set(item['model'] for model in data_filtered for item in data_filtered)
    return models
