# 方法一
# from car import Car, ElectricCar

# my_new_car = Car('audi', 'a4', '2012')
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_tesla2 = ElectricCar('tesla', 'x', 2020)
# my_tesla2.battery.update_battery()
# my_tesla2.battery.get_range()

# 方法二
import car
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'x', 2020)
print(my_tesla.get_descriptive_name())

# 方法三
# from car import *
