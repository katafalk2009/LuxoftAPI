import requests
import time
from abc import ABC
FILMS_URL = 'https://swapi.dev/api/films/'
PEOPLE_URL = 'https://swapi.dev/api/people/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/39.0.2171.95 Safari/537.36'}


class DATA(ABC):
    def __init__(self, attributes):
        for key in attributes:
            setattr(self, key, attributes[key])


def check_time(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {format(end - start, ".2f")} seconds.')
        return result
    return wrapper


@check_time
def get_object_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        obj = DATA(response.json())
        return obj
    else:
        print(response)


@check_time
def get_page_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response)


@check_time
def get_all_data(url, headers):
    final_results = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        count = data['count']
        for i in range(1, count+1):
            response = requests.get(url+str(i), headers=headers)
            if response.status_code == 200:
                obj = DATA(response.json())
                final_results.append(obj)
            else:
                print(response)
    else:
        print(response)
    return final_results


