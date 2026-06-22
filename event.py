from tkinter import *
root=Tk()
root.title("event program")
root.geometry("400x300")
def handle_keypress(event):
    """print the character assosiated to the key pressed"""
    print(event.char)
root.bind("<Key>",handle_keypress)
def handle_click(event):
    print("the button was clicked")
button=Button(text="click me")
button.pack()
root.bind("<Button-1>",handle_click)
root.mainloop()
