#getting the number 
amount=input("please enter the desired number:")
amount=int(amount)
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print(note1)
print(note2)
print(note3)


