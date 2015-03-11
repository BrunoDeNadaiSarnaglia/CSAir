from unittest import TestCase
from graph_builder import get_graph
from route_info import get_total_distance, get_total_time, get_total_cost

__author__ = 'Bruno'


global graph_CSAir
graph_CSAir = get_graph()
global set_of_cities
set_of_cities = graph_CSAir.get_set_of_cities()
global set_of_route
set_of_route = graph_CSAir.get_set_of_routes()


class route_info_test(TestCase):
    """
    Tests to correctly calculate time to travel, cost and distance
    """

    def test_distance(self):
        self.assertEqual(get_total_distance(["SAO", "BUE"]), 1000)


    def test_distance_connection(self):
        self.assertEqual(get_total_distance(["SAO", "BUE", "SAO", "BUE"]), 3000)

    def test_time(self):
        self.assertEqual(get_total_time(["SAO", "BUE"]), 1.866666666666666666666666)

    def test_time_with_connection(self):
        self.assertEqual(get_total_time(["SAO", "BUE", "SAO", "BUE"]), 8.266666666666666666666666)

    def test_cost(self):
        self.assertEqual(get_total_cost(["SAO", "BUE"]), 350)

    def test_cost_with_connection(self):
        self.assertEqual(get_total_cost(["SAO", "BUE", "SAO", "BUE"]), 900)