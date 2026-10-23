from tkinter import *

window = Tk()
window.title("denomination calcualator")
window.geometry("400x300")

def topwin():
    top = Toplevel()
    top.geometry("200x200")
    top.title("topwin")

    l2 = Label(top, text="this is topwin")
    l2.pack()
    top.mainloop()

l1 = (Label(window, text="this is our main window"))
btn = Button(window, text="Click Me!", command= topwin)
l1.pack()
btn.pack()

window.mainloop()

