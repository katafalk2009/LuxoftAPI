import requests
import time

FILMS_URL = 'https://swapi.dev/api/films/'
PEOPLE_URL = 'https://swapi.dev/api/people/'


class DATA():
    def __init__(self, attributes):
        for key in attributes:
            setattr(self, key, attributes[key])
    def __str__(self):
        return [i for i in self.__dict__]



def check_time(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {format(end - start, ".2f")} seconds.')
        return result
    return wrapper


@check_time
def get_object_data(url):
    response = requests.get(url).json()
    return DATA(response)


@check_time
def get_page_data(url):
    response = requests.get(url)
    return response.json()


@check_time
def get_all_data(url):
    response = requests.get(url)
    data = response.json()
    count = data['count']
    return [get_object_data(url+str(i)) for i in range(1, count+1)]



for p in get_all_data(PEOPLE_URL):
    print(p)