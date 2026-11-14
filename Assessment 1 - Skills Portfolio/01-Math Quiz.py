import tkinter as tk

root = tk.Tk()
root.title("Math Quiz")
root.geometry("1080x720")
root.resizable(False, False)

l = tk.Label(root, text="THE Math Quiz", font=("Arial", 24,), fg="black",)
l.pack()

root.mainloop()
