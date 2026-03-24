def cube(num):
    return num*num*num
def by_three(num):
    if num %3==0:
        return cube(num)
    else:
        return False
by_three(3)
by_three(2) 
print(by_three(3))
print(by_three(2))