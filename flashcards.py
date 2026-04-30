class flashcards:
    def __init(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        self.word +'('+self.meaning+')'
flash=[]
while(True):
    word=input("enter you word here:")
    meaning=input("enter the word meaning here:")
    flash.append(flashcards(word,meaning))
    option=int(input("0 is to stop the program and 1 is to kepp going so enter your choice here:"))
    if option==0:
        print("program stopped")
        break
for i in flash:
    print(i)



