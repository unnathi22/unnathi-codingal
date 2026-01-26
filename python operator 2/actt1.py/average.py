marks1=82
marks2=45
marks3=88
marks4=77
marks5=70
tot=marks1+marks2+marks3+marks4+marks5
avg=tot/5
if avg>=90:
    print("very good scores!")
elif avg<90 and avg>=80:
    print("good score!")
elif avg<80 and avg>=60:
    print("try hard next time !!")
else:
    print("fail ! try hard")