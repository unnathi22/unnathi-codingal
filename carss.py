class cars:
    def __init__(self,brand,maxspeed,fueltype):
        self.brand=brand
        self.maxspeed=maxspeed
        self.fueltype=fueltype
    def info(self):
        print("brand:",self.brand)
        print("maxspeed is:",self.maxspeed)
        print("fueltype is :",self.fueltype)
ob1=cars("BMW",200,"diesel")
ob2=cars("ferrari",190,"diesel")
ob1.info()
ob2.info()