import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def button(master, text, command):
    bt = tk.Button(master, text=text, command=command)
    bt.pack(pady=5)

class Error: # This class is for error catching
    def __init__(self):
        tk.messagebox.showerror(title="Error", message="There has been an error")

class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        button(self.window, "Button", Error)
        button(self.window, "Button 2", Error)

window = Window()
window