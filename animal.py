from abc import ABC
class animals(ABC):
    def move(self):
        pass
class human(animals):
    def move(self):
        print("i can walk talk and run")
class dog(animals):
    def move(self):
        print("i can bark")
class birds(animals):
    print("i can fly")
obj=human()
obj.move
obj1=dog()
obj1.move
obj2=birds()
obj2.move