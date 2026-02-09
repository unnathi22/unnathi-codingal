word=input("enter the word:")
charac=input("enter the character:")
i=0
count=0
while(i<len(word)):
    if word[i]==charac:
     count=count+1
    i=i+1
print("the occurance of the charcter in the",word,"is",count)