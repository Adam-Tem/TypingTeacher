def generateRandomChar(event, lbl_streak, new_letter, letter_display):
    streak = int(lbl_streak["text"])
    if(event.char == letter_display["text"]):
        print("match")
        new_letter.set(random.choice(string.ascii_lowercase))
        letter_display.config(text=new_letter.get())
        lbl_streak.config(text=str(streak + 1))
    else:
        lbl_streak.config(text="0")