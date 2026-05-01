class vehicle:
    def __init__(self,seating_capacity,name):
        self.seating_capacity=seating_capacity
        self.name=name
        totalfare=seating_capacity*100
        print("total fare of the ride is :",totalfare)
class bus(vehicle):
    maintenence=totalfare*0.1
obj=vehicle()
obj.fare(100,50)
obj.maintenence()

    