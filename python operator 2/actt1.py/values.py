try:
    num1,num2=eval(input("enter the numbers separated by a comma"))
    result=num1/num2
    print("the result is:",result)
except ZeroDivisionError:
    print("its a zero division error!!")
except SyntaxError:
    print("its a syntax error write your answer with commas!!correct format: 1,2,3")
except:
    print("wrong respose!")
else:
    print("no exceptions!!")
finally:
    print("this will excecute no matter what!")