from tkinter import *
from PIL import Image, ImageTk
from action import Action
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech

def get_audio():
    return speech_to_text()

def User_send():
    send = entry1.get()
    bot = Action(send)  # Assuming Action is a function
    text.insert(END, "Me --> " + send + "\n")
    
    if bot is not None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
        text_to_speech(bot)
    else:
        text.insert(END, "Bot <-- I didn't understand that.\n")

    if bot == "ok sir":
        root.destroy()

def ask():
    ask_val = get_audio()

    if ask_val is None or ask_val == "":
        text.insert(END, "Audio not recognized.\n")
        return

    bot_val = Action(ask_val)
    text.insert(END, "Me --> " + ask_val + "\n")

    if bot_val is not None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
        text_to_speech(bot_val)
    else:
        text.insert(END, "Bot <-- I didn't understand that.\n")

    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")

def welcome_user():
    welcome_message = "Welcome! I am Navi, your voice assistant. How can I help you today?"
    text_to_speech(welcome_message)
    text.insert(END, "Bot <-- " + welcome_message + "\n")


root = Tk()
root.title("NAVI")
root.geometry("1300x750")
root.resizable(False, False)
root.config(bg="#6F8FAF")

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised", bg="#6f8faf")
frame.grid(row=0, column=1, padx=55, pady=10)

text_label = Label(frame, text="NAVI", font=("comic sans ms", 20, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=30, pady=10)

# Ensure the path to the image is correct
img = ImageTk.PhotoImage(Image.open("boy2.png"))  # Update path if necessary
img_label = Label(frame, image=img)
img_label.grid(row=1, column=0, pady=20)

text = Text(root, font=('courier 10 bold'), bg="#356696")
text.grid(row=2, column=0)
text.place(x=600, y=50, width=600, height=650)

entry1 = Entry(root, justify=CENTER)
entry1.place(x=100, y=400, width=350, height=120)

btn1 = Button(root, text="ASK", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
btn1.place(x=70, y=575)

btn2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=User_send)
btn2.place(x=400, y=575)

btn3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete_text)
btn3.place(x=225, y=575)

welcome_user()
root.mainloop()
