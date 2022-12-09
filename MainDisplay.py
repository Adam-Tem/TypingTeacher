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
    if(event.char == letter_display["text"]):
        new_val = random.choice(string.ascii_lowercase)
        new_letter.set(new_val)
        for finger, keys in fingers_to_keys.items():
            if new_val in keys:
                finger_to_use.config(text=finger)
        letter_display.config(text=new_letter.get())
        lbl_streak.config(text="Streak: " + str(streak + 1))
    else:
        lbl_streak.config(text="0")

window = tk.Tk()

title = tk.Label(text="Typing Teacher", fg="white", bg="#8eb5f5", font=("Arial", 20))
title.pack(fill=tk.BOTH, expand=1)

lbl_streak = tk.Label(text = "Streak: 0", height = 1, font = 14)
lbl_streak.pack(fill=tk.BOTH)

new_letter = tk.StringVar()
new_letter.set("a")

letter_display = tk.Label( text=new_letter.get(), fg="white", bg="black", font=("Times", 40))

letter_display.pack(fill=tk.BOTH, expand=1)

finger_to_use = tk.Label( text="L Pinky", fg="#d1d1d1", bg="black", font=("Arial", 15))
finger_to_use.pack(fill=tk.BOTH, expand=1)

window.bind('<KeyPress>', generateRandomChar)

window.geometry("500x500")
window.mainloop()