import random
import tkinter as tk

# the main items
root = tk.Tk()
root.title("jokes!")
root.geometry("1080x720")
root.resizable(False, False)

# function used to show which frame is being displayed
def showframe(frame):
    frame.tkraise()

# this function gathers all the data required to display the jokes
with open("randomJokes.txt", "r", encoding="utf-8") as file:
    joke = [line for line in file.readlines() if "?" in line]
    punchline_text=""

# the function used to display the joke being shown in the screen
def jokeGenerator():
    if punchline_text == "":
        nextjoke()

# this function changes the code into a random one selected from the .txt, repeating over and over
def nextjoke():
    global punchline_text
    line1, line2 = random.choice(joke).split("?", 1)
    jokelabel.config(text=line1 + "?")
    punchline_text = line2.strip()
    punchlinelabel.config(text="")
    nextbutton.place(relx=0.5, rely=0.7, anchor="center")

# this function is a dependancy button containing all the items for displayign the joke
def dependancybutton():
    global punchline_text
    punchline_text=""
    jokelabel.config(text="")
    punchlinelabel.config(text="")
    nextbutton.place_forget()

# button used to show the punchline of the joke
def showJoke():
    punchlinelabel.config(text=punchline_text)

def quit():
    root.destroy()

def back():
    dependancybutton()
    showframe(mainmenu)

# main menu frame, used to display the first thing the user sees
mainmenu = tk.Frame(root, width="1080", height="720", bg="lightblue")
menulabel1 = tk.Label(mainmenu, text="The JOKER's Circus!", font=("Arial", 24,), fg="black")
menulabel1.place(relx=0.5, rely=0.2, anchor="center")
startbutton = tk.Button(mainmenu, text="START!", font=("Arial", 24), fg="Black", command=lambda: (showframe(jokepage)))
startbutton.place(relx=0.5, rely=0.5, anchor="center")
backbutton = tk.Button(mainmenu, text="Quit", font=("Arial", 20), fg="black", width=20, command=quit)
backbutton.place(relx=0.5, rely=0.8, anchor="center")
mainmenu.place(x=0, y=0)

# another frame used to display the jokes 
jokepage = tk.Frame(root, width="1080", height="720", bg="lightblue")
jokelabel = tk.Label(jokepage, text="", font=("Arial", 20), fg="black")
jokelabel.place(relx=0.5, rely=0.2, anchor="center")
punchlinelabel = tk.Label(jokepage, text="", font=("Arial", 20), fg="black")
punchlinelabel.place(relx=0.5, rely=0.3, anchor="center")
displayjoke = tk.Button(jokepage, text="Alexa, Tell me a joke", font=("Arial", 20), fg="black", width=20, command=jokeGenerator)
displayjoke.place(relx=0.3, rely=0.5, anchor="center")
dispalypunchline = tk.Button(jokepage, text="Show me the punch line!", font=("Arial", 20), fg="black", width=20, command=showJoke)
dispalypunchline.place(relx=0.7, rely=0.5, anchor="center")
nextbutton = tk.Button(jokepage, text="Next Joke", font=("Arial", 20), fg="black", width=20, command=dependancybutton)
backbutton = tk.Button(jokepage, text="Back", font=("Arial", 20), fg="black", width=20, command=back)
backbutton.place(relx=0.5, rely=0.8, anchor="center")
jokepage.place(x=0, y=0)

mainmenu.tkraise()
root.mainloop()