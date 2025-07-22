# Q#1
class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand                  # Q#4 - Encapsulation
        self.__model = model
        Car.total_cars += 1    
    # Q#2
    def fullName(self):
        return f'{self.__brand} {self.__model}'
    
    # Q#4 - Encapsulation
    def get_Brand(self):
        return self.__brand
    
    
    # Q#5 - polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # Q#7
    
    @staticmethod
    def general_description():
        return "A mode of transportation"
    
    # Q#8
    @property
    def model(self):
        return self.__model

    
    
    
    # Q#3 - Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # Q#5 - polymorphism
    def fuel_type(self):
        return "Electric Charge"
    

# Q#10
class Battery():
    def battery(self):
        return "This is battery"

class Engine():
    def engine(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        
    
    
        
  
  
# Q#1    
my_car = Car("Toyota", "Supra")
# print(my_car.brand) 
# print(Car.model) X

# Q#2
# print(my_car.fullName())


# Q#4 - Encapsulation
# print(my_car.get_Brand())

# Q#5 - polymorphism
# print(my_car.fuel_type())

# Q#6
# print(Car.total_cars)

# Q#7
# print(Car.general_description()) X


# Q#8
# my_car.model = "City"
# print(my_car.model)
 
 

# Q#3
my_tesla = ElectricCar("Tesla","Model S", "85kmh")
# print(my_tesla.battery_size)
# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.fullName())
 

# Q#5 - polymorphism
# print(my_tesla.fuel_type())

# Q#6
# print(ElectricCar.total_cars)

# Q#7
# print(my_tesla.general_description()) X

# Q#9
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# Q#10
my_new_car = ElectricCarTwo("Tesla", "model M")
print(my_new_car.battery())
print(my_new_car.engine())
