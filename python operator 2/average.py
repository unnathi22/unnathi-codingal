a=int(input("enter the speed of A:"))
b=int(input("enter the speed of B:"))
c=int(input("enter the speed of C:"))
avg=(a+b+c)/3
print(avg)
if avg>a and avg>b and avg>c:
    print("%d is greater than %d,%d,%d"%(avg,a,b,c))
else:
    print("average is smaller than one of them")
    