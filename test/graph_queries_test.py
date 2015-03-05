from Statistics import longest_flight_in_the_network, shortest_flight_in_the_network, average_distance_of_all_flights, \
    biggest_city_served_by_CSAir, smallest_city_served_by_CSAir, average_population_of_all_cities, CSAir_hubs_cities, \
    cities_by_continent_served_by_CSAir
from graph_builder import get_graph
from unittest import TestCase

__author__ = 'Bruno'


class graph_queries(TestCase):

    graph = get_graph()

    def test_longest_flight(self):
        longest_flight = longest_flight_in_the_network()
        self.assertEqual(1999, longest_flight.distance)

    def test_shortest_flight(self):
        shortest_flight = shortest_flight_in_the_network()
        self.assertEqual(1, shortest_flight.distance)

    def test_average_distance(self):
        average_distance = average_distance_of_all_flights()
        self.assertEqual(1000, average_distance)

    def test_biggest_city_served_by_CSAir(self):
        biggest_city = biggest_city_served_by_CSAir()
        self.assertEqual(biggest_city.code, "SAO")

    def test_smallest_city_served_by_CSAir(self):
        smallest_city = smallest_city_served_by_CSAir()
        self.assertEqual(smallest_city.code, "BUE")

    def test_average_population_of_all_cities(self):
        average_population = average_population_of_all_cities()
        self.assertEqual(average_population, 50000000)

    def test_cities_by_continent_served_by_CSAir(self):
        cities_by_continent = cities_by_continent_served_by_CSAir()
        list_cities_south_america = cities_by_continent["South America"]
        self.assertEqual(True, "VIX" in list_cities_south_america)
        list_cities_north_america = cities_by_continent["North America"]
        self.assertEqual(True, "CHM" in list_cities_north_america)
        self.assertEqual(False, "VIX" in list_cities_north_america)
        self.assertEqual(False, "CHM" in list_cities_south_america)

    def test_CSAir_hubs_cities(self):
        list_hubs = CSAir_hubs_cities()
        self.assertEqual(4, len(list_hubs))
        self.assertEqual(True, "SAO" in list_hubs)
        self.assertEqual(True, "CHI" in list_hubs)
        self.assertEqual(True, "HKG" in list_hubs)
        self.assertEqual(True, "IST" in list_hubs)
        self.assertEqual(False, "BUE" in list_hubs)
