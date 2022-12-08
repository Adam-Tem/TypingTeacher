import tkinter as tk
import string
import random


def onKeyPress(event):
    text.insert('end', 'You pressed %s\n' % (event.char, ))

def generateRandomChar(event):
    if(event.char == letter_display["text"]):
        print("match")
        new_letter.set(random.choice(string.ascii_letters))
        letter_display.config(text=new_letter.get()) 


window = tk.Tk()

title = tk.Label(
    text="Typing Teacher",
    fg="white",
    bg="black",
    height=4
)
title.pack(fill=tk.X)

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


text = tk.Text(window, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
window.bind('<KeyPress>', generateRandomChar)

window.geometry("500x500")
window.mainloop()