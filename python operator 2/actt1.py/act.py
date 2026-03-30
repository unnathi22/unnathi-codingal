try:
    age=int(input("enter you age:"))
    if age%2==0:
        print("age is even..")
except:
    print("invalid!!")
    if ValueError:
        print("invalid input...please enter a valid integer age")
    else:
        print("something went wrong....")
finally:
    print("program excecuted successfully")