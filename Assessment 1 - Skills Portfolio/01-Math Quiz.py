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
attempts = 0

# this function allows the frames to be switched between eachother
def showframe(frame):
    frame.tkraise()

# This function allows the questions to be generated, it randomizes it between 1-9 for now (easy), will implement moderate and advanced later on
def generateQuestion():
    global questionLabel, attempts
    attempts = 0
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
    global scoreLabel, attempts
    if questionNumber.get() > 10 :
        return
    global resultLabel
    if resultLabel:
        resultLabel.destroy()

    if str(answer.get()) == givenAnswer.get():
        if attempts == 0:
            score.set(score.get() + 10)
        else:
            score.set(score.get() + 5)
        resultLabel = tk.Label(easy, text="Correct", font=("arial, 20"), fg="green")
        resultLabel.place(relx=0.5, rely=0.6, anchor="center")
        scoreLabel = tk.Label(easy, text=f"Score : {score.get()}", font=("arial, 20"), fg="black")
        scoreLabel.place(relx=0.5, rely=0.7, anchor="center")
    else:
        if attempts == 0:
            attempts = 1
            givenAnswer.set("")
            resultLabel = tk.Label(easy, text="WRONG! try again", font=("arial", 20), fg="red")
            resultLabel.place(relx=0.5, rely=0.6, anchor="center")
            return
        resultLabel = tk.Label(easy, text="WRONG!", font=("arial", 20), fg="red")
        resultLabel.place(relx=0.5, rely=0.6, anchor="center")
    givenAnswer.set("")
    if questionNumber.get() == 10:
        scoreLabel.destroy()
        scoreLabel = tk.Label(easy, text=f"Final score: {score.get()}", font=("arial, 20"), fg="black")
        scoreLabel.place(relx=0.5, rely=0.7, anchor="center")
        questionNumber.set(11)
    else: generateQuestion()

# a function for restart, will be used soon when 5pts is implemented and all the difficulties are done
def Restart():
    global scoreLabel, resultLabel
    scoreLabel.destroy()
    resultLabel.config(text="Result", fg="black")
    score.set(0)
    questionNumber.set(0)
    givenAnswer.set("")
    generateQuestion()
    scoreLabel = tk.Label(easy, text=f"Score: {score.get()}", font=("arial", 20), fg="black")
    scoreLabel.place(relx=0.5, rely=0.7, anchor="center")
    showframe(menu)

#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER

def generateQuestion2():
    global questionLabel2, attempts
    attempts = 0
    questionNumber.set(questionNumber.get() + 1)
    number1 = random.randint(10, 99)
    number2= random.randint(10, 99)
    operator = random.choice(['+', '-'])
    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))
    if questionLabel2:
        questionLabel2.destroy()
    questionLabel2 = tk.Label(moderate, text=f"Question : {question.get()}", font=("arial", 20))
    questionLabel2.place(relx=0.5, rely=0.3, anchor="center")

# This function tells whether the answer given is correct or not, giving 10 points each correct answer (add second chance 5pts later on)
def checkAnswer2():
    global scoreLabel2, attempts
    if questionNumber.get() > 10 :
        return
    global resultLabel2
    if resultLabel2:
        resultLabel2.destroy()

    if str(answer.get()) == givenAnswer.get():
        if attempts == 0:
            score.set(score.get() + 10)
        else:
            score.set(score.get() + 5)
        resultLabel2 = tk.Label(moderate, text="Correct", font=("arial, 20"), fg="green")
        resultLabel2.place(relx=0.5, rely=0.6, anchor="center")
        scoreLabel2 = tk.Label(moderate, text=f"Score : {score.get()}", font=("arial, 20"), fg="black")
        scoreLabel2.place(relx=0.5, rely=0.7, anchor="center")
    else:
        if attempts == 0:
            attempts = 1
            givenAnswer.set("")
            resultLabel2 = tk.Label(moderate, text="WRONG! try again", font=("arial", 20), fg="red")
            resultLabel2.place(relx=0.5, rely=0.6, anchor="center")
            return
        resultLabel2 = tk.Label(moderate, text="WRONG!", font=("arial", 20), fg="red")
        resultLabel2.place(relx=0.5, rely=0.6, anchor="center")
    givenAnswer.set("")
    if questionNumber.get() == 10:
        scoreLabel2.destroy()
        scoreLabel2 = tk.Label(moderate, text=f"Final score: {score.get()}", font=("arial, 20"), fg="black")
        scoreLabel2.place(relx=0.5, rely=0.7, anchor="center")
        questionNumber.set(11)
    else: generateQuestion2()

# a function for restart, will be used soon when 5pts is implemented and all the difficulties are done
def Restart2():
    global scoreLabel2, resultLabel2
    scoreLabel2.destroy()
    resultLabel2.config(text="Result", fg="black")
    score.set(0)
    questionNumber.set(0)
    givenAnswer.set("")
    generateQuestion2()
    scoreLabel2 = tk.Label(moderate, text=f"Score: {score.get()}", font=("arial", 20), fg="black")
    scoreLabel2.place(relx=0.5, rely=0.7, anchor="center")
    showframe(menu)

#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER

def generateQuestion3():
    global questionLabel3, attempts
    attempts = 0
    questionNumber.set(questionNumber.get() + 1)
    number1 = random.randint(1000, 9999)
    number2= random.randint(1000, 9999)
    operator = random.choice(['+', '-'])
    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))
    if questionLabel3:
        questionLabel3.destroy()
    questionLabel3 = tk.Label(advanced, text=f"Question : {question.get()}", font=("arial", 20))
    questionLabel3.place(relx=0.5, rely=0.3, anchor="center")

# This function tells whether the answer given is correct or not, giving 10 points each correct answer (add second chance 5pts later on)
def checkAnswer3():
    global scoreLabel3, attempts
    if questionNumber.get() > 10 :
        return
    global resultLabel3
    if resultLabel3:
        resultLabel3.destroy()

    if str(answer.get()) == givenAnswer.get():
        if attempts == 0:
            score.set(score.get() + 10)
        else:
            score.set(score.get() + 5)
        resultLabel3 = tk.Label(advanced, text="Correct", font=("arial, 20"), fg="green")
        resultLabel3.place(relx=0.5, rely=0.6, anchor="center")
        scoreLabel3 = tk.Label(advanced, text=f"Score : {score.get()}", font=("arial, 20"), fg="black")
        scoreLabel3.place(relx=0.5, rely=0.7, anchor="center")
    else:
        if attempts == 0:
            attempts = 1
            givenAnswer.set("")
            resultLabel3 = tk.Label(advanced, text="WRONG! try again", font=("arial", 20), fg="red")
            resultLabel3.place(relx=0.5, rely=0.6, anchor="center")
            return
        resultLabel3 = tk.Label(advanced, text="WRONG!", font=("arial", 20), fg="red")
        resultLabel3.place(relx=0.5, rely=0.6, anchor="center")
    givenAnswer.set("")
    if questionNumber.get() == 10:
        scoreLabel3.destroy()
        scoreLabel3 = tk.Label(advanced, text=f"Final score: {score.get()}", font=("arial, 20"), fg="black")
        scoreLabel3.place(relx=0.5, rely=0.7, anchor="center")
        questionNumber.set(11)
    else: generateQuestion3()

# a function for restart, will be used soon when 5pts is implemented and all the difficulties are done
def Restart3():
    global scoreLabel3, resultLabel3
    scoreLabel3.destroy()
    resultLabel3.config(text="Result", fg="black")
    score.set(0)
    questionNumber.set(0)
    givenAnswer.set("")
    generateQuestion3()
    scoreLabel3 = tk.Label(easy, text=f"Score: {score.get()}", font=("arial", 20), fg="black")
    scoreLabel3.place(relx=0.5, rely=0.7, anchor="center")
    showframe(menu)


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
back_button1 = tk.Button(easy, text="Back", font=("Arial", 20,), fg="black", command=Restart)
back_button1.place(relx=0.5, rely=0.9, anchor="center")
easy.place(x=0, y=0)

#moderate frame
moderate = tk.Frame(root, width=1080, height=720, bg="yellow")
headingLabel = tk.Label(moderate, text="Moderate Level", font=("arial", 25), fg="Black")
headingLabel.place(relx=0.5, rely=0.1, anchor="center")
questionLabel2 = tk.Label(moderate, text=question.get(), font=("arial", 25), fg="Black")
questionLabel2.place(relx=0.5, rely= 0.3, anchor="center")
answerEntry = tk.Entry(moderate, textvariable=givenAnswer, font=("arial", 25), width=25)
answerEntry.place(relx=0.5, rely=0.4, anchor="center")
submitButton = tk.Button(moderate, text="Submit", fg="yellow", bg="grey", font=("arial", 15), width=25, command=checkAnswer2)
submitButton.place(relx=0.5, rely=0.5, anchor="center")
resultLabel2 = tk.Label(moderate, text="Result", font=("arial", 20), fg="black")
resultLabel2.place(relx=0.5, rely=0.6, anchor="center")
scoreLabel2 = tk.Label(moderate, text=f"Score : {score.get()}", font=("arial", 20), fg="black")
scoreLabel2.place(relx=0.5, rely=0.7, anchor="center")
back_button1 = tk.Button(moderate, text="Back", font=("Arial", 20,), fg="black", command=Restart2)
back_button1.place(relx=0.5, rely=0.9, anchor="center")
moderate.place(x=0, y=0)

#advanced frame
advanced = tk.Frame(root, width=1080, height=720, bg="red")
headingLabel = tk.Label(advanced, text="Advanced Level", font=("arial", 25), fg="Black")
headingLabel.place(relx=0.5, rely=0.1, anchor="center")
questionLabel3 = tk.Label(advanced, text=question.get(), font=("arial", 25), fg="Black")
questionLabel3.place(relx=0.5, rely= 0.3, anchor="center")
answerEntry = tk.Entry(advanced, textvariable=givenAnswer, font=("arial", 25), width=25)
answerEntry.place(relx=0.5, rely=0.4, anchor="center")
submitButton = tk.Button(advanced, text="Submit", fg="yellow", bg="grey", font=("arial", 15), width=25, command=checkAnswer3)
submitButton.place(relx=0.5, rely=0.5, anchor="center")
resultLabel3 = tk.Label(advanced, text="Result", font=("arial", 20), fg="black")
resultLabel3.place(relx=0.5, rely=0.6, anchor="center")
scoreLabel3 = tk.Label(advanced, text=f"Score : {score.get()}", font=("arial", 20), fg="black")
scoreLabel3.place(relx=0.5, rely=0.7, anchor="center")
back_button1 = tk.Button(advanced, text="Back", font=("Arial", 20,), fg="black", command=Restart3)
back_button1.place(relx=0.5, rely=0.9, anchor="center")
advanced.place(x=0, y=0)

generateQuestion()
generateQuestion2()
generateQuestion3()
menu.tkraise() # <- this allows the menu to be the first frame that the program is showing
root.mainloop()