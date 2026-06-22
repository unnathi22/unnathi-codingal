from tkinter import *
root=Tk()
root.title("login page")
root.geometry("400x400")
frame=Frame(master=root,height=200,width=360,bg="lightblue")
lbl1=Label(frame,text="enter your name",bg="pink",fg="white",width=12)
lbl2=Label(frame,text="enter your email",bg="pink",fg="white",width=12)
lbl3=Label(frame,text="password",bg="pink",fg="white",width=12)
name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")
def display():
    name=name_entry.get()
    greet="hello"+name
    message="congrats for the new acc"
    textbox.insert(END,greet)
    textbox.insert(END,message)
textbox=Text(bg="red",fg="white")


