# class Student:
#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["1","2"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name =  input("Name: ")
#     house = input("House: ")
#     return Student(name,house) # contructer call 
# # Getter
# def house(self):
#     return self.house

# #  Setter
# def house(self,house):
#     self.house = house
#     # student = Student()
#     # student.name = input("name: ")
#     # student.house = input("House: ")
#     # student = {}
#     # student["name"] = input("Name: ")
#     # student["house"] = input("House: ")
#     # name =  input("Name: ")
#     # house = input("House: ")
#     # return {
#     #     "name": name ,"house":house
#     # }

# if __name__ == "__main__":
#     main()     








class Car:
    total_car = 0

    def __init__(self,brand,model):  # we call init contructer
        self.__brand = brand
        self.__model = model
        Car.total_car += 1        

    def full_Name(self):
        return f"{self.__brand} {self.__model} "

    def get_brand(self):
        return self.__brand + "! "

    def fuel_type(self):
        return "PETROL OR DIESEL"
    
    @staticmethod
    def general_info():
        return "Cars are means of transport"
    @property
    def model(self):
        return self.__model
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine info"
class ElectricCar2(Battery,Engine,Car):
    pass



my_new_tesla = ElectricCar2("Tesla","model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())

# my_car = Car("Tata","Safari")
# my_car.model = "Model S"
# print(my_car.model())
# print(my_car.general_info())
# print(my_car.general_info())
# print(Car.general_info())





my_tesla = ElectricCar("Tesla" , "Model S", "85KWH")
# print(my_tesla.get_brand())
# print(my_tesla.__brand) # this will give error because brand is private and we can not access it directly
# print(my_tesla.full_Name())
# print(my_tesla.fuel_type())
ElectricCar("Tesla" , "Model A", "85KWH")
Car("Bugati", "1212")
# print(Car.fuel_type())
# print(Car.total_car)
#  print(my_car.full_Name())
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))



    




















