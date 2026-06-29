from tkinter import *

root = Tk()
root.title("Password Strength Checker")
root.geometry("400x550")
root.configure(bg="green")

def check_password():
    password = entry_password.get()
    has_length = len(password) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-_=+[{]}|;:',.<>/?`~"
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    total= sum([has_length, has_upper, has_lower, has_digit, has_special])

    # 5. Determine progress bar dimensions and text readouts
    if total <= 2:
        lbl_strength.config(text="Strength: Weak ", fg="red")
        color = "blue"
        width = 100
    elif total <= 4:
        lbl_strength.config(text="Strength: Medium ", fg="yellow")
        color = "yellow"
        width = 220
    else:
        lbl_strength.config(text="Strength: Strong ", fg="green")
        color ="green"
        width = 33

def update_checklist(label, conditionstrue):
    if conditionstrue:
        label.config(fg="green")  
    else:
        label.config(fg="red")
Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="blue", fg="blue").pack()
entry_password = Entry(root, font=("Arial", 14), show="*", width=25, bd=2, relief="raised")
entry_password.pack()
lbl_strength = Label(root, text="Enter a password", font=("Arial", 12, "bold"), bg="green", fg="green")
lbl_strength.pack()
frame_check = LabelFrame(root, text=" Requirements ", font=("Arial", 10, "bold"), bg="blue", fg="blue", padx=20, pady=15)
frame_check.pack(pady=15, padx=30)
lbl_cond_len = Label(frame_check, text=" Minimum 8 characters", font=("Arial", 11), bg="blue", fg="white", anchor="center")
lbl_cond_len.pack( pady=2)

lbl_cond_upper = Label(frame_check, text=" At least one uppercase letter (A-Z)", font=("Arial", 11), bg="blue", fg="blue", anchor="center")
lbl_cond_upper.pack(pady=2)

lbl_cond_lower = Label(frame_check, text=" At least one lowercase letter (a-z)", font=("Arial", 11), bg="blue", fg="blue", anchor="center")
lbl_cond_lower.pack(fill="x", pady=2)

lbl_cond_digit = Label(frame_check, text=" At least one digit (0-9)", font=("Arial", 11), bg="green", fg="green", anchor="center")
lbl_cond_digit.pack(pady=2)

lbl_cond_special = Label(frame_check, text=" At least one special character", font=("Arial", 11), bg="red", fg="red", anchor="center")
lbl_cond_special.pack(pady=2)

root.mainloop()
