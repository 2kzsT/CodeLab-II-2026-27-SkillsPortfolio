import tkinter as tk
from tkinter import messagebox
import json
import os 

#the main items
root = tk.Tk()
root.title("Student Manager")
root.resizable(False, False)
root.geometry("1080x720")

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

# runs at the start of every add/delete/update, so the records stay updated
def refresh_students():
    students.clear()
    for subject in records:
        students.append({
            "id": subject[0],
            "name": subject[1],
            "coursework": subject[2] + subject[3] + subject[4],
            "examscore": subject[5],
        })

# this function saves the records being added/deleted/updated
def save_records():
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file)

refresh_students()

# this function is used for finding the student number in the records
def find(student_id):
    for i in range(len(records)):
        if records[i][0] == student_id:
            return i
    return None

# makes a label and entry box for every item it is in
def create_entries(window, labels):
    entries = []
    for text in labels:
        create_entries_label = tk.Label(window, text=text)
        create_entries_label.pack(pady=(8, 0))
        create_entry = tk.Entry(window)
        create_entry.pack()
        entries.append(create_entry)
    return entries

# this function turns the entry boxes into one record, but none if the data isn't valid
def get_record(entries):
    try:
        record = [entries[0].get().strip(), entries[1].get().strip(),
                  int(entries[2].get()), int(entries[3].get()),
                  int(entries[4].get()), int(entries[5].get())]
    except ValueError:
        return None
    id_yes = record[0].isdigit() and 1000 <= int(record[0]) <= 9999
    marks_yes = all(0 <= m <= 20 for m in record[2:5]) and 0 <= record[5] <= 100
    if id_yes and marks_yes and record[1] != "":
        return record
    return None

FORM_LABELS = [
    "Student Number (1000-9999):", "Student Name:",
    "Coursework 1 (out of 20):",
    "Coursework 2 (out of 20):",
    "Coursework 3 (out of 20):",
    "Exam (out of 100):"
]

# function used to add students
def show_add():
    add_menu = tk.Toplevel(root)
    add_menu.title("Add Student")
    add_menu.geometry("400x350")
    add_menu.resizable(False, False)
    entries = create_entries(add_menu, FORM_LABELS)

# dependancy for the function show_add, this section includes the actual contents such as messageboxes and required functions
    def add():
        record = get_record(entries)
        if record is None:
            messagebox.showerror("Error", "Please complete the information", parent=add_menu)
        elif find(record[0]) is not None:
            messagebox.showerror("Error", "The student record's number already exists", parent=add_menu)
        else:
            records.append(record)
            save_records()
            refresh_students()
            show("STUDENT ADDED:\n\n" + library(students[-1]))
            add_menu.destroy()

    tk.Button(add_menu, text="Add Student", command=add).pack(pady=20)

# function used to delete students in the records
def show_delete():
    delete_menu = tk.Toplevel(root)
    delete_menu.title("Delete Student")
    delete_menu.geometry("400x350")
    delete_menu.resizable(False, False)
    tk.Label(delete_menu, text="Enter the student number to delete:").pack(pady=(20, 5))
    id_entry = tk.Entry(delete_menu)
    id_entry.pack()

# dependancy for the function show_delete, includes all the required code to make the command work
    def delete():
        i = find(id_entry.get().strip())
        if i is None:
            messagebox.showerror("Error", "Student is not found", parent=delete_menu)
        elif messagebox.askyesno("Confirm", "Delete " + records[i][1] + "?", parent=delete_menu):
            records.pop(i)
            save_records()
            refresh_students()
            show("Student deleted")
            delete_menu.destroy()

    tk.Button(delete_menu, text="Delete Student", command=delete).pack(pady=20)

# function used to update students in the records
def show_update():
    update_menu = tk.Toplevel(root)
    update_menu.title("Update Student")
    update_menu.geometry("400x425")
    update_menu.resizable(False, False)
    tk.Label(update_menu, text="Enter the number of the student to update, \n type their new details in").pack(pady=(10, 0))
    entries = create_entries(update_menu, FORM_LABELS)

# dependancy for the function show_update, contains the required code to update the students in the database
    def update():
        record = get_record(entries)
        if record is None:
            messagebox.showerror("Error", "Please complete the information", parent=update_menu)
            return
        i = find(record[0])
        if i is None:
            messagebox.showerror("Error", "Student is not found", parent=update_menu)
        else:
            records[i] = record
            save_records()
            refresh_students()
            show("STUDENT UPDATED:\n\n" + library(students[i]))
            update_menu.destroy()

    tk.Button(update_menu, text="Update Student", command=update).pack(pady=20)

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

# puts the text into the white area (or in this case, black)
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
        for s in students:
            if s["id"] == student_searched:
                show(library(s))
                individualmenu.destroy()
                return
        result_label.config(text="Student is Not Found")

    search_button = tk.Button(individualmenu, text="Search", command=search)
    search_button.place(relx=0.5, rely=0.3, anchor="center")

#These functions are used for sorting the HIGHEST and LOWEST scored students, along with a system that organizes it alphabetically
# highest scored students
def highest_score():
    top_student = max(students, key=percentage)
    show("STUDENT WITH HIGHEST MARK:\n\n" + library(top_student))

# lowest scored students
def lowest_score():
    bottom_student = min(students, key=percentage)
    show("STUDENT WITH LOWEST MARK:\n\n" + library(bottom_student))

# alphabetical order
def alphabetical_score():
    message = "ALPHABETICAL ORDER (A-Z):\n\n"
    for student in sorted(students, key=lambda x: x["name"]):
        message += library(student) + "\n"
    show(message)

# A sort menu, it is a toplevel that sorts based on the button clicked:the highest/lowest scored students, and the alphabetical order
def show_sort():
    sort_menu = tk.Toplevel(mainmenu)
    sort_menu.title("Sort Tab")
    sort_menu.geometry("400x350")
    sort_menu.resizable(False, False)

    sort_title = tk.Label(sort_menu, text="Sort the Data:", font=("Arial", 12))
    sort_title.place(relx=0.5, rely=0.1, anchor="center")

# a system that makes it so that the popup is destroyed whenever the user clicks on a button
    def choose(action):
        action()
        sort_menu.destroy() 

# all the buttons within the sort menu, placed in the functions itself for easier access
    view_alphabetical = tk.Button (sort_menu, text="View Alphabetical (A-Z)", command=lambda: choose(alphabetical_score))
    view_alphabetical.place(relx=0.5, rely=0.3, anchor="center")
    view_highest = tk.Button(sort_menu, text="View Highest", command=lambda: choose(highest_score))
    view_highest.place(relx=0.5, rely=0.5, anchor="center")
    view_lowest = tk.Button(sort_menu, text="View Lowest", command=lambda: choose(lowest_score))
    view_lowest.place(relx=0.5, rely=0.7, anchor="center")

# the actual app/software
mainmenu = tk.Frame(root, width=1080, height=720, bg="#202030")
title = tk.Label(mainmenu, text="The Library's Student Records", font =("arial", 25), fg="white", bg="#202030")
title.place(relx=0.5, rely=0.1, anchor="center")
whitearea = tk.Text(mainmenu, bg="#0C0C0C", fg="white", state=tk.DISABLED)
whitearea.place (relx=0.5, rely=0.6, anchor="center", width= 800, height=450)
view_all = tk.Button(mainmenu, text="View all Students", command=show_allstudents)
view_all.place(relx=0.2, rely=0.2, anchor="center")
individual = tk.Button(mainmenu, text="View Individual Students", command=show_individual)
individual.place(relx=0.4, rely=0.2, anchor="center")
sort_button = tk.Button(mainmenu, text="SORT", command=show_sort)
sort_button.place(relx=0.6, rely=0.2, anchor="center")
add_button = tk.Button(mainmenu, text="ADD", command=show_add)
add_button.place(relx=0.2, rely=0.9, anchor="center")
update_button = tk.Button (mainmenu, text="UPDATE", command=show_update)
update_button.place(relx=0.3, rely=0.9, anchor="center")
delete_button = tk.Button(mainmenu, text="DELETE", command=show_delete)
delete_button.place(relx=0.4, rely=0.9, anchor="center")
mainmenu.place(x=0, y=0)



root.mainloop()