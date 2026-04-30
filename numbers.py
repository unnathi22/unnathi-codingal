class A:
    def __init__(self,a):
        self.a=a 
    def __lt__(self,other):
        if(self.a<other.a):
            return ("ob1<ob2")
        else:
            return("ob2<ob1")
    def __eq__(self,other):
        if(self.a==other.a):
            return("ob1=ob2")
        else:
            return("ob1 is not equal to ob2")
ob1=A(3)
ob2=A(6)
print(ob1<ob2)
print(ob1.a)
print(ob2.a)
ob3=A(3)
ob4=A(4)
print(ob1==ob2)