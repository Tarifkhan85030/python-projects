
from tkinter import *
from PIL import Image, ImageTk
import random

# main window
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("1000x368")
root.configure(background="#3b19b6")

# load images for player choices
rock_img = ImageTk.PhotoImage(Image.open("rockman.png"))
paper_img = ImageTk.PhotoImage(Image.open("paperman.png"))
scissor_img = ImageTk.PhotoImage(Image.open("secssorman.png").rotate(-90))

# load images for computer choices
com_rock_img = ImageTk.PhotoImage(Image.open("rock.jpg").rotate(90))
com_paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").rotate(90))
com_scissor_img = ImageTk.PhotoImage(Image.open("secssor.jpg").rotate(90))

# insert images in window
user_label = Label(root, image=scissor_img, bg="#3b19b6")
com_label = Label(root, image=com_scissor_img, bg="#3b19b6")

user_label.grid(row=1, column=0)
com_label.grid(row=1, column=4)

# scores
player_score = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computer_score = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
player_score.grid(row=1, column=1)
computer_score.grid(row=1, column=3)

# indicators
user_indicator = Label(root, font=50, text="User", bg="#3b19b6", fg="white")
user_indicator.grid(row=0, column=1)
com_indicator = Label(root, font=50, text="Computer", bg="#3b19b6", fg="white")
com_indicator.grid(row=0, column=3)

# messages
msg = Label(root, font=50, bg="#9b59b6", fg="white", text="Start Playing!")
msg.grid(row=3, column=2)

# function to update choices and determine the winner
def update_choice(user_choice):
    # update user choice image
    if user_choice == "rock":
        user_label.configure(image=rock_img)
    elif user_choice == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    # generate computer choice
    choices = ["rock", "paper", "scissor"]
    com_choice = random.choice(choices)
    if com_choice == "rock":
        com_label.configure(image=com_rock_img)
    elif com_choice == "paper":
        com_label.configure(image=com_paper_img)
    else:
        com_label.configure(image=com_scissor_img)

    # determine winner
    if user_choice == com_choice:
        msg['text'] = "It's a Tie!"
    elif (user_choice == "rock" and com_choice == "scissor") or \
         (user_choice == "paper" and com_choice == "rock") or \
         (user_choice == "scissor" and com_choice == "paper"):
        msg['text'] = "You Win!"
        player_score['text'] = int(player_score['text']) + 1
    else:
        msg['text'] = "You Lose!"
        computer_score['text'] = int(computer_score['text']) + 1


 
# buttons
rock_btn = Button(root, width=20, height=2, text="ROCK", bg="#ff3e4d", fg="white", command=lambda: update_choice("rock"))
rock_btn.grid(row=2, column=1)

paper_btn = Button(root, width=20, height=2, text="PAPER", bg="#fad02e", fg="white", command=lambda: update_choice("paper"))
paper_btn.grid(row=2, column=2)

scissor_btn = Button(root, width=20, height=2, text="SCISSOR", bg="#0abde3", fg="white", command=lambda: update_choice("scissor"))
scissor_btn.grid(row=2, column=3)

root.mainloop()


