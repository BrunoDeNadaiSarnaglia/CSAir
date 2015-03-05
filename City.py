__author__ = 'Bruno'

class City():
    """
    City class that store the characteristic of a city
    """

    def __init__(self, code, name, country, continent, timezone, coordinates, population, region):
        """
        Store the Characteristic of a city
        :param code: code of the city
        :param name: name of the city
        :param country: country that city belongs
        :param continent: continent that city belongs
        :param timezone: timezone of city
        :param coordinates: coordinates of city
        :param population: population of city
        :param region: region where city is in
        :return:
        """
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region

    def __str__(self):
        """
        :return: string representing City
        """
        string = ""
        string += "code: " + self.code
        string += "\nname: " + self.name
        string += "\ncountry: " + self.country
        string += "\ncontinent: " + self.continent
        string += "\ntimezone: " + str(self.timezone)
        string += "\ncoordinates: " + str(self.coordinates)
        string += "\npopulation: " + str(self.population)
        string += "\nregion: " + str(self.region)
        return string