costprice=float(input("enter the cost price of the object:"))
sellingprice=float(input("enter the selling price of the object:"))
if costprice<sellingprice:
    profit=sellingprice - costprice 
    print(profit)
else:
    print("its a loss!")
