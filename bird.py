class parrot:
    species="birds"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blue=parrot("bro",12)
red=parrot("bro2",2)
print(f"{blue.species}")
print(f"name is:{blue.name}")
print(f"age of blue is:{blue.age}")
print(f" :{red.species}")
print(f"name is{red.name}")
print(f"age of red is:{red.age}")