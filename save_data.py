import json
from graph_builder import get_graph

__author__ = 'Bruno'


global graph_CSAir
graph_CSAir = get_graph()
global set_of_cities
set_of_cities = graph_CSAir.get_set_of_cities()
global set_of_route
set_of_route = graph_CSAir.get_set_of_routes()

def save_data():
    """
    This function saves a json file with the changes made
    """
    new_data = {}
    new_data['data sources'] = []
    new_data['metros'] = []
    new_data['routes'] = []
    for code in set_of_cities:
        city = set_of_cities[code]
        data = {}
        data['code'] = city.code
        data['name'] = city.name
        data['country'] = city.country
        data['continent'] = city.continent
        data['timezone'] = city.timezone
        data['coordinates'] = city.coordinates
        data['population'] = city.population
        data['region'] = city.region
        new_data['metros'].append(data)
    for route in set_of_route:
        code_of_cities = route.code_of_cities
        distance = route.distance
        data = {}
        data['ports'] = code_of_cities
        data['distance'] = distance
        new_data['routes'].append(data)

    with open("new_data.json", 'wb') as outfile:
        json.dump(new_data, outfile, sort_keys=True, indent=4, separators=(',', ':'))

    print "Changes saved in new_data.json"