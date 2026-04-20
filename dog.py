class dogs:
    def _init_(self,breed,name,colour,age):
        self.breed=breed
        self.name=name
        self.colour=colour
        self.age=age
ob1=dogs("breed:german shepherd","name:charlie","colour:dark brown","age:2")
ob2=dogs("breed:doberman","name:leo","colour:black","age:1")
ob3=dogs("breed:husky","name:lego","colour:white","age:2")
print(f"{ob1.breed}")
print(f"{ob1.name}")
print(f"{ob1.colour}")
print(f"{ob1.age}")
print(f"{ob2.breed}")
print(f"{ob2.name}")
print(f"{ob1.colour}")
print(f"{ob2.age}")
print(f"{ob3.breed}")
print(f"{ob3.name}")
print(f"{ob3.colour}")
print(f"{ob3.age}")