__author__ = 'Bruno'

class Route():

    def __init__(self, code_of_cities, distance):
        """
        initiates values for self
        :param code_of_cities: list containing the TWO cities of this route
        :param distance: distance of the route
        :return:
        """
        self.code_of_cities = code_of_cities
        self.distance = distance

    def other_city(self, code):
        if not code in self.code_of_cities:
            return "code " + code + " not is these route"
        if self.code_of_cities[0] == code:
            return self.code_of_cities[1]
        return self.code_of_cities[0]

    def __str__(self):
        """
        :return: string representing route
        """
        string = ""
        string += "code of cities: " + str(self.code_of_cities)
        string += "\ndistance: " + str(self.distance)
        return string
