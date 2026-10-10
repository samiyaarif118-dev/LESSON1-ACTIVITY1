from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("After School Routine Checker")
window.geometry("300x300")

heading = Label(window, text="My After-School Routine", font=("Arial", 16, "bold"))
heading.pack(pady=10)

instruction = Label(window, text="Tell something about your after-school routine")
instruction.pack()

task_entry = Entry(window, width=35)
task_entry.pack(pady=8)

key_label = Label(window, text="Last key pressed: None")
key_label.pack(pady=5)

def handle_keypress(event):
    """Display the character associated with the key pressed."""
    key_label.config(text="Last key pressed: " + event.char)

task_entry.bind("<Key>", handle_keypress)

def handle_click(event):
    """Update the message when the routine area is clicked."""
    messagebox.showinfo("Routine Status", "Routine section clicked!")

routine_message = Label(window, text="Click here to check your routine", bg="lightblue", width=32, height=3)
routine_message.pack(pady=10)
routine_message.bind("<Button-1>", handle_click)

def check_routine():
    """Display the task or show a warning when it is missing."""
    task = task_entry.get()

    if task == "":
        messagebox.showwarning("Missing task", "Please enter an after school task")

    else:
        routine_message.config(text="Next task: " + task)

btn = Button(window,text="Check my routine", command= check_routine)
btn.pack(pady=10)
window.mainloop()
