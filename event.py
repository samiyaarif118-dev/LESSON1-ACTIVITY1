from tkinter import *

window = Tk()
window.title("EVENT")
window.geometry("300x300")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("button was clicked")

btn = Button(window, text="Click me")
btn.pack()
btn.bind("<Button-1>", handle_click)
window.mainloop()

