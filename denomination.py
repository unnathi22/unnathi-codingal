from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title("denomination")
root.configure(bg="green")
root.geometry("400x400")
upload=Image.open("tally.png")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
lbl=Label(root,image=image,bg="red")
lbl.place(x=180,y=20)
lbl1=Label(root,text="hey welcome to denomination calculation",bg="pink")
lbl1.place(relx=0.5,rely=340,anchor=CENTER)
def message():
    message=messagebox.showinfo("alert !, do you wanna calculate the denominations? ")
    if message=="ok":
        topwin()
button1=Button(root,text="lets get started",command=message,bg="brown",fg="black")
button1.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.title("denomination calculation")
    top.configure(bg="lavender")
    top.geometry("600x350+50+50")
    label=Label(root,text="enter total amount",bg="pink")
    entry=Entry(top)
    lbl=Label(root,text="here are the number or notes",bg="pink")
    l1=Label(top,text="2000",bg="red")
    l2=Label(top,text="500",bg="red")
    l3=Label(top,text="100",bg="red")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculator():
        try:
            amount = int(entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(
        top,text="calculate",command=calculator,bg="green",fg="white")
    lbl.place(x=230,y=50)
    entry.place(x=200,y=80)
    button1.place(x=240,y=120)
    lbl.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=260)
    ll3.place(x=180,y=230)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    top.mainloop()
root.mainloop()
