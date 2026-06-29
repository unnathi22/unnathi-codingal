from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("length converter")
root.geometry("400x300")
root.configure(bg="blue")
def converter():
    try:
        meters = float(entry_meters.get())
        centimeters = meters * 100
        label_result.config(
            text=f"{meters} m = {centimeters} cm", fg="green"
        )
    except ValueError:
        messagebox.showerror(
            "Invalid Input")
    label_title = Label(
    root,
    text="Length Converter",
    font=("Arial", 14, "bold"),
    bg="pink"
)
    label_title.pack()
input_frame = Frame(root, bg="green")
input_frame.pack()
entry_meters = Entry(
    input_frame, font=("Arial")
)
entry_meters.pack()
label_unit =Label(
    input_frame, text="Meters", font=("Arial"), bg="yellow"
)
label_unit.pack()
btn = Button(
    root,
    text="Convert",
    font=("Arial"),
    bg="green",
    command=converter)
btn.pack()
label_result =Label(
    root,
    text="Enter a value and click Convert",
    font=("Arial"),
    bg="black"
)
label_result.pack()
root.mainloop()

