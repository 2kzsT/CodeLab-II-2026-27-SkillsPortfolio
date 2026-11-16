import random
import tkinter as tk

# the main items
root = tk.Tk()
root.title("Math Quiz")
root.geometry("1080x720")
root.resizable(False, False)

# this function allows the frames to be switched between eachother
def showframe(frame):
    frame.tkraise()

def randomInt():
    Easy = random.randomint(1, 9)
    Moderate = random.randomint(10, 99)
    Advanced = random.randomint(1000, 9999)

# simple menu, nothing too fancy
menu = tk.Frame(root, width=1080, height=720, bg="lightblue")
menulabel1 = tk.Label(menu, text="THE Math Quiz", font=("Arial", 24,), fg="black", padx=20, pady=20)
menulabel1.place(relx=0.5, rely=0.1, anchor="center")
menulabel2 = tk.Label(menu, text="Hello, Welcome to the Infamous Math Quiz!", font=("Arial", 16,), fg="black")
menulabel2.place(relx=0.5, rely=0.28, anchor="center")
menulabel3 = tk.Label(menu, text="Please Select the Difficulty Level", font=("Arial", 14,), fg="black",)
menulabel3.place(relx=0.5, rely=0.38, anchor="center")

# the buttons for the different difficulties
easybutton = tk.Button(menu, text="Easy", font=("Arial", 20,), fg="black", command=lambda: showframe(easy))
easybutton.place(relx=0.25, rely=0.6, anchor="center")
moderatebutton = tk.Button(menu, text="Moderate", font=("Arial", 20,), fg="black", command=lambda: showframe(moderate))
moderatebutton.place(relx=0.5, rely=0.6, anchor="center")
advancedbutton = tk.Button(menu, text="Advanced", font=("Arial", 20,), fg="black", command=lambda: showframe(advanced))
advancedbutton.place(relx=0.75, rely=0.6, anchor="center")
menu.place(x=0, y=0)

# the frames for different difficulties
easy = tk.Frame(root, width=1080, height=720, bg="green")
easywidget = tk.Entry(easy, font=("Arial", 20,), fg="black")
easywidget.place(relx=0.5, rely=0.5, anchor="center")
submit = tk.Button(easy, text="Submit", font=("Arial", 20,), fg="black")
submit.place(relx=0.5, rely=0.6, anchor="center")

back_button1 = tk.Button(easy, text="Back", font=("Arial", 20,), fg="black", command=lambda: showframe(menu))
back_button1.place(relx=0.5, rely=0.9, anchor="center")
easy.place(x=0, y=0)

#moderate frame
moderate = tk.Frame(root, width=1080, height=720, bg="yellow")
back_button1 = tk.Button(moderate, text="Back", font=("Arial", 20,), fg="black", command=lambda: showframe(menu))
back_button1.place(relx=0.5, rely=0.9, anchor="center")
moderate.place(x=0, y=0)

#advanced frame
advanced = tk.Frame(root, width=1080, height=720, bg="red")
back_button1 = tk.Button(advanced, text="Back", font=("Arial", 20,), fg="black", command=lambda: showframe(menu))
back_button1.place(relx=0.5, rely=0.9, anchor="center")
advanced.place(x=0, y=0)


menu.tkraise() # <- this allows the menu to be the first frame that the program is showing
root.mainloop()