medical_cause=input("tell the cause x or y:")
attend=int(input("enter your attendence:"))
if medical_cause=="y":
    print("you are allowed!")
else:
    if attend >=75:
        print("you are allowed !")
    else:
        print("u are not allowed !!")
