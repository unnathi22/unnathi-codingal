test_dict={'codingal':3,'is':2,'the':3,'best':2,'for':2,'coding':6}
print(test_dict)
frequency=int(input("enter the number you want to find the frequency of :"))
res=0
for key in test_dict:
    if test_dict[key]==frequency:
        res=res+1
print(res)
        
