number=(input("enter the digit"))
if len(number)>=4:
    mid=len(number)//2
    prod=int(number[mid-1])*int(number[mid])
    print(prod)
else:
    print("its not a 4 or more than 4 digit number")