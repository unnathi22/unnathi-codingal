num=int(input("enter the number :"))
sum=0
pow=len(str(num))
temp=num
while temp>0:
    digit=num%temp
    sum+=digit **pow
    temp//=10
if num==sum:
    print(sum,"is an armsstrong number ")
else:
    print(sum,"is not an armsstrong number !")