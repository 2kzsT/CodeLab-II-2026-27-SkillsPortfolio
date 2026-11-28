# CODELAB ASSESSMENT - Exercise 1 
# By Hanz Athane Iñigo G. Muñoz / Cyber Security Y2 G1
import tkinter as tk
from tkinter import messagebox
import json
import os 

#the main variables
root = tk.Tk()
root.title("Student Manager")
root.resizable(False, False)
root.geometry("1080x720")

# JSON_FILE is used to read the .json file so the data can be accessed
JSON_FILE = "studentMarks.json"

#reads the .json, and records is used as a listing system
with open(JSON_FILE, "r", encoding="utf-8") as file:
    records = json.load(file)

#students is a second records list, build from the records and uses each student as a dictionary
students = []

# This system is made for the students list/system, one dictionary per record, and the three coursework marks are added together for the total
for subject in records:
    students.append({
        "id": subject[0],
        "name": subject[1],
        "coursework": subject[2] + subject[3] + subject[4],
        "examscore": subject[5],
    })

# runs at the start of every add/delete/update, so the records stay updated
def refresh_students():
    students.clear() # empties the list, so there arent any mishaps with organizing the list
    for subject in records:
        students.append({
            "id": subject[0],
            "name": subject[1],
            "coursework": subject[2] + subject[3] + subject[4],
            "examscore": subject[5],
        })

# this function saves the records being added/deleted/updated into the .json file, "w" is used to write so that the adding/removing/updating may work
def save_records():
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file)

refresh_students()

# this function is used for finding the student number in the records, and returns the position of the student in the list (or None if there is no student)
def find(student_id):
    for i in range(len(records)):
        if records[i][0] == student_id:
            return i
    return None # outside the loop so it only goes ahead and run after EVERY single record has been checked

# makes a label and entry box for every item in the LABELS list
def create_entries(window, labels):
    entries = []
    for text in labels:
        create_entries_label = tk.Label(window, text=text)
        create_entries_label.pack(pady=(8, 0))
        create_entry = tk.Entry(window)
        create_entry.pack() # pack stacks each widget underneath the one before it
        entries.append(create_entry)
    return # returns the list of entry boxes so the functions can read what the user has inputted into the entrybox

# this function turns the entry boxes into one record, but None if the data isn't valid
def get_record(entries):
    try:
        record = [entries[0].get().strip(), entries[1].get().strip(), # reads every box, the student id and name can stay as text meanwhile the coursework and exams are integers
                  int(entries[2].get()), int(entries[3].get()),
                  int(entries[4].get()), int(entries[5].get())]
    except ValueError: # if a mark isnt a number it returns as invalid
        return None
    id_yes = record[0].isdigit() and 1000 <= int(record[0]) <= 9999 # student id is limited to 1000-9999
    marks_yes = all(0 <= m <= 20 for m in record[2:5]) and 0 <= record[5] <= 100 # courseworks are limited to 20 / meanwhile the exam is limited to 100
    if id_yes and marks_yes and record[1] != "": # it only accepts a valid input into name and marks, if it is empty then it returns the record
        return record
    return None

# this text is used for each entrybox above, both add and update utilizes this system
FORM_LABELS = [
    "Student Number (1000-9999):", "Student Name:",
    "Coursework 1 (out of 20):",
    "Coursework 2 (out of 20):",
    "Coursework 3 (out of 20):",
    "Exam (out of 100):"
]

# opens a Toplevel popup when you click add, allowing the user to add students to the record
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
            messagebox.showerror("Error", "Please complete the information", parent=add_menu) # if the details are invalid or not present, it shows an error
        elif find(record[0]) is not None: 
            messagebox.showerror("Error", "The student record's number already exists", parent=add_menu) # if a student already exists within the record it also shows an error
        else:
            records.append(record) # this adds a new student to the records
            save_records() # saves the records into the .json file
            refresh_students() # refreshes the student list 
            show("STUDENT ADDED:\n\n" + library(students[-1])) # shows the recently added student in the whitearea (plot twist its actually black)
            add_menu.destroy() # this closes the popup

    tk.Button(add_menu, text="Add Student", command=add).pack(pady=20)

# this functions opens a Toplevel popup when you click delete, allowing the user to delete a student record
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
        i = find(id_entry.get().strip()) # finds the position of the student number within the records
        if i is None:
            messagebox.showerror("Error", "Student is not found", parent=delete_menu) # if the student id is not found, it will return with an error
        elif messagebox.askyesno("Confirm", "Delete " + records[i][1] + "?", parent=delete_menu): # if the student is found, a confirmation will apear in which case the user can either choose to delete the student record or not
            records.pop(i) # deletes the  record
            save_records() # saves the records in the .json file
            refresh_students() # refreshes the list of students
            show("Student deleted") # shows a deleted text to the whitearea (actually black)
            delete_menu.destroy() # closes the popup

    tk.Button(delete_menu, text="Delete Student", command=delete).pack(pady=20)

# this function opens a Toplevel popup when you click update, allowing the user to update a student's record
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
            messagebox.showerror("Error", "Please complete the information", parent=update_menu) # an error that shows if a user did not input anything
            return
        i = find(record[0]) # picks which student gets changed
        if i is None:
            messagebox.showerror("Error", "Student is not found", parent=update_menu) # if the student is not found, it shows an error
        else:
            records[i] = record # replaces the old record with the newly updated one
            save_records() # saves it into the .json fle
            refresh_students() # refreshes the list
            show("STUDENT UPDATED:\n\n" + library(students[i])) # shows which student got updated into the whitearea (again its black (running joke funny))
            update_menu.destroy() # closes the popup

    tk.Button(update_menu, text="Update Student", command=update).pack(pady=20)

# the grade for each student, it returns the letter corresponding with the number of the student
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

#this function handles all the necessary data for the student it is linked towards the student's main data, every button that shows a student uses this function
def library(student):
    percent = percentage(student)
    lines = [
        f"Student Number: {student['id']}",
        f"Student Name: {student['name']}",
        f"Total Coursework Mark: {student['coursework']}",
        f"Exam: {student['examscore']}",
        f"Overall Percentage: {percent:.1f}%", # rounds to the 1 decimal place
        f"Student Grade: {grade(percent)}",
    ]
    return "\n".join(lines) + "\n" # joins the line

#calculates the student's coursework with the exam score to figure out the overall %
def percentage(students):
    return (students["coursework"] + students["examscore"]) / 160 * 100 # coursework is out of 60 + the exam which is out of 100 = 160

#  show all the students and their information within the whitearea
def show_allstudents():
    message = ""
    for student in students:
        message += library(student) + "\n\n" # \n adds a blank between each student
    show(message)

# puts the text into the white area (or in this case, black
def show(message):
    whitearea.config(state=tk.NORMAL) # the box is first unlocked with NORMAL to input information
    whitearea.delete("1.0", tk.END)
    whitearea.insert(tk.END, message)
    whitearea.config(state=tk.DISABLED) # and then the box is locked as DISABLED so the user cannot input anything into the whitearea

#this function allows individual's data to be acquired through the "View Individual Students" button
def show_individual():
    individualmenu = tk.Toplevel(mainmenu)
    individualmenu.title("Individual Student Records")
    individualmenu.geometry("400x350")
    individualmenu.resizable(False, False)

    individual_label = tk.Label(individualmenu, text="Enter Student Number:")
    individual_label.place(relx=0.5, rely=0.1, anchor="center")
    enter_id = tk.Entry(individualmenu)
    enter_id.place(relx=0.5, rely=0.2, anchor="center")

    result_label = tk.Label(individualmenu, text="", justify=tk.LEFT, font=("Arial", 11)) # this label is for students not found, displaying a label in the popup 
    result_label.place(relx=0.5, rely=0.6, anchor="center")

# This allows the search function to work in the individuals popup
    def search():
        student_searched = enter_id.get().strip()
        for s in students:
            if s["id"] == student_searched:
                show(library(s)) #shows the student in the main frame
                individualmenu.destroy() #close the popup
                return # if the student is found, it ends here
        result_label.config(text="Student is Not Found") # line is outside of the loop, which only shows if no students are found

    search_button = tk.Button(individualmenu, text="Search", command=search)
    search_button.place(relx=0.5, rely=0.3, anchor="center")

#These functions are used for sorting the HIGHEST and LOWEST scored students, along with a system that organizes it alphabetically
# highest scored students
def highest_score():
    top_student = max(students, key=percentage) # max identifies each student and uses percentage to compare the information
    show("STUDENT WITH HIGHEST MARK:\n\n" + library(top_student))

# lowest scored students
def lowest_score():
    bottom_student = min(students, key=percentage) # min also identifies each student but picks the smallest possible one
    show("STUDENT WITH LOWEST MARK:\n\n" + library(bottom_student))

# alphabetical order
def alphabetical_score():
    message = "ALPHABETICAL ORDER (A-Z):\n\n"
    for student in sorted(students, key=lambda x: x["name"]): # makes a sorted copy, and lambda orders it to organize it by each student's first name
        message += library(student) + "\n"
    show(message)

# A sort menu, it is a Toplevel that sorts based on the button clicked:the highest/lowest scored students, and the alphabetical order
def show_sort():
    sort_menu = tk.Toplevel(mainmenu)
    sort_menu.title("Sort Tab")
    sort_menu.geometry("400x350")
    sort_menu.resizable(False, False)

    sort_title = tk.Label(sort_menu, text="Sort the Data:", font=("Arial", 12))
    sort_title.place(relx=0.5, rely=0.1, anchor="center")

# a system that makes it so the popup is played out then destroyed whenever the user clicks on a button
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
whitearea = tk.Text(mainmenu, bg="#0C0C0C", fg="white", state=tk.DISABLED) # whitearea is mentioned alot in the functions, it is used to display all the necessary information
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



root.mainloop() # absolute necessity, keeps the window open