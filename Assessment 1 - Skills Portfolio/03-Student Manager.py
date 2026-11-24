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
for row in records:
    students.append({
        "id": row[0],
        "name": row[1],
        "coursework": row[2] + row[3] + row[4],
        "examscore": row[5],
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

def describe(students):
    percent = percentage(students)
    lines = [
        f"Student Number: {students['id']}",
        f"Student Name: {students['name']}",
        f"Total Coursework Mark: {students['coursework']}",
        f"Exam: {students['exam']}",
        f"Overall Percentage: {percent:.1f}%",
        f"Student Grade: {grade(percent)}",
    ]
    return "\n".join(lines) + "\n"



    





mainmenu = tk.Frame(root, width=1080, height=720, bg="#2F2F94")
title = tk.Label(mainmenu, text="The Library's Student Records", font =("arial", 25), fg="white")
title.place(relx=0.5, rely=0.1, anchor="center")
textarea = (mainmenu,)
mainmenu.place(x=0, y=0)








root.mainloop()