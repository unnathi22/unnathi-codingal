import random
class fruitquiz:
    def __init__(self):
        self.fruits={"apple":"red","watermelon":"green","dragonfruit":"pink","orange":"orange","grapes":"green"}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("what is the colour of{}:".format(fruit))
            userinput=input()
            if (userinput.lower()==color):
                print("correct!")
            else:
                print("oops ! wrong")
            option=int(input("enter 0 if you want to end the quiz or enter 1 to keep going!:"))
            if (option):
                break
print("welcome to the quiz")
ob=fruitquiz()
ob.quiz()