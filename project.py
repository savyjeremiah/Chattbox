import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        color_label.config(bg=color)

root = tk.Tk()
root.title("Color Picker")

choose_button = tk.Button(root, text="Choose Color", command=choose_color)
choose_button.pack(pady=10)

color_label = tk.Label(root, text="savyjeremiah", width=2000, height=50)
color_label.pack(pady=10)

root.mainloop()
