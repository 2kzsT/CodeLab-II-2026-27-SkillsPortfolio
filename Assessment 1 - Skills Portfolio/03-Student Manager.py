import tkinter as tk
from tkinter import messagebox
import json
import os 

root = tk.Tk()
root.title("Student Manager")
root.resizable(False, False)
root.geometry("1080x720")
root.config(bg="#2F2F94")

JSON_FILE = "studentMarks.json"
TXT_FILE = "studentMarks.txt"

with open("studentMarks.json", "r", encoding="utf-8") as file:
    records = json.load(file)

students = []
for subject in records:
    students.append({
        "id": subject[0],
        "name": subject[1],
        "coursework": subject[2] + subject[3] + subject[4],
        "examscore": subject[5],
    })

def percentage(students):
    return (students["coursework"] + students["examscore"]) / 160 * 100

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




mainmenu = tk.Frame(root, width=1080, height=720, bg="#2F2F94")
title = tk.Label(mainmenu, text="The Library's Student Records", font =("arial", 25), fg="white")
title.place(relx=0.5, rely=0.1, anchor="center")
whitearea = tk.Text(mainmenu, bg="#FFFFFF", state=tk.DISABLED)
whitearea.place (relx=0.5, rely=0.6, anchor="center", width= 800, height=500)
view_all = tk.Button(mainmenu, text="View all Students", command=show_allstudents)
view_all.place(relx=0.2, rely=0.2, anchor="center")
mainmenu.place(x=0, y=0)








root.mainloop()