class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model =  model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make  + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has " + str(self.odometer_reading) +" miles on it")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")
    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size =  battery_size
    
    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh bettery")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 285
        message = "this car can go about " + str(range) + " miles on a full charge"
        print(message)
    
    def update_battery(self):
        if self.battery_size != 85:
           self.battery_size = 85
        
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 将实例作为属性
        self.battery = Battery()

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# my_tesla2 = ElectricCar('tesla', 'x', 2020)
# my_tesla2.battery.update_battery()
# my_tesla2.battery.get_range()