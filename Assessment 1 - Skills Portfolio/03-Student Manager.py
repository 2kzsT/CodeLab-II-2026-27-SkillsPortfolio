import tkinter as tk
from tkinter import messagebox
import json
import os 

#the main items
root = tk.Tk()
root.title("Student Manager")
root.resizable(False, False)
root.geometry("1080x720")
root.config(bg="#2F2F94")

# JSON_FILE is used to read the .json file so itll be accessible
JSON_FILE = "studentMarks.json"

#reads the .json
with open(JSON_FILE, "r", encoding="utf-8") as file:
    records = json.load(file)

#student's main data
students = []
for subject in records:
    students.append({
        "id": subject[0],
        "name": subject[1],
        "coursework": subject[2] + subject[3] + subject[4],
        "examscore": subject[5],
    })

# the grade for each student
def grade(percentage):
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

#this function handles all the necessary data for the student it is linked towards the student's main data
def library(student):
    percent = percentage(student)
    lines = [
        f"Student Number: {student['id']}",
        f"Student Name: {student['name']}",
        f"Total Coursework Mark: {student['coursework']}",
        f"Exam: {student['examscore']}",
        f"Overall Percentage: {percent:.1f}%",
        f"Student Grade: {grade(percent)}",
    ]
    return "\n".join(lines) + "\n"

#calculates the student's coursework with the exam score to figure out the overall %
def percentage(students):
    return (students["coursework"] + students["examscore"]) / 160 * 100

# simple show all students button for the whitearea
def show_allstudents():
    message = ""
    for student in students:
        message += library(student) + "\n"
    show(message)

def show(message):
    whitearea.config(state=tk.NORMAL)
    whitearea.delete("1.0", tk.END)
    whitearea.insert(tk.END, message)
    whitearea.config(state=tk.DISABLED)

#this function allows individual's data to be acquired through the "individual" button
def show_individual():
    individualmenu = tk.Toplevel(mainmenu)
    individualmenu.title("Individual Student Records")
    individualmenu.geometry("400x350")
    individualmenu.resizable(False, False)

    individual_label = tk.Label(individualmenu, text="Enter Student Number:")
    individual_label.place(relx=0.5, rely=0.1, anchor="center")
    enter_id = tk.Entry(individualmenu)
    enter_id.place(relx=0.5, rely=0.2, anchor="center")

    result_label = tk.Label(individualmenu, text="", justify=tk.LEFT, font=("Arial", 11))
    result_label.place(relx=0.5, rely=0.6, anchor="center")

# This allows the search function to work in the individuals
    def search():
        student_searched = enter_id.get().strip()
        message = "Student is Not Found"
        for s in students:
            if s["id"] == student_searched:
                message = library(s)
                break
        result_label.config(text=message)

    search_button = tk.Button(individualmenu, text="Search", command=search)
    search_button.place(relx=0.5, rely=0.3, anchor="center")



# the actual app/software
mainmenu = tk.Frame(root, width=1080, height=720, bg="#2F2F94")
title = tk.Label(mainmenu, text="The Library's Student Records", font =("arial", 25), fg="white")
title.place(relx=0.5, rely=0.1, anchor="center")
whitearea = tk.Text(mainmenu, bg="#FFFFFF", state=tk.DISABLED)
whitearea.place (relx=0.5, rely=0.6, anchor="center", width= 800, height=500)
view_all = tk.Button(mainmenu, text="View all Students", command=show_allstudents)
view_all.place(relx=0.2, rely=0.2, anchor="center")
individual = tk.Button(mainmenu, text="View Individual Students", command=show_individual)
individual.place(relx=0.4, rely=0.2, anchor="center")
mainmenu.place(x=0, y=0)



root.mainloop()