from tkinter import *
root=Tk()
root.title("interest calculator")
root.geometry("400x500")
def calculator():
    try:
     principle=float(entry_principle.get())
     time=float(entry_time.get())
     rateofinterest=float(entry_rateofinterest.get())
     interest=(principle*time*rateofinterest)/100
     label_result.config(text=f"Interest: {interest}")
    except ValueError:
       label_result.config(text="invalid response")

Label(root, text="Principal Amount:", font=("Arial", 11)).pack(pady=5)
entry_principle = Entry(root, font=("Arial", 11))
entry_principle.pack(pady=5)
Label(root, text="Time Period (Years):", font=("Arial", 11)).pack(pady=5)
entry_time = Entry(root, font=("Arial", 11))
entry_time.pack(pady=5)
Label(root, text="Rate of Interest (%):", font=("Arial", 11)).pack(pady=5)
entry_rateofinterest = Entry(root, font=("Arial", 11))
entry_rateofinterest.pack(pady=5)
btn_calculate = Button(root, text="Calculate", command=calculator, bg="lightblue", font=("Arial", 11, "bold"))
btn_calculate.pack(pady=20)
label_result = Label(root, text="Interest: 0.00", font=("Arial", 14, "bold"), fg="green")
label_result.pack(pady=10)
root.mainloop()