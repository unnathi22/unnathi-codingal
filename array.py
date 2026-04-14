import array as arr
array_num=arr.array('i',[1,2,3,4,5,6,7,3])
print(array_num)
num=int(input("enter a number to find:"))
print("the number of times your entered number has repeated:",
array_num.count(num))
array_num.reverse()
print("revered version of the array:",array_num)
