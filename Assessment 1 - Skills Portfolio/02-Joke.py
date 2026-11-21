import random
import tkinter as tk

root = tk.Tk()
root.title("jokes!")
root.geometry("1080x720")
root.resizable(False, False)

with open("randomJokes.txt", "r", encoding="utf-8") as file:
    joke = file.read()
    jokelines_text=""

    def jokeGenerator():
        if jokelines_text == "":
            next

    def next():
        global jokelines_text
        line, line2 = random.choice(joke).split("?, 1")
        joke.config(text=line["line"] +"?")
        jokelines_text = line2.strip
        jokelines_text.config(text="")

    def showJoke():
        jokelines_text.config(text=jokelines_text)



menu = tk.Frame(root, width="1080", height="720", bg="lightblue")
menulabel1 = tk.Label(menu, text="The JOKER's Circus!", font=("Arial", 24,), fg="black", padx=20, pady=20)
menulabel1.place(relx=0.5, rely=0.1, anchor="center")

menu.place(x=0, y=0)

menu.tkraise()
root.mainloop()