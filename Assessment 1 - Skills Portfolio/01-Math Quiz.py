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
    global questionlabel, attempts
    attempts = 0
    questionNumber.set(questionNumber.get() + 1)
    number1 = random.randint(1, 9)
    number2= random.randint(1, 9)
    operator = random.choice(['+', '-'])
    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))
    if questionlabel:
        questionlabel.destroy()
    questionlabel = tk.Label(easy, text=f"Question : {question.get()}", font=("arial", 20))
    questionlabel.place(relx=0.5, rely=0.3, anchor="center")

# This function tells whether the answer given is correct or not, giving 10 points each correct answer (add second chance 5pts later on)
def checkAnswer():
    global scorelabel, attempts, restartbutton
    if questionNumber.get() > 10 :
        return
    global resultlabel
    if resultlabel:
        resultlabel.destroy()

    if str(answer.get()) == givenAnswer.get():
        if attempts == 0:
            score.set(score.get() + 10)
        else:
            score.set(score.get() + 5)
        resultlabel = tk.Label(easy, text="Correct", font=("arial, 20"), fg="green")
        resultlabel.place(relx=0.5, rely=0.6, anchor="center")
        scorelabel = tk.Label(easy, text=f"Score : {score.get()}", font=("arial, 20"), fg="black")
        scorelabel.place(relx=0.5, rely=0.7, anchor="center")
    else:
        if attempts == 0:
            attempts = 1
            givenAnswer.set("")
            resultlabel = tk.Label(easy, text="WRONG! try again", font=("arial", 20), fg="red")
            resultlabel.place(relx=0.5, rely=0.6, anchor="center")
            return
        resultlabel = tk.Label(easy, text="WRONG!", font=("arial", 20), fg="red")
        resultlabel.place(relx=0.5, rely=0.6, anchor="center")
    givenAnswer.set("")
    if questionNumber.get() == 10:
        scorelabel.destroy()
        scorelabel = tk.Label(easy, text=f"Final score: {score.get()}\n {rankings(score.get())}", font=("arial, 20"), fg="black")
        scorelabel.place(relx=0.5, rely=0.7, anchor="center")
        restartbutton = tk.Button(easy, text="Do you want to restart?", font=("arial", 20), fg="black", command=Restart)
        restartbutton.place(relx=0.5, rely=0.8, anchor="center")
        questionNumber.set(11)
    else: generateQuestion()

# a function for restart, will be used soon when 5pts is implemented and all the difficulties are done
def Restart():
    global scorelabel, resultlabel, restartbutton
    scorelabel.destroy()
    resultlabel.config(text="Result", fg="black")
    score.set(0)
    questionNumber.set(0)
    givenAnswer.set("")
    generateQuestion()
    scorelabel = tk.Label(easy, text=f"Score: {score.get()}", font=("arial", 20), fg="black")
    scorelabel.place(relx=0.5, rely=0.7, anchor="center")
    restartbutton.destroy()
    
def Back():
    Restart()
    showframe(menu)

#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER

def generateQuestion2():
    global questionlabel2, attempts
    attempts = 0
    questionNumber.set(questionNumber.get() + 1)
    number1 = random.randint(10, 99)
    number2= random.randint(10, 99)
    operator = random.choice(['+', '-'])
    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))
    if questionlabel2:
        questionlabel2.destroy()
    questionlabel2 = tk.Label(moderate, text=f"Question : {question.get()}", font=("arial", 20))
    questionlabel2.place(relx=0.5, rely=0.3, anchor="center")

# This function tells whether the answer given is correct or not, giving 10 points each correct answer (add second chance 5pts later on)
def checkAnswer2():
    global scorelabel2, attempts, restartbutton2
    if questionNumber.get() > 10 :
        return
    global resultlabel2
    if resultlabel2:
        resultlabel2.destroy()

    if str(answer.get()) == givenAnswer.get():
        if attempts == 0:
            score.set(score.get() + 10)
        else:
            score.set(score.get() + 5)
        resultlabel2 = tk.Label(moderate, text="Correct", font=("arial, 20"), fg="green")
        resultlabel2.place(relx=0.5, rely=0.6, anchor="center")
        scorelabel2 = tk.Label(moderate, text=f"Score : {score.get()}", font=("arial, 20"), fg="black")
        scorelabel2.place(relx=0.5, rely=0.7, anchor="center")
    else:
        if attempts == 0:
            attempts = 1
            givenAnswer.set("")
            resultlabel2 = tk.Label(moderate, text="WRONG! try again", font=("arial", 20), fg="red")
            resultlabel2.place(relx=0.5, rely=0.6, anchor="center")
            return
        resultlabel2 = tk.Label(moderate, text="WRONG!", font=("arial", 20), fg="red")
        resultlabel2.place(relx=0.5, rely=0.6, anchor="center")
    givenAnswer.set("")
    if questionNumber.get() == 10:
        scorelabel2.destroy()
        scorelabel2 = tk.Label(moderate, text=f"Final score: {score.get()}\n {rankings(score.get())}", font=("arial, 20"), fg="black")
        scorelabel2.place(relx=0.5, rely=0.7, anchor="center")
        restartbutton2 = tk.Button(moderate, text="Do you want to restart?", font=("arial", 20), fg="black", command=Restart2)
        restartbutton2.place(relx=0.5, rely=0.8, anchor="center")
        questionNumber.set(11)
    else: generateQuestion2()

# a function for restart, will be used soon when 5pts is implemented and all the difficulties are done
def Restart2():
    global scorelabel2, resultlabel2, restartbutton2
    scorelabel2.destroy()
    resultlabel2.config(text="Result", fg="black")
    score.set(0)
    questionNumber.set(0)
    givenAnswer.set("")
    generateQuestion2()
    scorelabel2 = tk.Label(moderate, text=f"Score: {score.get()}", font=("arial", 20), fg="black")
    scorelabel2.place(relx=0.5, rely=0.7, anchor="center")
    restartbutton2.destroy()
    
def Back2():
    Restart2()
    showframe(menu)

#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER

def generateQuestion3():
    global questionlabel3, attempts
    attempts = 0
    questionNumber.set(questionNumber.get() + 1)
    number1 = random.randint(1000, 9999)
    number2= random.randint(1000, 9999)
    operator = random.choice(['+', '-'])
    question.set(str(number1) + operator + str(number2))
    answer.set(eval(question.get()))
    if questionlabel3:
        questionlabel3.destroy()
    questionlabel3 = tk.Label(advanced, text=f"Question : {question.get()}", font=("arial", 20))
    questionlabel3.place(relx=0.5, rely=0.3, anchor="center")

# This function tells whether the answer given is correct or not, giving 10 points each correct answer (add second chance 5pts later on)
def checkAnswer3():
    global scorelabel3, attempts, restartbutton3
    if questionNumber.get() > 10 :
        return
    global resultlabel3
    if resultlabel3:
        resultlabel3.destroy()

    if str(answer.get()) == givenAnswer.get():
        if attempts == 0:
            score.set(score.get() + 10)
        else:
            score.set(score.get() + 5)
        resultlabel3 = tk.Label(advanced, text="Correct", font=("arial, 20"), fg="green")
        resultlabel3.place(relx=0.5, rely=0.6, anchor="center")
        scorelabel3 = tk.Label(advanced, text=f"Score : {score.get()}", font=("arial, 20"), fg="black")
        scorelabel3.place(relx=0.5, rely=0.7, anchor="center")
    else:
        if attempts == 0:
            attempts = 1
            givenAnswer.set("")
            resultlabel3 = tk.Label(advanced, text="WRONG! try again", font=("arial", 20), fg="red")
            resultlabel3.place(relx=0.5, rely=0.6, anchor="center")
            return
        resultlabel3 = tk.Label(advanced, text="WRONG!", font=("arial", 20), fg="red")
        resultlabel3.place(relx=0.5, rely=0.6, anchor="center")
    givenAnswer.set("")
    if questionNumber.get() == 10:
        scorelabel3.destroy()
        scorelabel3 = tk.Label(advanced, text=f"Final score: {score.get()}\n {rankings(score.get())}", font=("arial, 20"), fg="black")
        scorelabel3.place(relx=0.5, rely=0.7, anchor="center")
        restartbutton3 = tk.Button(advanced, text="Do you want to restart?", font=("arial", 20), fg="black", command=Restart3)
        restartbutton3.place(relx=0.5, rely=0.8, anchor="center")
        questionNumber.set(11)
    else: generateQuestion3()

# a function for restart, will be used soon when 5pts is implemented and all the difficulties are done
def Restart3():
    global scorelabel3, resultlabel3
    scorelabel3.destroy()
    resultlabel3.config(text="Result", fg="black")
    score.set(0)
    questionNumber.set(0)
    givenAnswer.set("")
    generateQuestion3()
    scorelabel3 = tk.Label(advanced, text=f"Score: {score.get()}", font=("arial", 20), fg="black")
    scorelabel3.place(relx=0.5, rely=0.7, anchor="center")
    restartbutton3.destroy()

def Back3():
    Restart3()
    showframe(menu)

def rankings(finalscore):
    if finalscore == 100:
        return "Rank S (AMAZING WORK!)"
    elif finalscore >= 80:
        return "Rank A (Good job!)"
    elif finalscore >=50:
        return "Rank B (Not bad!)"
    elif finalscore >=40:
        return "Rank C (You could do better!)"
    else:
        return "Rank F (How do you even manage that?!)"


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
headinglabel = tk.Label(easy, text="Easy Level", font=("arial", 25), fg="Black")
headinglabel.place(relx=0.5, rely=0.1, anchor="center")
questionlabel = tk.Label(easy, text=question.get(), font=("arial", 25), fg="Black")
questionlabel.place(relx=0.5, rely= 0.3, anchor="center")
answerEntry = tk.Entry(easy, textvariable=givenAnswer, font=("arial", 25), width=25)
answerEntry.place(relx=0.5, rely=0.4, anchor="center")
submitButton = tk.Button(easy, text="Submit", fg="yellow", bg="grey", font=("arial", 15), width=25, command=checkAnswer)
submitButton.place(relx=0.5, rely=0.5, anchor="center")
resultlabel = tk.Label(easy, text="Result", font=("arial", 20), fg="black")
resultlabel.place(relx=0.5, rely=0.6, anchor="center")
scorelabel = tk.Label(easy, text=f"Score : {score.get()}", font=("arial", 20), fg="black")
scorelabel.place(relx=0.5, rely=0.7, anchor="center")
back_button1 = tk.Button(easy, text="Back", font=("Arial", 20,), fg="black", command=Back)
back_button1.place(relx=0.5, rely=0.9, anchor="center")
easy.place(x=0, y=0)

#moderate frame
moderate = tk.Frame(root, width=1080, height=720, bg="yellow")
headinglabel = tk.Label(moderate, text="Moderate Level", font=("arial", 25), fg="Black")
headinglabel.place(relx=0.5, rely=0.1, anchor="center")
questionlabel2 = tk.Label(moderate, text=question.get(), font=("arial", 25), fg="Black")
questionlabel2.place(relx=0.5, rely= 0.3, anchor="center")
answerEntry = tk.Entry(moderate, textvariable=givenAnswer, font=("arial", 25), width=25)
answerEntry.place(relx=0.5, rely=0.4, anchor="center")
submitButton = tk.Button(moderate, text="Submit", fg="yellow", bg="grey", font=("arial", 15), width=25, command=checkAnswer2)
submitButton.place(relx=0.5, rely=0.5, anchor="center")
resultlabel2 = tk.Label(moderate, text="Result", font=("arial", 20), fg="black")
resultlabel2.place(relx=0.5, rely=0.6, anchor="center")
scorelabel2 = tk.Label(moderate, text=f"Score : {score.get()}", font=("arial", 20), fg="black")
scorelabel2.place(relx=0.5, rely=0.7, anchor="center")
back_button1 = tk.Button(moderate, text="Back", font=("Arial", 20,), fg="black", command=Back2)
back_button1.place(relx=0.5, rely=0.9, anchor="center")
moderate.place(x=0, y=0)

#advanced frame
advanced = tk.Frame(root, width=1080, height=720, bg="red")
headinglabel = tk.Label(advanced, text="Advanced Level", font=("arial", 25), fg="Black")
headinglabel.place(relx=0.5, rely=0.1, anchor="center")
questionlabel3 = tk.Label(advanced, text=question.get(), font=("arial", 25), fg="Black")
questionlabel3.place(relx=0.5, rely= 0.3, anchor="center")
answerEntry = tk.Entry(advanced, textvariable=givenAnswer, font=("arial", 25), width=25)
answerEntry.place(relx=0.5, rely=0.4, anchor="center")
submitButton = tk.Button(advanced, text="Submit", fg="yellow", bg="grey", font=("arial", 15), width=25, command=checkAnswer3)
submitButton.place(relx=0.5, rely=0.5, anchor="center")
resultlabel3 = tk.Label(advanced, text="Result", font=("arial", 20), fg="black")
resultlabel3.place(relx=0.5, rely=0.6, anchor="center")
scorelabel3 = tk.Label(advanced, text=f"Score : {score.get()}", font=("arial", 20), fg="black")
scorelabel3.place(relx=0.5, rely=0.7, anchor="center")
back_button1 = tk.Button(advanced, text="Back", font=("Arial", 20,), fg="black", command=Back3)
back_button1.place(relx=0.5, rely=0.9, anchor="center")
advanced.place(x=0, y=0)

generateQuestion()
generateQuestion2()
generateQuestion3()
menu.tkraise() # <- this allows the menu to be the first frame that the program is showing
root.mainloop()