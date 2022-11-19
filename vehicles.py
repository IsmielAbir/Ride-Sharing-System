from abc import ABC, abstractmethod
from time import sleep

class Vehicle(ABC):
    speed = {
        'car': 30,
        'bike':50,
        'cng': 15 
    }
    def __init__(self, vehicle_type, license_plate,  rate, driver) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.status = 'available'
        self.license_plate = license_plate
        self.speed = self.speed[vehicle_type]
        
        
    @abstractmethod
    def start_driving(self):
        pass
    
    @abstractmethod
    def trip_finish(self):
        pass
        
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
           
    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'started')
        distance  = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f'driving: {self.license_plate} current position: {i} of {distance}\n')
        self.trip_finish()
        
        
    
    def trip_finish(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'Completed trip')
    
    
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
           
    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'started')
        distance  = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f'driving: {self.license_plate} current position: {i} of {distance}\n')
        self.trip_finish()
    
    def trip_finish(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'Completed trip')
    
    
    
class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
           
    def start_driving(self, start, destination):
        self.status = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'started')
        distance  = abs(start - destination)
        for i in range(0, distance):
            sleep(0.5)
            print(f'driving: {self.license_plate} current position: {i} of {distance}\n')
        self.trip_finish()
    
    def trip_finish(self):
        self.status = 'available'
        print(self.vehicle_type, self.license_plate, 'Completed trip')
    