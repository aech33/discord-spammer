import time, pyautogui, keyboard
from tkinter import *

root = Tk()
repeats = IntVar()
msg = StringVar()

def spammer():
    begin = False
    end = False
    counter = 0

    f = open('msg.txt')
    lines = f.readlines()
    msg = lines[0]

    msgbox = pyautogui.locateCenterOnScreen('msgbox.jpg', confidence=0.5)
    pyautogui.click(msgbox)

    while end == False:
        if counter >= repeats.get():
            end = True
        else:
            time.sleep(0.65)
            keyboard.write(msg)
            counter += 1

Entry(root, textvariable = msg,bd = 3,font = ('',13)).grid(row=0, column=1)
Label(root, text = 'Message to spam: ',bg='#3A84FA',fg='white',font = ('',15)).grid(row=0, column=0)
Label(root, text = 'Times to spam it:  ',bg='#3A84FA',fg='white',font = ('',15)).grid(row=2, column=0)
Label(root, text = 'placeholder text cos im lazy',bg='#3A84FA',fg='#3A84FA',font = ('',5)).grid(row=1, column=0)
#probably don't go higher than a thousand unless you're crazy
Spinbox(root, from_= 0, to = 1000, textvariable = repeats,bd = 3,font = ('',13)).grid(row=2, column=1)
Label(root, text = 'more placeholder text cos im lazy',bg='#3A84FA',fg='#3A84FA',font = ('',5)).grid(row=3, column=0)
Button(root, text = 'Start Spammer',bg='#4E8EF5',fg='white',font = ('',14),pady=5,padx=5,command=spammer).grid(row=4, column=0)

root.geometry('410x150')
root.configure(bg='#3A84FA')
root.title('Discord Spammer')
root.mainloop()
