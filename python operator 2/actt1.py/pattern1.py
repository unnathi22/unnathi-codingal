print("pyramid of stars *")
input=int(input("enter a digit:"))
for i in range(input):
    for j in range(i+1):
        print("*",end="")
    print()
 