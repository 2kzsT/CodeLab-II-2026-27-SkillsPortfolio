import random
import tkinter as tk
from tkinter import *
from random import randint, choice

# the main items
root = tk.Tk()
root.title("Math Quiz")
root.geometry("1080x720")
root.resizable(False, False)
question= tk.StringVar()
answer = tk.StringVar()
givenAnswer = tk.StringVar()
score = tk.IntVar()
questionNumber = tk.IntVar()

# this function allows the frames to be switched between eachother
def showframe(frame):
    frame.tkraise()

# This function allows the questions to be generated, it randomizes it between 1-9 for now (easy), will implement moderate and advanced later on
def generateQuestion():
    global questionLabel
    questionNumber.set(questionNumber.get() + 1)
    number1 = random.randint(1, 9)
    number2= random.randint(1, 9)
    operator = random.choice(['+', '-'])
    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))

    if questionLabel:
        questionLabel.destroy()

    questionLabel = tk.Label(easy, text=f"Question : {question.get()}", font=("arial", 20))
    questionLabel.place(relx=0.5, rely=0.3, anchor="center")

# This function tells whether the answer given is correct or not, giving 10 points each correct answer (add second chance 5pts later on)
def checkAnswer():
    global scoreLabel
    if questionNumber.get() > 10 :
        return
    global resultLabel
    if resultLabel:
        resultLabel.destroy()

    if str(answer.get()) == givenAnswer.get():
        score.set(score.get() + 10)
        resultLabel = tk.Label(easy, text="Correct", font=("arial, 20"), fg="green")
        resultLabel.place(relx=0.5, rely=0.6, anchor="center")
        scoreLabel = tk.Label(easy, text=f"Score : {score.get()}", font=("arial, 20"), fg="black")
        scoreLabel.place(relx=0.5, rely=0.7, anchor="center")

    else:
        resultLabel = tk.Label(easy, text="Incorrect", font=("arial, 20"), fg="red")
        resultLabel.place(relx=0.5, rely=0.6, anchor="center")

    if questionNumber.get() == 10:
        scoreLabel.destroy()
        scoreLabel = tk.Label(easy, text=f"Final score: {score.get()}", font=("arial, 20"), fg="black")
        scoreLabel.place(relx=0.5, rely=0.7, anchor="center")

    else: generateQuestion()

# a function for restart, will be used soon when 5pts is implemented and all the difficulties are done
def Restart():
    global scoreLabel
    scoreLabel.destroy()

    score.set(0)
    questionNumber.set(0)
    generateQuestion()

    scoreLabel = tk.Label(easy, text=f"Score: {score.get()}", font=("arial", 20), fg="black")
    scoreLabel.place(relx=0.5, rely=0.7, anchor="center")


#USER INTERFACE

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
headingLabel = tk.Label(easy, text="Easy Level", font=("arial", 25), fg="Black")
headingLabel.place(relx=0.5, rely=0.1, anchor="center")
questionLabel = tk.Label(easy, text=question.get(), font=("arial", 25), fg="Black")
questionLabel.place(relx=0.5, rely= 0.3, anchor="center")
answerEntry = tk.Entry(easy, textvariable=givenAnswer, font=("arial", 25), width=25)
answerEntry.place(relx=0.5, rely=0.4, anchor="center")
submitButton = tk.Button(easy, text="Submit", fg="yellow", bg="grey", font=("arial", 15), width=25, command=checkAnswer)
submitButton.place(relx=0.5, rely=0.5, anchor="center")
resultLabel = tk.Label(easy, text="Result", font=("arial", 20), fg="black")
resultLabel.place(relx=0.5, rely=0.6, anchor="center")
scoreLabel = tk.Label(easy, text=f"Score : {score.get()}", font=("arial", 20), fg="black")
scoreLabel.place(relx=0.5, rely=0.7, anchor="center")
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

generateQuestion()
menu.tkraise() # <- this allows the menu to be the first frame that the program is showing
root.mainloop()