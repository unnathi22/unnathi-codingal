
import tkinter as tk  
import random
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("350x300")
player_score = 0
computer_score = 0
options = ["Rock", "Paper", "Scissors"]
def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    choice_label.config(text=f"You chose {player_choice} vs Computer's {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {player_score} | Computer: {computer_score}")
title = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
title.pack()
btn_frame = tk.Frame(window)
btn_frame.pack()
tk.Button(btn_frame, text="Rock", width=8, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=8, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=8, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)
choice_label = tk.Label(window, text="Make a move to start!", font=("Arial", 11))
choice_label.pack()

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack()

score_label = tk.Label(window, text="Score - You: 0 /Computer: 0", font=("Arial", 11))
score_label.pack()
window.mainloop()
