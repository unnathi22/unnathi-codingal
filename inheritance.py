class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(vehicle):
    pass
schoolbus=bus("school volvo",200,12)
print("name of the bus is:",schoolbus.name,"max speed is:",schoolbus.max_speed,"mileage is:",schoolbus.mileage)