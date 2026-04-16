num1=[1,2,3,4,5]
num2=[1,2,3,4,-3]
result=map(lambda x,y:x+y,num1,num2)
print(list(result))
def square(num):
    return(num*num)
square=map(square,num2)
print(list(square))