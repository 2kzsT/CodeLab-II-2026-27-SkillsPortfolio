import tkinter as tk

root = tk.Tk()
root.title("Math Quiz")
root.geometry("1080x720")
root.resizable(False, False)

def showframe(frame):
    frame.tkraise()

menu = tk.Frame(root, width=1080, height=720, bg="lightblue")
l1 = tk.Label(menu, text="THE Math Quiz", font=("Arial", 24,), fg="black", padx=20, pady=20)
l1.place(relx=0.5, rely=0.1, anchor="center")
l2 = tk.Label(menu, text="Hello, Welcome to the Infamous Math Quiz!", font=("Arial", 16,), fg="black")
l2.place(relx=0.5, rely=0.28, anchor="center")
l3 = tk.Label(menu, text="Please Select the Difficulty Level", font=("Arial", 14,), fg="black",)
l3.place(relx=0.5, rely=0.38, anchor="center")

button1 = tk.Button(menu, text="Easy", font=("Arial", 20,), fg="black", command=lambda: showframe(easy))
button1.place(relx=0.25, rely=0.6, anchor="center")
button2 = tk.Button(menu, text="Moderate", font=("Arial", 20,), fg="black", command=lambda: showframe(moderate))
button2.place(relx=0.5, rely=0.6, anchor="center")
button3 = tk.Button(menu, text="Advanced", font=("Arial", 20,), fg="black", command=lambda: showframe(advanced))
button3.place(relx=0.75, rely=0.6, anchor="center")
menu.place(x=0, y=0)

easy = tk.Frame(root, width=1080, height=720, bg="green")

back_button1 = tk.Button(easy, text="Back", font=("Arial", 20,), fg="black", command=lambda: showframe(menu))
back_button1.place(relx=0.5, rely=0.9, anchor="center")

easy.place(x=0, y=0)


moderate = tk.Frame(root, width=1080, height=720, bg="yellow")

back_button1 = tk.Button(moderate, text="Back", font=("Arial", 20,), fg="black", command=lambda: showframe(menu))
back_button1.place(relx=0.5, rely=0.9, anchor="center")

moderate.place(x=0, y=0)

advanced = tk.Frame(root, width=1080, height=720, bg="red")

back_button1 = tk.Button(advanced, text="Back", font=("Arial", 20,), fg="black", command=lambda: showframe(menu))
back_button1.place(relx=0.5, rely=0.9, anchor="center")

advanced.place(x=0, y=0)

menu.tkraise()
root.mainloop()
