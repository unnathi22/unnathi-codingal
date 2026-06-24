from tkinter import *
root = Tk()
root.geometry("250x200")
entry1 = Entry(root)
entry1.pack()
entry2 = Entry(root)
entry2.pack()
result_label = Label(root, text="Product: ")
result_label.pack()
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    result_label.config(text=f"Product: {product}")

btn = Button(root, text="Multiply", command=lambda: calculate())
btn.pack(pady=5)
root.mainloop()
