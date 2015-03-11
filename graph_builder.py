import json

from file_handler import read_file, load_cities_from_json, load_routes_from_json, load_data_sources_from_json
from graph import Graph


__author__ = 'Bruno'

global graph_CSAir
global set_of_cities
global set_of_route
global set_of_data_sources

def get_graph():
    return graph_CSAir

def get_set_of_cities():
    """
    :return set_of_cities: set with all cities
    """
    return set_of_cities

def get_set_of_route():
    """
    :return set_of_route: set with all routes
    """
    return set_of_route

def get_set_of_data_sources():
    """
    :return set_of_data_sources: set with all data sources
    """
    return set_of_data_sources

def read_json_data(file_name):
    """
    read the json and initialize its information. It fills set_of_cities and set_of_routes
    that will be used to construct the graph
    """
    json_content = read_file(file_name)
    json_data = json.loads(json_content)
    global set_of_cities
    global set_of_route
    global set_of_data_sources
    set_of_cities = load_cities_from_json(json_data)
    set_of_route = load_routes_from_json(json_data)
    set_of_data_sources = load_data_sources_from_json(json_data)

def build_graph_from_file(file_name):
    """
    With set of cities and routes, we create the graph
    the graph is a dictionary that each city code index another dictionary
    these second dictionary is indexed by the code of the other city in the route
    and give us the route
    """
    read_json_data(file_name)
    graph = {}
    for code in set_of_cities:
        graph[code] = {}
    for route in set_of_route:
        codes_of_cities = route.code_of_cities
        code0 = codes_of_cities[0]
        code1 = codes_of_cities[1]
        list_adj_of_code0 = graph[code0]
        list_adj_of_code0[code1] = route
        list_adj_of_code1 = graph[code1]
        list_adj_of_code1[code0] = route
    return graph



def build_graph():
    """
    function that when called build all data structures
    :return:
    """
    read_json_data('map_data.json')
    global graph_CSAir
    graph_CSAir = Graph(set_of_cities, set_of_route)


build_graph()