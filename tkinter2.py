from tkinter import *
from datetime import date
root=Tk()
root.title("tkinter window")
root.geometry("500x500")
lbl=Label(text="hey there!",fg="red",bg="blue",height=1,width=1)
name_lbl=Label(text="enter your full name:")
name_entry=Entry()
def display():
    name=name_entry.get()
    global message 
    message="welcome to the application \ntodays date"
    greet="hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="enter",command=display,height=2,bg="green",fg="pink",)
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()

# 10) Arrange all widgets in the window using `pack()`:
#     a) Pack the main label.
#     b) Pack the name label.
#     c) Pack the name entry box.
#     d) Pack the button.
#     e) Pack the text box.


# 11) Start the GUI event loop using `root.mainloop()`
#     so the window stays open and responds to user actions.
