class roman_numbers:
    def convert(self,num):
        values=[(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        result = ""  # Our empty bag to hold the letters

        for value, symbol in values:
            while num >= value:
                result += symbol
                num -= value
        return result
converter=roman_numbers()
userinput=int(input("enter the number you wanna know the roman value of:"))
romanconversion=converter.convert(userinput)
print(f"your roman value for the number you entered is:",romanconversion)