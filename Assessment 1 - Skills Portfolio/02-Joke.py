import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("jokes!")
root.geometry("1080x720")
root.resizable(False, False)



def showframe(frame):
    frame.tkraise()

with open("randomJokes.txt", "r", encoding="utf-8") as file:
    joke = [line for line in file.readlines() if "?" in line]

def nextjoke():
    global punchline_text
    line1, line2 = random.choice(joke).split("?", 1)
    jokelabel.config(text=line1 + "?")
    punchline_text = line2.strip()
    nextbutton.place(relx=0.5, rely=0.7, anchor="center")

def dependancybutton():
    global punchline_text
    jokelabel.config(text="")
    nextbutton.place_forget()

def showJoke():
        messagebox.showinfo("Explanation ng joke", punchline_text, parent=root)

def quit():
    root.destroy()

mainmenu = tk.Frame(root, width="1080", height="720", bg="lightblue")
menulabel1 = tk.Label(mainmenu, text="The JOKER's Circus!", font=("Arial", 24,), fg="black")
menulabel1.place(relx=0.5, rely=0.2, anchor="center")
startbutton = tk.Button(mainmenu, text="START!", font=("Arial", 24), fg="Black", command=lambda: (showframe(jokepage)))
startbutton.place(relx=0.5, rely=0.5, anchor="center")
backbutton = tk.Button(mainmenu, text="Quit", font=("Arial", 20), fg="black", width=20, command=quit)
backbutton.place(relx=0.5, rely=0.8, anchor="center")
mainmenu.place(x=0, y=0)

jokepage = tk.Frame(root, width="1080", height="720", bg="lightblue")
jokelabel = tk.Label(jokepage, text="", font=("Arial", 20), fg="black")
jokelabel.place(relx=0.5, rely=0.2, anchor="center")
displayjoke = tk.Button(jokepage, text="Alexa, Tell me a joke", font=("Arial", 20), fg="black", width=20, command=nextjoke)
displayjoke.place(relx=0.3, rely=0.5, anchor="center")
dispalypunchline = tk.Button(jokepage, text="Show me the punch line!", font=("Arial", 20), fg="black", width=20, command=showJoke)
dispalypunchline.place(relx=0.7, rely=0.5, anchor="center")
nextbutton = tk.Button(jokepage, text="Next Joke", font=("Arial", 20), fg="black", width=20, command=dependancybutton)
backbutton = tk.Button(jokepage, text="Back", font=("Arial", 20), fg="black", width=20, command=lambda: (showframe(mainmenu)))
backbutton.place(relx=0.5, rely=0.8, anchor="center")

jokepage.place(x=0, y=0)

mainmenu.tkraise()
root.mainloop()