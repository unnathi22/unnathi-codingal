nums=[10,20,30,40,50,60]
target=int(input("enter the target:"))
seen={}
for i,n in enumerate(nums):
    if target-n in seen:
        print(seen[target-n],i)
        break
    seen[n]=i
    
    
