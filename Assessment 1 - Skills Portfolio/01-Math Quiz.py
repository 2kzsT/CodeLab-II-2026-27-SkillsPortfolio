# CODELAB ASSESSMENT - Exercise 1 
# By Hanz Athane Iñigo G. Muñoz / Cyber Security Y2 G1
import random
import tkinter as tk
from tkinter import *
from random import randint, choice

# the main variables
root = tk.Tk()
root.title("Math Quiz")
root.geometry("1080x720")
root.resizable(False, False)

#these variables are shared by all 3 difficulties
# string/intvar are tkinter variables that are linked to widgets
question= tk.StringVar() # keeps track of the current question
answer = tk.StringVar() # this keeps track of the correct answer to the question
givenAnswer = tk.StringVar() # givenAnswer is the info typed into the entrybox
score = tk.IntVar() # keeps track of the user's socre
questionNumber = tk.IntVar() # identifies which number the user is on
attempts = 0 # the number of attempts

# this function allows the frames to be switched between eachother, this function brings the frame getting called so it displays the frame to the user
def showframe(frame):
    frame.tkraise()

# every single function is responsible for generating and resetting the question itself, it is also responible for managing/running when a button is clicked  
def starteasy():
    questionNumber.set(0)
    generateQuestion()
    showframe(easy)
    score.set(0)

def startmoderate():
    questionNumber.set(0)
    generateQuestion2()
    showframe(moderate)
    score.set(0)

def startadvanced():
    questionNumber.set(0)
    generateQuestion3()
    showframe(advanced)
    score.set(0)

# this allows the questions to be generated through numbers 1-9 so the questions are randomized between those numbers
def generateQuestion():
    global questionlabel, attempts # global controls other items outside of the function 
    attempts = 0
    questionNumber.set(questionNumber.get() + 1) # this allows it to move onto the next question number
    number1 = random.randint(1, 9) # randomly generates the first number of the question
    number2= random.randint(1, 9) # randomly generates the second number of the question
    operator = random.choice(['+', '-']) # picks addition and subtraction, * and / are not included due to them being too hard
    question.set(str(number1) + operator + str(number2)) # this is responsible for combining the two numbers along with the sign
    answer.set(eval(question.get()))
    if questionlabel:
        questionlabel.destroy()
    questionlabel = tk.Label(easy, text=f"Question : {question.get()}", font=("arial", 20))
    questionlabel.place(relx=0.5, rely=0.3, anchor="center")

# this function is respnsible for checking the user input, updating the score and checking the answer. This is also responsible for going to the next question
def checkAnswer():
    global scorelabel, attempts, restartbutton, backbutton
    if questionNumber.get() > 10 : # limits the questions to 10 questions only
        return
    global resultlabel
    if resultlabel:
        resultlabel.destroy()

# this compares the question to the correct answer
    if str(answer.get()) == givenAnswer.get():
        if attempts == 0:
            score.set(score.get() + 10)
        else:
            score.set(score.get() + 5) # points system, awarding 10 points for the first try and 5 for the second try
        resultlabel = tk.Label(easy, text="Correct", font=("arial, 20"), fg="green")
        resultlabel.place(relx=0.5, rely=0.6, anchor="center")
        scorelabel = tk.Label(easy, text=f"Score : {score.get()}", font=("arial, 20"), fg="black")
        scorelabel.place(relx=0.5, rely=0.7, anchor="center")
    else:
        if attempts == 0: # this enables the user to have a second chance at answering the question
            attempts = 1
            givenAnswer.set("")
            resultlabel = tk.Label(easy, text="WRONG! try again", font=("arial", 20), fg="red") # 2nd chance
            resultlabel.place(relx=0.5, rely=0.6, anchor="center")
            return
        resultlabel = tk.Label(easy, text="WRONG!", font=("arial", 20), fg="red") # completely wrong answer, the question moves onto the next and awards 0 points
        resultlabel.place(relx=0.5, rely=0.6, anchor="center")
    givenAnswer.set("")
    if questionNumber.get() == 10: # limits the questions to 10, and shows the user's final score along with a back button and a restart button
        scorelabel.destroy()
        scorelabel = tk.Label(easy, text=f"Final score: {score.get()}\n {rankings(score.get())}", font=("arial, 20"), fg="black")
        scorelabel.place(relx=0.5, rely=0.7, anchor="center")
        restartbutton = tk.Button(easy, text="Do you want to restart?", font=("arial", 20), fg="black", command=Restart)
        restartbutton.place(relx=0.5, rely=0.8, anchor="center")
        backbutton = tk.Button(easy, text="Back", font=("Arial", 20,), fg="black", command=Back)
        backbutton.place(relx=0.5, rely=0.9, anchor="center")
        questionNumber.set(11) # 11 means the questions are finished
    else: generateQuestion() # if its not 11, generate more questions to be answered

# This function runs when the restart button is clicked, and resets everything to be answered again
def Restart():
    global scorelabel, resultlabel, restartbutton
    scorelabel.destroy()
    resultlabel.config(text="Result", fg="black")
    score.set(0)
    questionNumber.set(0)
    givenAnswer.set("")
    generateQuestion() # makes the question again, to be answered a second time
    scorelabel = tk.Label(easy, text=f"Score: {score.get()}", font=("arial", 20), fg="black")
    scorelabel.place(relx=0.5, rely=0.7, anchor="center")
    restartbutton.destroy()
    backbutton.destroy() # all the .destroy() commands are to reset everything, such as scorelabel, restartbutton, and backbutton
    
def Back(): # this function depends on the restart function to run along with showing the main menu frame, basically doing the same purpose as the restart but taking you back to the menu
    Restart()
    showframe(menu)

#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER

# everything from this point onwards are basically the same function utilized in the easy difficulty, please refer to those explanations for information, thanks :)



#please refer to easy difficulty's functions :)
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

#please refer to easy difficulty's functions :)
def checkAnswer2():
    global scorelabel2, attempts, restartbutton2, backbutton
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
        backbutton = tk.Button(moderate, text="Back", font=("Arial", 20,), fg="black", command=Back2)
        backbutton.place(relx=0.5, rely=0.9, anchor="center")
        questionNumber.set(11)
    else: generateQuestion2()

#please refer to easy difficulty's functions :)
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
    backbutton.destroy()

#please refer to easy difficulty's functions :)
def Back2():
    Restart2()
    showframe(menu)

#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER#BORDER

#please refer to easy difficulty's functions :)
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

#please refer to easy difficulty's functions :)
def checkAnswer3():
    global scorelabel3, attempts, restartbutton3, backbutton
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
        backbutton = tk.Button(advanced, text="Back", font=("Arial", 20,), fg="black", command=Back3)
        backbutton.place(relx=0.5, rely=0.9, anchor="center")
        questionNumber.set(11)
    else: generateQuestion3()

#please refer to easy difficulty's functions :)
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
    backbutton.destroy()

#please refer to easy difficulty's functions :)
def Back3():
    Restart3()
    showframe(menu)

# takes the final score of the user and gives a rank based on the score, each with varying ranks
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

# simple main menu, with the title and a welcome message
menu = tk.Frame(root, width=1080, height=720, bg="lightblue")
menulabel1 = tk.Label(menu, text="THE Math Quiz", font=("Arial", 24,), fg="black", padx=20, pady=20)
menulabel1.place(relx=0.5, rely=0.1, anchor="center")
menulabel2 = tk.Label(menu, text="Hello, Welcome to the Infamous Math Quiz!", font=("Arial", 16,), fg="black")
menulabel2.place(relx=0.5, rely=0.28, anchor="center")
menulabel3 = tk.Label(menu, text="Please Select the Difficulty Level", font=("Arial", 14,), fg="black",)
menulabel3.place(relx=0.5, rely=0.38, anchor="center")
# buttons to direct to the different difficulties, each running a certain command based on the difficulty
easybutton = tk.Button(menu, text="Easy", font=("Arial", 20,), fg="black", command=starteasy)
easybutton.place(relx=0.25, rely=0.6, anchor="center")
moderatebutton = tk.Button(menu, text="Moderate", font=("Arial", 20,), fg="black", command=startmoderate)
moderatebutton.place(relx=0.5, rely=0.6, anchor="center")
advancedbutton = tk.Button(menu, text="Advanced", font=("Arial", 20,), fg="black", command=startadvanced)
advancedbutton.place(relx=0.75, rely=0.6, anchor="center")
menu.place(x=0, y=0)

#easy frame, includes the heading, question itself, an entrybox, a submit button, results, and a score button
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
easy.place(x=0, y=0)

#moderate frame, includes the heading, question itself, an entrybox, a submit button, results, and a score button
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
moderate.place(x=0, y=0)

#advanced frame, includes the heading, question itself, an entrybox, a submit button, results, and a score button
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
advanced.place(x=0, y=0)

menu.tkraise() # <- this allows the menu to be the first frame that the program is showing
root.mainloop() # absolute necessity, keeps the window open

# thank you for your time :)