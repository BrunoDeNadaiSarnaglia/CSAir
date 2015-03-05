from City import City
import json
from Route import Route

__author__ = 'Bruno'


def read_file(file_name):
    """
    Passing a string with the name of a file, it returns the content or exit if file doesn't exist
    :param file_name: name of file that function is opening
    :return: content: content of file_name
    """
    try:
        file = open(file_name, "r")
    except IOError:
        exit("Error opening " + file_name)
    content = file.read()
    file.close()
    return content


def main():
    json_content = read_file("map_data.json")
    json_data = json.loads(json_content)
    set_of_cities = load_cities_from_json(json_data)
    set_of_route = load_routes_from_json(json_data)
    set_of_data_sources = load_data_sources_from_json(json_data)
    # print set_of_data_sources


def load_cities_from_json(json_data):
    """
    Function that get the Json and return a dictionary of all cities
    :param json_data: json with the data to be retrieved
    :return set_of_cities: return a dictionary with all  cities included
    """
    json_cities = json_data["metros"]
    set_of_cities = {}
    for city_dictionary in json_cities:
        code = city_dictionary["code"]
        name = city_dictionary["name"]
        country = city_dictionary["country"]
        continent = city_dictionary["continent"]
        timezone = city_dictionary["timezone"]
        coordinates = city_dictionary["coordinates"]
        population = city_dictionary["population"]
        region = city_dictionary["region"]
        city = City(code, name, country, continent, timezone, coordinates, population, region)
        set_of_cities[code] = city
    return set_of_cities


def load_routes_from_json(json_data):
    """
    Function that get the Json and return a list of all routes
    :param json_data: json with the data to be retrieved
    :return set_of_routes: list containing all Routes
    """
    json_routes = json_data["routes"]
    set_of_routes = []
    for route in json_routes:
        code_of_cities = route["ports"]
        distance = route["distance"]
        route = Route(code_of_cities, distance)
        set_of_routes.append(route)
    return set_of_routes


def load_data_sources_from_json(json_data):
    json_data_sources = json_data["data sources"]
    set_of_data_sources = json_data_sources  # json_data_sources is already a list
    return set_of_data_sources