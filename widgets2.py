from tkinter import *
from datetime import date
window = Tk()
window.title("introduction to tkinter")
window.geometry("400x400")

label = Label(text="hi", fg="pink", bg="black",)
name = Label(text="your name", bg="light blue")
entry = Entry()

def display():
    name = entry.get()

    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())


text_box = Text(height=3)

btn = Button(text="begin", command=display, height=1, bg="white", fg="black")

label.pack()
name.pack()
entry.pack()
btn.pack()
text_box.pack()

window.mainloop()