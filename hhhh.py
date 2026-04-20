class vehicle:
    def __init__(self,max_speed,mileage,colour):
        self.max_speed=max_speed
        self.mileage=mileage
        self.colour=colour
modelx=vehicle(300,12,"red")
modely=vehicle(120,20,"blue")
print("speed of modelx:",modelx.max_speed)
print("mileage of modelx:",modelx.mileage)
print("colour of modelx:",modelx.colour)
print("speed of modely:",modely.max_speed)
print("mileage of modely:",modely.mileage)
print("colour of modely:",modely.colour)
    