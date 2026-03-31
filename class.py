def hotelnights():
    hotelnights*140
    return
def planeridecost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 222
    elif city=="Pittsburgh":
        return 220
    elif city=="Los Angeles":
        return 475
    
def rentalcarcost(days):
    if days>=7:
        return 40*days-50
    elif days>3:
        return 40*days-20
    else:
        return 40*days
def tripcost(city,days,spendingmoney):
    return rentalcarcost(days)+hotelnights(days)+planeridecost(city)+spendingmoney
print("cost of car rental:",rentalcarcost(5))
print("cost of plane ride:"planeridecost("Los Angeles"))
print("cost of hotel room:",hotelnights(7))
print("your total cost cost is :",tripcost("Los Angeles",7,500))
print(tripcost("Tampa",6,500))
    




        
    
def tripcost(city,days,spendingmoney):
    


# 4) Define a function `trip_cost(city, days, spending_money)` to calculate total trip cost:
#    a) Add rental car cost for `days`.
#    b) Add hotel cost for `days`.
#    c) Add plane ride cost for `city`.
#    d) Add extra `spending_money`.
#    e) Return the total trip cost.

# 5) Call `rental_car_cost(5)` and print the car rental cost.

# 6) Call `plane_ride_cost("Los Angeles")` and print the plane ride cost.

# 7) Call `hotel_cost(7)` and print the hotel room cost.

# 8) Call `trip_cost("Los Angeles", 7, 500)` and print the total trip cost.

# 9) Call `trip_cost("Tampa", 6, 500)` and print the total trip cost for Tampa.