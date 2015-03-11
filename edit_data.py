from City import City
from Route import Route
from graph_builder import get_graph

__author__ = 'Bruno'

global graph_CSAir
graph_CSAir = get_graph()
global set_of_cities
set_of_cities = graph_CSAir.get_set_of_cities()
global set_of_route
set_of_route = graph_CSAir.get_set_of_routes()


def edit_data():
    """
    Decide which operation will be executed
    :return:
    """
    option = print_edit_data_options()
    if option == "1":
        code = option_remove_city()
        graph_CSAir.remove_city(code)
    elif option == "2":
        remove_route()
    elif option == "3":
        add_city()
    elif option == "4":
        add_route()
    elif option == "5":
        edit_city()

def edit_city():
    """
    Edit city from graph
    :return:
    """
    print "Fill the following form"
    code = raw_input("Code: ")
    name = raw_input("Name: ")
    country = raw_input("Country: ")
    continent = raw_input("Continent: ")
    timezone = raw_input("Timezone: ")
    coordinates = raw_input("Coordinates: ")
    population = raw_input("Population: ")
    region = raw_input("Region: ")
    city = City(code, name, country, continent, timezone, coordinates, population, region)
    graph_CSAir.edit_city(code, city)

def add_route():
    """
    Add a route to the graph
    :return:
    """
    print "Fill the following form"
    code_origin = raw_input("Code Of Origin City: ")
    code_destination = raw_input("Code Of Destination City: ")
    distance = raw_input("Distance: ")
    route = Route([code_origin, code_destination], distance)
    graph_CSAir.add_route(route)

def add_city():
    """
    Add a city to the graph
    :return:
    """
    print "Fill the following form"
    code = raw_input("Code: ")
    name = raw_input("Name: ")
    country = raw_input("Country: ")
    continent = raw_input("Continent: ")
    timezone = raw_input("Timezone: ")
    coordinates = raw_input("Coordinates: ")
    population = raw_input("Population: ")
    region = raw_input("Region: ")
    city = City(code, name, country, continent, timezone, coordinates, population, region)
    graph_CSAir.add_city(code, city)

def remove_route():
    """
    Remove a route from the Graph
    :return:
    """
    print "Type city origin code:"
    code_origin = raw_input(">> ")
    print "Type city destination code:"
    code_destination = raw_input(">> ")
    graph_CSAir.remove_route(code_origin, code_destination)

def print_edit_data_options():
    """
    display an interface and show what user wants to do
    :return option: What user wants to do
    """
    print "Edit Data Options"
    print "1. Remove City"
    print "2. Remove Route"
    print "3. Add City"
    print "4. Add Route"
    print "5. Edit City"
    return raw_input(">> ")

def option_remove_city():
    print "Remove City"
    print "Type city code:"
    return raw_input(">> ")
