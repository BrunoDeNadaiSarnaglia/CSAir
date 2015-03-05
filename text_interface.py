# from Statistics import longest_flight_in_the_network
import webbrowser
from Statistics import longest_flight_in_the_network, shortest_flight_in_the_network, average_distance_of_all_flights, \
    biggest_city_served_by_CSAir, smallest_city_served_by_CSAir, average_population_of_all_cities, \
    cities_by_continent_served_by_CSAir, CSAir_hubs_cities
from graph_builder import get_set_of_cities, get_set_of_route, get_set_of_data_sources, build_graph_from_file, \
    build_graph, get_graph

__author__ = 'Bruno'

global graph
global set_of_cities
global set_of_route
global set_of_data_sources


def main():
    """
    Loop that keep getting user choice and displaying what he want
    """
    global graph
    graph = get_graph()
    global set_of_cities
    set_of_cities = get_set_of_cities()
    global set_of_route
    set_of_route = get_set_of_route()
    global set_of_data_sources
    set_of_data_sources = get_set_of_data_sources()
    option = print_menu()
    while (option != "5"):
        if option == "1":
            print_city_name_and_code()
        elif option == "2":
            code = print_city_menu()
            print_city_informations(code)
        elif option == "3":
            statistical_option = print_statistical_menu()
            print_selected_statistical_information(statistical_option)
        elif option == "4":
            open_map()
        else:
            print "Invalid choice"
        option = print_menu()


def print_menu():
    """
    Print the text interface and return the choice of the user
    :return: choice of the user
    """
    print "\nWelcome to CSAir! \nChoose:"
    print "1. List all cities that we fly to"
    print "2. Get info about a city"
    print "3. Statistical info about CSAir"
    print "4. Open map"
    print "5. Close system"
    return raw_input(">> ")

def print_statistical_menu():
    """
    Prints the statistical menu
    :return: option the user chose
    """
    print "a. the longest single flight in the network"
    print "b. the shortest single flight in the network"
    print "c. the average distance of all the flights in the network"
    print "d. the biggest city (by population) served by CSAir"
    print "e. the smallest city (by population) served by CSAir"
    print "f. the average size (by population) of all the cities served by CSAir"
    print "g. a list of the continents served by CSAir and which cities are in them"
    print "h. identifying CSAirs hub cities"
    return raw_input(">> ")

def print_selected_statistical_information(option):
    """
    If statements to select which function will be called to handle the user choice
    :param option: option the user chose
    :return:
    """
    if option == "a":
        print_longest_flight()
    elif option == "b":
        print_shortest_flight()
    elif option == "c":
        print_average_distance()
    elif option == "d":
        print_biggest_city()
    elif option == "e":
        print_smallest_city()
    elif option == "f":
        print_average_population()
    elif option == "g":
        print_list_of_cities_by_continent()
    elif option == "h":
        print_CSAir_hubs()
    else:
        print "Invalid choice"


def print_CSAir_hubs():
    """
    print CSAir hubs
    :return:
    """
    print "CSAirs hub cities"
    list_of_cities = CSAir_hubs_cities()
    for code in list_of_cities:
        city = set_of_cities[code]
        print city.name + " (" + code + ")"

def print_list_of_cities_by_continent():
    """
    Print each continent followed by its countries that CSAir work on
    :return:
    """
    print "List of the continents served by CSAir and which cities are in them"
    cities_by_continent = cities_by_continent_served_by_CSAir()
    for continent, list_of_cities in cities_by_continent.items():
        print "\n" + continent + ":"
        for code in list_of_cities:
            city = set_of_cities[code]
            print "\t" + city.name + " (" + code + ")"


def print_average_population():
    """
    Print the population average
    :return:
    """
    print "The average size (by population) of all the cities served by CSAir"
    average_population = average_population_of_all_cities()
    print str(average_population)


def print_smallest_city():
    """
    Print the smallest city data
    :return:
    """
    print "The smallest city (by population) served by CSAir"
    smallest_city = smallest_city_served_by_CSAir()
    print smallest_city


def print_biggest_city():
    """
    Print the biggest city data
    :return:
    """
    print "The biggest city (by population) served by CSAir"
    biggest_city = biggest_city_served_by_CSAir()
    print biggest_city

def print_average_distance():
    """
    Print the average distance of all flights
    :return:
    """
    print "The average distance of all the flights in the network"
    average_distance = average_distance_of_all_flights()
    print str(average_distance)

def print_shortest_flight():
    """
    Print the shortest of flight
    :return:
    """
    print "The shortest single flight in the network"
    shortest_route = shortest_flight_in_the_network()
    code_of_cities = shortest_route.code_of_cities
    code0 = code_of_cities[0]
    code1 = code_of_cities[1]
    city0 = set_of_cities[code0]
    city1 = set_of_cities[code1]
    print "Cities: " + city0.name + " (" + code0 + ") " + city1.name + " (" + code1 + ") "
    print "Distance: " + str(shortest_route.distance)


def print_longest_flight():
    """
    Print the longest flight
    :return:
    """
    print "The longest single flight in the network"
    longest_route = longest_flight_in_the_network()
    code_of_cities = longest_route.code_of_cities
    code0 = code_of_cities[0]
    code1 = code_of_cities[1]
    city0 = set_of_cities[code0]
    city1 = set_of_cities[code1]
    print "Cities: " + city0.name + " (" + code0 + ") " + city1.name + " (" + code1 + ") "
    print "Distance: " + str(longest_route.distance)

def print_city_name_and_code():
    """
    print the name and the code of each city that CSAir flies
    """
    for city in set_of_cities.values():
        print city.name + " (" + city.code + ")"


def print_city_menu():
    """
    print a menu to the user choose what city's information he want
    :return: code of the city that the user wants information
    """
    print "Write city code:"
    return raw_input(">> ")


def print_city_informations(code):
    """
    Test if code is valid and print information or print a message of invalid code
    :param code:
    :return:
    """
    if code in set_of_cities:
        print set_of_cities[code]
        list_adj_city = graph[code]
        print "Possible destinations: "
        for code_destination, route in list_adj_city.items():  # run over the list of cities which have flies non-stop connecting
            city_destination = set_of_cities[code_destination]
            print city_destination.name + " (" + code_destination + ") " + str(route.distance)
    else:
        print "Code not found in our cities"

def open_map():
    request = "http://www.gcmap.com/mapui?P="
    for code_origin, list_of_code_destination in graph.items():
        for code_destination in list_of_code_destination:
            request += code_origin + "-" + code_destination + ",+"
    webbrowser.open(request)

if __name__ == "__main__":
    main()