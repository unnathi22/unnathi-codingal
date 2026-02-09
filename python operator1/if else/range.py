n=int(input("enter the lower range:"))
m=int(input("enter the higher range:"))
for n in range(max(2,n),m+1):
    for i in range(2,n):
        if n %i==0:
            break
    else:
         print(n)
    