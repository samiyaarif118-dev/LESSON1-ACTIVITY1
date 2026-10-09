from tkinter import *
from datetime import date 

root = Tk()
root.title("Workshop Greeting")
root.geometry("400x400")

heading = Label(text="Workshop Welcome", fg="lightblue",bg="black", height=1, width=300)

name_label = Label(text="participant Name", bg="pink")
name_entry = Entry()

def display_welcome():
    name = name_entry.get()
    text_box.delete(1.0, END)
    greeting = "Hello " + name + "!\n"
    message = "Welcome to the Workshop! \nToday's date is: "
    workshop_date = "Date: " + str(date.today())
    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, workshop_date)

text_box = Text(root, height=5, width=45)
welcome_button = Button(text="check in",command=display_welcome, height=1, bg="gray", fg="black")
heading.pack()
name_label.pack(pady=10)
name_entry.pack()
welcome_button.pack(pady=10)
text_box.pack()
root.mainloop()
