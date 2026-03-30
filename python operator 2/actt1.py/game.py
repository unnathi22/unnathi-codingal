import random
while True:
    useraction=input("enter your choice bw rock,papers or scissors: ")
    possibleactions=["rock","paper","scissors"]
    computeraction=random.choice(possibleactions)
    print("useraction=",useraction)
    print("computeraction=",computeraction)
    if useraction==computeraction:
        print("its a tie")
    elif useraction=="rock":
        if computeraction=="scissors":
            print("you won")
        else:
            print("you lost!")
    elif useraction=="paper":
        if computeraction=="rock":
            print("you lost!")
        else:
            print("you won!")
    elif useraction=="scissors":
        if computeraction=="paper":
            print("you won!")
        else:
            print("you lost!")
    ask=input("do you wanna play again !?:")
    if ask!='y':
        print("bye!")
        break
        



