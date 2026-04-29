class vehicle:
    def __init__(self,seating_capacity,number):
        self.seating_capacity=seating_capacity
        self.number=number
        totalfare=seating_capacity*number
        print("total fare of the ride is :",totalfare)
    def maintenence(self,totalfare):
        self.totalfare=totalfare
        maintenence_charge=totalfare*0.1
        print("maintence charge will be:",maintenence_charge)
class bus(vehicle):
    def __init__(self,maintenence_charge,totalfare):
        super().__init__(maintenence_charge,totalfare)
obj=vehicle()
obj.fare(100,50)
obj.maintenence()
obj=bus()
    