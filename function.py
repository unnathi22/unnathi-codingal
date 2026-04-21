class string:
    def __init__(self):
        self.str=""
    def get_string(self):
        self.str=input("enter a string")
    def print_string(self):
        print(self.str.upper())
str1=string()
str1.get_string()
str1.print_string()
