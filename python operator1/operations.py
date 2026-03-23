def add(p,q):
    return(p+q)
def sub(p,q):
    return(p-q)
def multiply(p,q):
    return(p*q)
def divide(p,q):
    return(p/q)
print("please select operation:")
print("a,add")
print("b,sub")
print("c,multiplication")
print("d,division")
num1=int(input("enter the first number:"))
num2=int(input("enter the second one:"))
choice=input("enter your choice:")
if choice=="a":
    print(num1,"+" ,num2,"=",add(num1,num2))
elif choice=="b":
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice=="c":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="d":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("invalid response")
    