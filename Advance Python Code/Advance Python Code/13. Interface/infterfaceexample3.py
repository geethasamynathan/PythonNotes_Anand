from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def max_speed(self):
        pass

    def start_engine(self):
        return "Engine started."

class Car(Vehicle):
    def max_speed(self):
        return '200'

class Bike(Vehicle):
    def max_speed(self):
        return '100'
bik=Bike();
car = Car()

def drive(obj):
    class_str =str(type(obj))
    vehicle_name = class_str.split('.')[-1].split('>')[0] 
    vehicle_name+= obj.start_engine();   
    print(vehicle_name)
    vehicle_speed =vehicle_name 
    vehicle_speed+=obj.max_speed()
    print(vehicle_speed)
    
drive(bik)
drive(car)