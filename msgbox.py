from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("MessageBox")
window.geometry("200x200")

def msg():
    messagebox.showwarning("Alert","Stop virus detected")

btn = Button(window, text="scan", command=msg)
btn.pack()
window.mainloop()

