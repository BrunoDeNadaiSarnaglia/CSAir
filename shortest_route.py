from graph_builder import get_graph

__author__ = 'Bruno'

global graph_CSAir
graph_CSAir = get_graph()
global set_of_cities
set_of_cities = graph_CSAir.get_set_of_cities()
global set_of_route
set_of_route = graph_CSAir.get_set_of_routes()


def shortest_route():
    print "Origin city code"
    code_origin = raw_input(">> ")
    print "Destination city code"
    code_destination = raw_input(">> ")
    if code_origin not in set_of_cities or code_destination not in set_of_cities:
        return
    path = graph_CSAir.dijkstra(code_origin, code_destination)
    print_path(path)

def print_path(path):
    print "Path"
    for code in path:
        print set_of_cities[code].name + ' (' + code + ')'