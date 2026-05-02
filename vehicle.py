class vehicle:
    def __init__(self,name,seating_capacity):
        self.name=name
        self.seating_capacity=seating_capacity
    def fare(self):
        return self.seating_capacity*100
        
class bus(vehicle):
    def fare(self):
        normal_fare=super().fare()
        maintenence_charge=normal_fare*0.10
        final_fare=maintenence_charge+normal_fare
        return final_fare
ob1=bus("school bus",50)
print(f"final fare for :",ob1.name,"is",ob1.fare())