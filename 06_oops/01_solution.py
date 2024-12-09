class Car:
  total_car = 0

  def __init__(self, brand, model):
    self.__brand = brand # '__name' make the variable private (Encapsulation)
    self.__model = model
    Car.total_car += 1 # we also define with class name

  def full_name(self):
    return f"{self.__brand} {self.__model}"
  
  def get_brand(self): # getter method
    return self.__brand
  
  def fuel_type(self): # Polymorphism (Same name with different work)
    return "Petrol or Diesel"
  
  @staticmethod # static method / Decorator (Only available for main class, instance don't have access)
  def general_description():
    return "Cars are means of transport"
  
  @property # decorator
  def model(self):
    return self.__model
  
class ElectricCar(Car): # Inheritance
  def __init__(self, brand, model, batter_size):
    super().__init__(brand, model)
    self.battery_size = batter_size

  def fuel_type(self): # Polymorphism (Same name with different work)
    return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "80kWh")

print("Is my_tesla instance of ElectricCar Class:", isinstance(my_tesla, ElectricCar)) # check instance
print("Is my_tesla instance of Car Class:", isinstance(my_tesla, Car))

# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

my_safari = Car("Tata", "Safari")
# print(my_safari.fuel_type())

# print(Car.total_car)

# print(Car.general_description())

# print(my_tesla.model())

# my_car = Car("Hyundai", "Creta")
# print(my_car.brand)
# print(my_car.full_name())

class Engine:
  def engine_info(self):
    return "this is engine"

class Battery:
  def battery_info(self):
    return "this is battery"

class ElectricCarTwo(Engine, Battery, Car):
  pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())