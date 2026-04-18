list1=[1,2,3,4,5,2345,667788,67,67]
print(list1)
odd=[x for x in list1 if x%2!=0]
print("the odd numbers are:",odd)
list2=['passionfruit','dragonfruit','strawberry','pineapple']
uppercase=list(map(str.upper,list2))
print(uppercase)



