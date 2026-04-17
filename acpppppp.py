import random

n=random.randint(1,100)
print("guess a number bw 1 to 100:")
for i in range(6):
    try:
        g=int(input("enter the num"))
        if g==n:
            print("correct!")
            break
        if g>=n:
            print("its higher!")
        else:
            print("its lower")
    except:
        print("invalid")

    