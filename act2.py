def matchwords(words):
    ctr=0
    lst=[]
    for word in words:
        if len(words)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("list :",lst)
    print("number of words having first and last ones same: ")
    print(ctr)
matchwords(['abc','ccc','ddd','aaa'])


