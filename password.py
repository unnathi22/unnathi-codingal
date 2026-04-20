import random
alphabets="ABCDEFGHIJKLMNOPQRTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
numbers="123456789"
symbols="!@#$%^&*><|"
all_charac=alphabets+lowercase+numbers+symbols
password=''.join(random.choices(all_charac,k=12))
print("the strong password recommendation is:",password)