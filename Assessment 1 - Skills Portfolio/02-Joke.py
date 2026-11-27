# CODELAB ASSESSMENT - Exercise 1 
# By Hanz Athane Iñigo G. Muñoz / Cyber Security Y2 G1
import random
import tkinter as tk

# the main variables
root = tk.Tk()
root.title("jokes!")
root.geometry("1080x720")
root.resizable(False, False)

# this function allows the frames to be switched between eachother, this function brings the frame getting called so it displays the frame to the user
def showframe(frame):
    frame.tkraise()

# this function is responsible for analyzing the data in the .txt file or "reading" it
with open("randomJokes.txt", "r", encoding="utf-8") as file: # reads the file
    joke = [line for line in file.readlines() if "?" in line] # loops through each line and only keeps ones with "?", and each kept line is one joke w/ the question and punchline in the same line
    punchline_text="" # stores the punchline of the text in screen, starting empty to make room for a joke

# this function runs when the displayjoke button is clicked 
def jokeGenerator():
    if punchline_text == "": # only displays when a joke is NOT shown, so clicking the button again doesnt replace the joke 
        nextjoke()

# picks a random joke and shows the joke and punchline to show for the other functions
def nextjoke():
    global punchline_text # global lets the function configure the text outside of it
    line1, line2 = random.choice(joke).split("?", 1) # picks one joke line then splits it, line 1= is the joke, and line2 is the punchlibe
    jokelabel.config(text=line1 + "?") # shows the joke
    punchline_text = line2.strip() # saves the punchline
    punchlinelabel.config(text="") # hides the punchline until the user wills it 
    nextbutton.place(relx=0.5, rely=0.7, anchor="center") #"next joke" button

# this function clears and resets everything when no joke was displayed
def dependancybutton():
    global punchline_text
    punchline_text="" 
    jokelabel.config(text="") # clears the joke
    punchlinelabel.config(text="") # clears the punchline
    nextbutton.place_forget() # hides the next joke button

# this function runs when the show punchline button is clicked, showing the punchline
def showJoke():
    punchlinelabel.config(text=punchline_text)

# quits the program
def quit():
    root.destroy()

# clears the joke and redirects the user back to the main menu
def back():
    dependancybutton()
    showframe(mainmenu)

# main menu frame, this is the frame that shows when the user first runs the program
mainmenu = tk.Frame(root, width="1080", height="720", bg="lightblue")
menulabel1 = tk.Label(mainmenu, text="The JOKER's Circus!", font=("Arial", 24,), fg="black")
menulabel1.place(relx=0.5, rely=0.2, anchor="center")
startbutton = tk.Button(mainmenu, text="START!", font=("Arial", 24), fg="Black", command=lambda: (showframe(jokepage)))
startbutton.place(relx=0.5, rely=0.5, anchor="center")
backbutton = tk.Button(mainmenu, text="Quit", font=("Arial", 20), fg="black", width=20, command=quit)
backbutton.place(relx=0.5, rely=0.8, anchor="center")
mainmenu.place(x=0, y=0)

# a frame used to display all the jokes (the main frame basically)
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

mainmenu.tkraise() # <-- makes the main menu the first thing that shows when the program is ran
root.mainloop() # absolute necessity, keeps the window open