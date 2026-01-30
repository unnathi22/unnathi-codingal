print("select your trasportation :")
print("1.BIKE")
print("2.CAR")
answer=input("enter your choice here:")
if answer=="BIKE":
    print("you have choosen the bike !")
    print("choose 1.motorcycle or 2.scooter")
    answer2=input("enter your trasport here :")
    if answer2=="motorcycle":
        print("you have choosen the motorcycle:")
    else:
        print("you have choosen the scooter !")
elif answer=="CAR":
    print("you have choosen the car !")
else:
    print("you have choosen something else !?")
    