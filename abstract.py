from abc import ABC, abstractmethod
class absmethod(ABC):
    def print(self,x):
        print("passed value is:",x)
    @abstractmethod
    def test(self):
        print("im inside absmethod")
class child(absmethod):
    def test(self):
        print("im inside the subclass")
c=child()
c.print(20)
c.test()


        