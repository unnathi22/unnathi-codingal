start=int(input("enter the start no."))
end=int(input("enter the end no."))
squares=[]
for i in range(start,end+1):
    squares.append(i**2)
even=[]
odd=[]
for num in squares:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("all squares:",squares)
print("even squares:",even)
print("odd squares:",odd)

# 2) Create an empty list to store square values.

# 3) Use a loop from start to end (inclusive) to:
#    - find square using (i ** 2)
#    - store it in the list

# 4) Create two lists for:
#    - even squares
#    - odd squares

# 5) Traverse the square list and:
#    - if number % 2 == 0 → add to even list
#    - else → add to odd list

# 6) Print:
#    - all square values
#    - even squares
#    - odd squares