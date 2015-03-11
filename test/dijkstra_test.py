from unittest import TestCase
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


class dijkstra(TestCase):

    def test_min_distance(self):
        path = graph_CSAir.dijkstra("SAO", "LAX")
        self.assertEqual(path, ["SAO", "LAX"])


    def test_min_distance2(self):
        path = graph_CSAir.dijkstra("LAX", "SAO")
        self.assertEqual(path, ["LAX", "SAO"])

    def test_min_distance3(self):
        path = graph_CSAir.dijkstra("SAO", "IST")
        self.assertEqual(path, ["SAO", "MAD", "ALG", "IST"])


    def test_min_distance4(self):
        path = graph_CSAir.dijkstra("IST", "SAO")
        self.assertEqual(path, ["IST", "ALG", "MAD", "SAO"])

    def test_min_distance5(self):
        path = graph_CSAir.dijkstra("SCL", "BOG")
        self.assertEqual(path, ["SCL", "LIM", "BOG"])

    def test_min_distance6(self):
        path = graph_CSAir.dijkstra("LIM", "MEX")
        self.assertEqual(path, ["LIM", "MEX"])

    def test_min_distance7(self):
        city = City("ABC", "vitoria", "brazil", "South America", "obbofiwrf", "anoinaofe", 10000, 2)
        graph_CSAir.add_city("ABC", city)
        graph_CSAir.add_route(Route(["ABC", "LIM"], 100))
        graph_CSAir.add_route(Route(["ABC", "MEX"], 100))
        path = graph_CSAir.dijkstra("LIM", "MEX")
        self.assertEqual(path, ["LIM", "ABC","MEX"])


    def test_min_distance8(self):
        city = City("ABC", "vitoria", "brazil", "South America", "obbofiwrf", "anoinaofe", 10000, 2)
        graph_CSAir.add_city("ABC", city)
        graph_CSAir.add_route(Route(["ABC", "LIM"], 100))
        graph_CSAir.add_route(Route(["ABC", "MEX"], 100))
        path = graph_CSAir.dijkstra("MEX", "LIM")
        self.assertEqual(path, ["MEX", "ABC","LIM"])