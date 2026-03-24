def factorial(x):
    """the recursive of the entered integer is :"""
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("the factorial of 1 is:",factorial(1))
print("the factorial of 3 is:",factorial(3))
print("the factorial of 5 is:",factorial(5))
      