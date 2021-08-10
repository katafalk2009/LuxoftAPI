import main
import logging


logger = logging.FileHandler("x.log")


def test_resource_code_people():
    assert main.get_page_status_code(main.PEOPLE_URL) == 200


def test_resource_data_people():
    response = main.get_page_data(main.PEOPLE_URL)
    assert set(response.keys()) == {'count', 'next', 'previous', 'results'}


def test_resource_next_films():
    response = main.get_page_data(main.PEOPLE_URL)
    next_ = response['next']
    print(next_)
    assert main.get_page_status_code(next_) == 200


def test_id_code_people():
    assert main.get_page_status_code(main.PEOPLE_URL + '1') == 200


def test_id_data_people():
    response = main.get_page_data(main.PEOPLE_URL + '1')
    assert set(response.keys()) == {'name', 'birth_year', 'eye_color',
                                    'gender', 'hair_color', 'height', 'mass',
                                    'skin_color', 'homeworld', 'films',
                                    'species', 'starships', 'vehicles',
                                    'url', 'created', 'edited'}


def test_id_code_people_last():
    response = main.get_page_data(main.PEOPLE_URL)
    count = response['count']
    assert main.get_page_status_code(main.PEOPLE_URL + str(count)) == 200


def test_id_data_people_last():
    response = main.get_page_data(main.PEOPLE_URL)
    count = response['count']
    response_last = main.get_page_data(main.PEOPLE_URL + str(count))
    assert set(response_last.keys()) == {'name', 'birth_year', 'eye_color',
                                         'gender', 'hair_color', 'height',
                                         'mass', 'skin_color', 'homeworld',
                                         'films', 'species', 'starships',
                                         'vehicles', 'url', 'created',
                                         'edited'}


def test_schema_status_people():
    assert main.get_page_status_code(main.PEOPLE_URL + 'schema') == 200


def test_search_status_people():
    assert main.get_page_status_code(main.PEOPLE_URL + '?search=yoda') == 200


def test_search_data_people():
    response = main.get_page_data(main.PEOPLE_URL + '?search=yoda')
    assert response['results'][0]['name'] == 'Yoda'


def test_search_status_blablabla_people():
    assert main.get_page_status_code(
        main.PEOPLE_URL + '?search=blablabla') == 200


def test_search_data_blablabla_people():
    response = main.get_page_data(main.PEOPLE_URL + '?search=blablabla')
    assert response['results'] == []


def test_wookie_status_people():
    assert main.get_page_status_code(
        main.PEOPLE_URL + '1' + '?format=wookiee') == 200


def test_wookie_data_people():
    assert len(main.get_page_data(main.PEOPLE_URL + '1' + '?format=wookiee')) \
           == len(main.get_page_data(main.PEOPLE_URL + '1'))


def test_ivalid_resource():
    assert main.get_page_status_code('https://swapi.dev/api/person') == 404


def test_zero_id_code_people():
    assert main.get_page_status_code(main.PEOPLE_URL + '0') == 404


def test_id_code_people_last_plus1():
    response = main.get_page_data(main.PEOPLE_URL)
    count = response['count']
    assert main.get_page_status_code(main.PEOPLE_URL + str(count + 1)) == 404


def test_invalid_status_people():
    assert main.get_page_status_code(
        main.PEOPLE_URL + '1' + '?format=bookiee') == 404


def test_resource_code_films():
    assert main.get_page_status_code(main.FILMS_URL) == 200


def test_resource_data_films():
    response = main.get_page_data(main.FILMS_URL)
    assert set(response.keys()) == {'count', 'next', 'previous', 'results'}


def test_id_code_films():
    assert main.get_page_status_code(main.FILMS_URL + '1') == 200


def test_id_data_films():
    response = main.get_page_data(main.FILMS_URL + '1')
    assert set(response.keys()) == {'title', 'episode_id', 'opening_crawl',
                                    'director', 'producer', 'release_date',
                                    'species', 'starships', 'vehicles',
                                    'characters', 'planets', 'url', 'created',
                                    'edited'}


def test_id_code_films_last():
    response = main.get_page_data(main.FILMS_URL)
    count = response['count']
    assert main.get_page_status_code(main.FILMS_URL + str(count)) == 200


def test_id_data_films_last():
    response = main.get_page_data(main.FILMS_URL)
    count = response['count']
    response_last = main.get_page_data(main.FILMS_URL + str(count))
    assert set(response_last.keys()) == {'title', 'episode_id',
                                         'opening_crawl', 'director',
                                         'producer', 'release_date',
                                         'species', 'starships', 'vehicles',
                                         'characters', 'planets', 'url',
                                         'created', 'edited'}


def test_schema_status_films():
    assert main.get_page_status_code(main.FILMS_URL + 'schema') == 200


def test_search_status_films():
    assert main.get_page_status_code(main.FILMS_URL + '?search=hope') == 200


def test_search_data_films():
    response = main.get_page_data(main.FILMS_URL + '?search=hope')
    assert response['results'][0]['title'] == 'A New Hope'


def test_search_status_blablabla_films():
    assert main.get_page_status_code(
        main.FILMS_URL + '?search=blablabla') == 200


def test_search_data_blablabla_films():
    response = main.get_page_data(main.FILMS_URL + '?search=blablabla')
    assert response['results'] == []


def test_wookie_status_films():
    assert main.get_page_status_code(
        main.FILMS_URL + '1' + '?format=wookiee') == 200


def test_wookie_data_films():
    assert len(main.get_page_data(main.FILMS_URL + '1' + '?format=wookiee')) \
           == len(main.get_page_data(main.FILMS_URL + '1'))


def test_zero_id_code_films():
    assert main.get_page_status_code(main.FILMS_URL + '0') == 404


def test_id_code_films_last_plus1():
    response = main.get_page_data(main.FILMS_URL)
    count = response['count']
    assert main.get_page_status_code(main.FILMS_URL + str(count + 1)) == 404


def test_invalid_status_films():
    assert main.get_page_status_code(
        main.FILMS_URL + '1' + '?format=bookiee') == 404
