from unittest import TestCase
from City import City
from Route import Route
from Statistics import longest_flight_in_the_network
from graph_builder import get_graph

__author__ = 'Bruno'

global graph_CSAir
graph_CSAir = get_graph()
global set_of_cities
set_of_cities = graph_CSAir.get_set_of_cities()
global set_of_route
set_of_route = graph_CSAir.get_set_of_routes()


class editting_graph_test(TestCase):
    """
    class that will make all tests for edition functions to the graph
    """
    def test_add_city(self):
        city = City("ABC", "vitoria", "brazil", "South America", "obbofiwrf", "anoinaofe", 10000, 2)
        graph_CSAir.add_city("ABC", city)
        self.assertEqual("ABC" in graph_CSAir.get_graph(), True);

    def test_add_city2(self):
        city = City("ABD", "vitoria", "brazil", "South America", "obbofiwrf", "anoinaofe", 10000, 2)
        graph_CSAir.add_city("ABD", city)
        self.assertEqual("ABD" in graph_CSAir.get_set_of_cities(), True);

    def test_add_twice_same_cities(self):
        city = City("ABE", "vitoria", "brazil", "South America", "obbofiwrf", "anoinaofe", 10000, 2)
        graph_CSAir.add_city("ABE", city)
        city = City("ABE", "vitoria", "USA", "South America", "obbofiwrf", "anoinaofe", 10000, 2)
        graph_CSAir.add_city("ABE", city)
        self.assertEqual(graph_CSAir.get_set_of_cities()["ABE"].country, "brazil");

    def test_remove_city(self):
        graph_CSAir.remove_city("ABC")
        self.assertEqual("ABC" in graph_CSAir.get_graph(), False);

    def test_remove_city2(self):
        graph_CSAir.remove_city("XYZ")
        self.assertEqual("XYZ" in graph_CSAir.get_graph(), False);

    def test_add_route(self):
        route = Route(["BUE", "SAO"], 100000)
        graph_CSAir.add_route(route)
        self.assertEqual(longest_flight_in_the_network().distance, 100000)

    def test_add_route2(self):
        route = Route(["BUE", "AAA"], 200000)
        graph_CSAir.add_route(route)
        self.assertEqual(longest_flight_in_the_network().distance, 100000)

    def test_remove_route(self):
        graph_CSAir.remove_route("SAO", "BUE")
        self.assertEqual(longest_flight_in_the_network().distance != 100000, True)

    def test_edit_city(self):
        city = City("SAO", "vitoria", "brazil", "South America", "obbofiwrf", "anoinaofe", 10000, 2)
        graph_CSAir.edit_city("SAO", city)
        self.assertEqual(graph_CSAir.get_set_of_cities()["SAO"].name, "vitoria")
