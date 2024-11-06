import tkinter as tk
from tkinter import colorchooser

def color():
    color =colorchooser.askcolor()[1]
    if color:
        color_lable.config(bg=color)

root =tk.Tk()
root.title("colors")

lable_button =tk.Button(root,name="saviour ", text='chose colors'     ,command=color)
lable_button.pack(pady=6)

color_lable =tk.Label(root,height=299,width=900)
color_lable.pack(padx=6)
root.mainloop()