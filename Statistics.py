from graph_builder import get_set_of_cities, get_set_of_route, get_set_of_data_sources, get_graph

__author__ = 'Bruno'

# global set_of_cities
# set_of_cities = get_set_of_cities()
# global set_of_route
# set_of_route = get_set_of_route()
# global set_of_data_sources
# set_of_data_sources = get_set_of_data_sources()
# global graph_CSAir
# graph_CSAir = get_graph()

global graph_CSAir
graph_CSAir = get_graph()
global set_of_cities
set_of_cities = graph_CSAir.get_set_of_cities()
global set_of_route
set_of_route = graph_CSAir.get_set_of_routes()

def longest_flight_in_the_network():
    """
    Look for biggest distance flight
    :return longest_flight_route: route instance that has biggest distance
    """
    longest_flight_route = set_of_route[0]
    longest_flight_distance = longest_flight_route.distance
    for route in set_of_route:
        if route.distance > longest_flight_distance:
            longest_flight_distance = route.distance
            longest_flight_route = route
    return longest_flight_route

def shortest_flight_in_the_network():
    """
    Look for shortest distance flight
    :return shortest_flight_route: route instance that has shortest distance
    """
    shortest_flight_route = set_of_route[0]
    shortest_flight_distance = shortest_flight_route.distance
    for route in set_of_route:
        if route.distance < shortest_flight_distance:
            shortest_flight_distance = route.distance
            shortest_flight_route = route
    return shortest_flight_route

def average_distance_of_all_flights():
    """
    Iterate over all flights. Sum all distances and return the average of them
    :return average_of_all_distances: integer value representing the average of all distances
    """
    sum_of_all_distances = 0
    for route in set_of_route:
        sum_of_all_distances += route.distance
    average_of_all_distances = sum_of_all_distances/len(set_of_route)
    return average_of_all_distances

def biggest_city_served_by_CSAir():
    """
    Iterate over all cities and return the most populated one
    :return biggest_city: most populated city object
    """
    biggest_city = None
    for city in set_of_cities.values():
        if biggest_city == None or biggest_city.population < city.population:
            biggest_city = city
    return biggest_city

def smallest_city_served_by_CSAir():
    """
    Iterate over all cities and return the less populated one
    :return biggest_city: most populated city object
    """
    smallest_city = None
    for city in set_of_cities.values():
        if smallest_city == None or smallest_city.population > city.population:
            smallest_city = city
    return smallest_city

def average_population_of_all_cities():
    """
    Sum all city's population and take the average
    :return average_of_all_population: Integer representing average of all populations
    """
    sum_of_all_population = 0
    for city in set_of_cities.values():
        sum_of_all_population += city.population
    average_of_all_population = sum_of_all_population/len(set_of_cities)
    return average_of_all_population

def cities_by_continent_served_by_CSAir():
    """
    Iterate over cities, and append to dictionary lists
    :return continent_list_of_cities: dictionary indexed by continent containing cities code
    """
    continent_list_of_cities = {}
    for city in set_of_cities.values():
        if city.continent in continent_list_of_cities:
            continent_list_of_cities[city.continent].append(city.code)
        else:
            continent_list_of_cities[city.continent] = [city.code]
    return continent_list_of_cities

def CSAir_hubs_cities():
    list_of_cities = []
    number_of_routes = None
    for code, list_of_routes in graph_CSAir.get_graph().items():
        if number_of_routes == None:
            number_of_routes = len(list_of_routes)
            list_of_cities.append(code)
        elif number_of_routes == len(list_of_routes):
            list_of_cities.append(code)
        elif number_of_routes < len(list_of_routes):
            number_of_routes = len(list_of_routes)
            list_of_cities = [code]
    return list_of_cities