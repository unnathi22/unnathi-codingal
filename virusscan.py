from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("window")
root.geometry("400x400")
def message():
    messagebox.showwarning("alert!","virus detected")
button=Button(root,text="scan for virus",command=message)
button.place(relx=0.5,rely=0.5,anchor="center")
root.mainloop()