__author__ = 'Bruno'

class Graph:
    """
    graph class that simulates
    """
    def __init__(self, set_of_cities, set_of_routes):
        """
        constructor that builds the graph
        :param set_of_cities: set of cities
        :param set_of_routes: set of routes
        :return:
        """
        self.set_of_cities = {}
        self.set_of_routes = []
        self.graph = {}
        for code, city in set_of_cities.items():
            self.add_city(code, city)
        for route in set_of_routes:
            self.add_route(route)

    def add_city(self, code, city):
        """
        Add city to the graph and to set_of_cities data structure
        :param code: code of the city to be inserted
        :param city: city object to be inserted
        :return:
        """
        if code not in self.set_of_cities:
            self.set_of_cities[code] = city
        if code not in self.graph:
            self.graph[code] = {}

    def add_route(self, route):
        """
        Add route to the graph and to the set_of_route
        :param route: city object to be inserted
        :return:
        """
        if route not in self.set_of_routes:
            codes_of_cities = route.code_of_cities
            code_destination = codes_of_cities[0]
            code_origin = codes_of_cities[1]
            if code_destination not in self.set_of_cities or code_origin not in self.set_of_cities:
                return
            self.set_of_routes.append(route)
            list_adj_of_code_destination = self.graph[code_destination]
            list_adj_of_code_destination[code_origin] = route
            list_adj_of_code_origin = self.graph[code_origin]
            list_adj_of_code_origin[code_destination] = route

    def remove_city(self, code):
        """
        remove the city from the graph
        :param code: code of the city you will remove
        :return:
        """
        if code in self.set_of_cities:
            del self.set_of_cities[code]
            list_adj_code = self.graph[code]
            for code_destination in list_adj_code:
                list_adj_code_destination = self.graph[code_destination]
                self.set_of_routes.remove(list_adj_code_destination[code])
                del list_adj_code_destination[code]
            del self.graph[code]

    def remove_route(self, code_origin, code_destination):
        """
        Remove routes from the graph
        :param code_origin: code of one city
        :param code_destination: code of the other city
        :return:
        """
        if code_origin in self.set_of_cities and code_destination in self.set_of_cities:
            list_adj_code_destination = self.graph[code_destination]
            if code_origin in list_adj_code_destination:
                self.set_of_routes.remove(list_adj_code_destination[code_origin])
                del list_adj_code_destination[code_origin]
                list_adj_code_origin = self.graph[code_origin]
                del list_adj_code_origin[code_destination]

    def edit_city(self, code, city):
        if code not in self.set_of_cities:
            return
        self.set_of_cities[code] = city

    def get_distance(self, code_origin, code_destination):
        if self.exist_route(code_origin, code_destination):
            return self.graph[code_origin][code_destination].distance

    def dijkstra(self, code_origin, code_destination):
        """
        Compute all Dijkstra data structure and give the path
        :param code_origin: code of the origin airport
        :param code_destination: code of the destination airport
        :return:
        """
        if code_origin not in self.set_of_cities:
            return
        previous = {}
        distances = {}
        cities_to_check = []
        for code in self.set_of_cities:
            previous[code] = None
        for code in self.set_of_cities:
            distances[code] = None
        for code in self.set_of_cities:
            cities_to_check.append(code)
        distances[code_origin] = 0
        previous[code_origin] = code_origin
        while self.has_someone_to_iterate(cities_to_check, distances):
            code = self.get_min_distance_in_cities_to_check(cities_to_check, distances)
            for code_dest in self.graph[code]:
                self.relax_node(code, code_dest, distances, previous)
            cities_to_check.remove(code)
        return self.shortest_path(code_destination, distances, previous)

    def shortest_path(self, code_destination, distances, previous):
        """
        Compute the shortest path based on previous
        :param code_destination: code of the airport of destination
        :param distances: list of all distances from origin
        :param previous: list of all previous airport for short paths
        :return: codes of the shortest path
        """
        if distances[code_destination] is None:
            return
        code = code_destination
        path = []
        while previous[code] is not code:
            path.insert(0, code)
            code = previous[code]
        return path

    def relax_node(self, code_origin, code_destination, distances, previous):
        """
        Check and execute changes if there is any benefit in taking the fly from code_origin to code_destination
        :param code_origin: code of the airport of origin
        :param code_destination: code of the airport of destination
        :param distances: list of distance of all cities
        :param previous: list of all previous airport for short paths
        :return:
        """
        if code_destination in self.graph[code_origin]:
            if distances[code_destination] is None:
                distances[code_destination] = distances[code_origin] + self.graph[code_origin][code_destination].distance
                previous[code_destination] = code_origin
            elif distances[code_destination] > distances[code_origin] + self.graph[code_origin][code_destination].distance:
                distances[code_destination] = distances[code_origin] + self.graph[code_origin][code_destination].distance
                previous[code_destination] = code_origin

    def get_min_distance_in_cities_to_check(self, cities_to_check, distances):
        """
        :param cities_to_check: list of cities that should iterate
        :param distances: list of distances
        :return: return the code with min distance
        """
        min_distance = None
        code_min_distance = None
        for code in cities_to_check:
            if min_distance is None and distances[code] is not None:
                code_min_distance = code
                min_distance = distances[code_min_distance]
            elif min_distance is not None and distances[code] is not None and distances[code] < min_distance:
                code_min_distance = code
                min_distance = distances[code_min_distance]
        return code_min_distance

    def has_someone_to_iterate(self, cities_to_check, distances):
        """
        :param cities_to_check: list of cities that should iterate
        :param distances: list of distances
        :return: True if there is any airport able to iterate
        """
        for code in cities_to_check:
            if distances[code] is not None:
                return True
        return False


    def get_num_routes(self, code):
        """
        number of flights from code's airport
        :param code: code of the city
        :return: number of flights from code's airport
        """
        if code in self.graph:
            return len(self.graph[code])

    def exist_route(self, code_origin, code_destination):
        """
        Test if there is an route between the cities
        :param code_origin:
        :param code_destination:
        :return: boolean that will test if route exist
        """
        if code_origin in self.graph:
            list_adj_code_origin = self.graph[code_origin]
            if code_destination in list_adj_code_origin:
                return True
        return False

    def get_set_of_cities(self):
        """
        :return set_of_cities: set with all cities
        """
        return self.set_of_cities

    def get_set_of_routes(self):
        """
        :return set_of_route: set with all routes
        """
        return self.set_of_routes

    def get_list_adj_of_city(self, code):
        return self.graph[code]

    def get_graph(self):
        return self.graph