def city_function(city_name, country_name, population=""):
    if population:
        return city_name + " , " + country_name + " -population " + str(population)
    else:
        return city_name + " , " + country_name
city_function('chengdu', 'china')