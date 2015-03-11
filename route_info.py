from graph_builder import get_graph

__author__ = 'Bruno'

global graph_CSAir
graph_CSAir = get_graph()
global set_of_cities
set_of_cities = graph_CSAir.get_set_of_cities()
global set_of_route
set_of_route = graph_CSAir.get_set_of_routes()

def get_route_info():
    route_cities = get_route_cities()
    if not valid_route(route_cities):
        print "Not valid Route"
        return
    # total_distance = 0
    # total_cost = 0
    # total_time = 0
    # price_per_kilometer = 0.35
    # for i in range(0,len(route_cities)-1):
    #     distance = graph_CSAir.get_distance(route_cities[i], route_cities[i+1])
    #     total_distance += distance
    #     total_cost += distance*max(price_per_kilometer, 0)
    #     travel_time = calc_travel_time(distance)
    #     total_time += travel_time
    #     price_per_kilometer -= 0.05
    #     if()
    total_distance = get_total_distance(route_cities)
    total_cost = get_total_cost(route_cities)
    total_time = get_total_time(route_cities)
    print "Total Distance: " + str(total_distance)
    print "Total Cost: " + str(total_cost)
    print "Total Time: " + str(total_time)

def get_total_time(route_cities):
    """
    Calculates the total time to final destination
    :param route_cities: list of codes
    :return: time to travel
    """
    total_time = 0
    for i in range(len(route_cities)-1):
        distance = graph_CSAir.get_distance(route_cities[i], route_cities[i+1])
        travel_time = calc_travel_time(distance)
        total_time += travel_time
        if i != len(route_cities)-2:
            total_time += calc_waiting_time_in_hub(route_cities[i+1])
    return total_time

def get_total_cost(route_cities):
    """
    Calculates the total cost to final destination
    :param route_cities: list of codes
    :return: total cost
    """
    total_cost = 0
    price_per_kilometer = 0.35
    for i in range(0,len(route_cities)-1):
        distance = graph_CSAir.get_distance(route_cities[i], route_cities[i+1])
        total_cost += distance*max(price_per_kilometer, 0)
        price_per_kilometer -= 0.05
    return total_cost

def get_total_distance(route_cities):
    """
    Calculates the total distance to final destination
    :param route_cities: list of codes
    :return: total distance
    """
    total_distance = 0
    for i in range(0,len(route_cities)-1):
        distance = graph_CSAir.get_distance(route_cities[i], route_cities[i+1])
        total_distance += distance
    return total_distance

def calc_waiting_time_in_hub(code):
    """
    Calculates the time spent by passenger in an airport subtracting from two hours the number of routes time ten minutes
    :param code: code of the city where passenger will be waiting
    :return: time waiting
    """
    num_route = graph_CSAir.get_num_routes(code)
    return 2 - num_route/6.0


def calc_travel_time(distance):
    """
    Calculate the time, for d > 400 it is (d + 400) / 750 for d less then 400 is 2d/750
    :param distance: distance between two cities
    :return: travel time between cities
    """
    if distance < 400:
        return 2.0*distance/750.0
    elif distance >= 400:
        return (distance + 400.0)/750.0

def get_route_cities():
    print "Type city codes separate by space:"
    string = raw_input(">> ")
    route_cities = parse_input(string)
    return route_cities

def parse_input(string):
    route_cities = string.split()
    return route_cities

def valid_route(route_cities):
    if len(route_cities) < 2:
        return False
    for i in range(0,len(route_cities)-1):
        if not graph_CSAir.exist_route(route_cities[i], route_cities[i+1]):
            return False
    return True