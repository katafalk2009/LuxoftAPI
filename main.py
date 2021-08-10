import requests
import time
from functools import wraps

FILMS_URL = 'https://swapi.dev/api/films/'
PEOPLE_URL = 'https://swapi.dev/api/people/'


class DATA:
    """Class to represent an object data received
     from api. Same for people and films."""
    def __init__(self, attributes):
        for key in attributes:
            setattr(self, key, attributes[key])

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        elif hasattr(self, 'title'):
            return self.title
        else:
            return None


def check_time(f):
    """Decorate function to check time of its execution."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f'Execution time: {format(end - start, ".2f")} seconds.')
        return result
    return wrapper


@check_time
def get_object_data(url):
    """Return response of GET request to API as an object of class DATA."""
    response = requests.get(url).json()
    return DATA(response)


@check_time
def get_page_data(url):
    """Return response of GET request to API decoded from json to a dict."""
    response = requests.get(url)
    return response.json()


@check_time
def get_page_status_code(url):
    """Return status code of GET request to API.    """
    response = requests.get(url)
    return response.status_code


@check_time
def get_all_data(url):
    """Return all objects data from a GET request
     to a resource as object of DATA class."""
    response = requests.get(url)
    data = response.json()
    count = data['count']
    return [get_object_data(url+str(i)) for i in range(1, count+1)]


def main():
    people = get_all_data(PEOPLE_URL)
    films = get_all_data(FILMS_URL)
    for person in people:
        print(person)
    for film in films:
        print(film)


if __name__ == '__main__':
    main()