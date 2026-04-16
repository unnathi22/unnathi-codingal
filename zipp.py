list1=[100,20,30,30,-200]
list2=[20,30,40,50]
output=zip(list1,list2[::-1])
for x,y in output:
    print(x,y)

