from ctypes import Union
import unittest
from city_function import city_function

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_string = city_function('chengdu', 'china')
        self.assertEqual(formatted_string, 'chengdu , china')
    def test_city_population(self):
        formatted_string = city_function('chengdu', 'china', population=20000)
        self.assertEqual(formatted_string, 'chengdu , china -population 20000')
unittest.main()
