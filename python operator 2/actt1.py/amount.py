def total_amt(bill_amt,tip_amt):
    total=bill_amt*(1+0.01*tip_amt)
    total=round(total,2)
    print(f"total is:",total)
total_amt(150,60)