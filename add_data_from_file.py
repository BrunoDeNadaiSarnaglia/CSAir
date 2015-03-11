import json
from file_handler import read_file, load_cities_from_json, load_routes_from_json
from graph_builder import get_graph

__author__ = 'Bruno'

global graph_CSAir
graph_CSAir = get_graph()

def add_data_from_file():
    """
    User type the file name and the function loads the new cities and routes to the graph
    To test use the save option that will save new_data.json with the changes made by
    this function
    :return:
    """
    print "File Name:"
    file_name = raw_input(">> ")
    json_content = read_file(file_name)
    json_data = json.loads(json_content)
    set_of_cities = load_cities_from_json(json_data)
    set_of_route = load_routes_from_json(json_data)
    for route in set_of_route:
        graph_CSAir.add_route(route)
    for code, city in set_of_cities.items():
        graph_CSAir.add_city(code, city)
    print "Data added to the database!"
