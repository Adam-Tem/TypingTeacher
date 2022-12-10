import tkinter as tk
import string
import random
from TypingFunctions import *

fingers_to_keys = {"L Pinky":["q", "a", "z"], "L Ring": ["s","w","x"], 
    "L Middle": ["e", "d", "c"], "L Index": ["r", "t", "f", "v", "g", "b"],
    "R Index": ["y", "u", "h", "j", "n", "m"], "R Middle": ["i", "k"],
    "R Ring": ["o", "l"], "R Pinky": ["p"]}

def generateRandomChar(event):
    streak = int(lbl_streak["text"][-1])
    if(event.char == curr_letter["text"]):
        old_letter.set(current_letter.get())
        current_letter.set(new_letter.get())
        curr_val = current_letter.get()
        new_letter.set(random.choice(string.ascii_lowercase))

        for finger, keys in fingers_to_keys.items():
            if curr_val in keys:
                finger_to_use.config(text=finger)
                if finger[0] == "L":
                    finger_to_use.config(fg="#dea8ff")
                else:
                    finger_to_use.config(fg="#e63c3c")
        prior_letter.config(text=old_letter.get())
        curr_letter.config(text=current_letter.get())
        next_letter.config(text=new_letter.get())
        lbl_streak.config(text="Streak: " + str(streak + 1))
    else:
        lbl_streak.config(text="0")

window = tk.Tk()

title = tk.Label(text="Typing Teacher", fg="black", bg="#8eb5f5", font=("Arial", 20))
title.pack(fill=tk.BOTH,expand=True)

lbl_streak = tk.Label(text = "Streak: 0", height = 1, font = 14)
lbl_streak.pack(fill=tk.BOTH,expand=True)

old_letter = tk.StringVar()
old_letter.set("...")
current_letter = tk.StringVar()
current_letter.set("a")
new_letter = tk.StringVar()
new_letter.set("b")

letters_frame = tk.Frame(master=window)

prior_letter = tk.Label(letters_frame, text=old_letter.get(), fg="#b5b5b5", bg="black", font=("Times", 20))
curr_letter = tk.Label(letters_frame, text=current_letter.get(), fg="white", bg="black", font=("Times", 40))
next_letter = tk.Label(letters_frame, text=new_letter.get(), fg="#b5b5b5", bg="black", font=("Times", 20))

letters_frame.pack(fill=tk.BOTH, expand=True)
prior_letter.pack(fill=tk.BOTH,expand=True, side=tk.LEFT)
curr_letter.pack(fill=tk.BOTH,expand=True, side=tk.LEFT)
next_letter.pack(fill=tk.BOTH,expand=True, side=tk.LEFT)

finger_to_use = tk.Label( text="L Pinky", fg="#dea8ff", bg="black", font=("Helvetica", 15))
finger_to_use.pack(fill=tk.BOTH,expand=True)

window.bind('<KeyPress>', generateRandomChar)

window.geometry("500x500")
window.mainloop()