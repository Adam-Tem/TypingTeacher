import tkinter as tk
import string
import random


def generateRandomChar(event):
    streak = int(lbl_streak["text"])
    if(event.char == letter_display["text"]):
        print("match")
        new_letter.set(random.choice(string.ascii_letters))
        letter_display.config(text=new_letter.get())
        lbl_streak.config(text=str(streak + 1))
    else:
        lbl_streak.config(text="0")


window = tk.Tk()

title = tk.Label(
    text="Typing Teacher",
    fg="white",
    bg="black",
    height=4
)
title.pack(fill=tk.X)

lbl_streak = tk.Label(
    text = "0",
)
lbl_streak.pack()

new_letter = tk.StringVar()
new_letter.set("A")

letter_display = tk.Label(
    text=new_letter.get(),
    fg="white",
    bg="black",
    height=4
)

letter_display.pack(fill=tk.X)

finger_to_use = tk.Label(
    text="Left index",
    fg="white",
    bg="black",
    height=4
)
finger_to_use.pack(fill=tk.X)

window.bind('<KeyPress>', generateRandomChar)

window.geometry("500x500")
window.mainloop()