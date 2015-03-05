from unittest import TestCase
from graph_builder import get_graph

__author__ = 'Bruno'


class graph_and_parsing_test(TestCase):


    def test_cities_in_graph(self):
        graph = get_graph()
        self.assertEqual(False, "ABC" in graph)
        self.assertEqual(True, "MEX" in graph)
        self.assertEqual(True, "SAO" in graph)
        self.assertEqual(True, "VIX" in graph)
        self.assertEqual(True, "CHM" in graph)

    def test_edges_in_graph(self):
        graph = get_graph()
        self.assertEqual({}, graph["VIX"])
        self.assertEqual({}, graph["CHM"])
        list_adj_SAO = graph["SAO"]
        self.assertEqual(True, "CHI" in list_adj_SAO)
        self.assertEqual(True, "LOS" in list_adj_SAO)
        self.assertEqual(True, "LAX" in list_adj_SAO)
        self.assertEqual(True, "MAD" in list_adj_SAO)
        self.assertEqual(True, "BOG" in list_adj_SAO)
        self.assertEqual(True, "BUE" in list_adj_SAO)
        self.assertEqual(False, "VIX" in list_adj_SAO)
        self.assertEqual(False, "MEX" in list_adj_SAO)
        self.assertEqual(False, "YYZ" in list_adj_SAO)
        list_adj_CHI = graph["CHI"]
        self.assertEqual(True, "SAO" in list_adj_CHI)
        list_adj_LOS = graph["LOS"]
        self.assertEqual(True, "SAO" in list_adj_LOS)
        list_adj_YYZ = graph["YYZ"]
        self.assertEqual(False, "SAO" in list_adj_YYZ)