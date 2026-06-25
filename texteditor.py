from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("codingal's text editor")
window.geometry("400x400")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
def open_file():
    filename=askopenfilename(filetypes=[("Text Files","*.txt","allfiles","*.*")])
    if not filename:
        return
    text_edit.delete(1.0,END)
    with open(filename,"r")as input_file:
        text=input_file.read()
        text_edit.insert(END,text)
        input_file.close()
    window.title(f"codingal's text editor{filename}")
def save_file():
    filename=asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt","All Files","*.*")])
    
    if not filename:
        return
    with open(filename,"w")as output_file:
        text=text_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"codingal's text editor{filename}")
text_edit=Text(window)
fr_button=Frame(window,relief=RAISED,bd=2)
btn_open=Button(fr_button,text="open",command=open_file)
btn_save=Button(fr_button,text="save as...",command=save_file)
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)
fr_button.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=0,column=1,sticky="nsew")
window.mainloop()
        
    


