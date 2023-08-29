import tkinter as tk #importing stuff
from tkinter import messagebox
from tkinter import simpledialog

def button(master, text, command): # definition for making a button
    bt = tk.Button(master, text=text, command=command)
    bt.pack(pady=5)

def label(master, text):
    la = tk.Label(master, text=text)
    la.pack(pady=5)

class Error: # This class is for error catching
    def __init__(self):
        tk.messagebox.showerror(title="Error", message="There has been an error")

class update: # used to read the save file
    def __init__(self):
        self.save_file = open("Game/save.txt", "r")
        self.name = self.save_file.readline()
        self.save_file.close()
    def __str__(self):
        return self.name

class Window: # class for the main window
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        self.menu_things = tk.Frame(self.window)
        label(self.menu_things, "Hello this is the title screen!")
        button(self.menu_things, "Play", self.start)
        button(self.menu_things, "Exit", self.exit)
        self.menu_things.pack(pady=5)

    def exit(self):
        if messagebox.askyesno(title="Exit", message="Are you sure?"):
            self.window.destroy()
            
    def start(self):
        self.menu_things.destroy()
        self.setting_things = tk.Frame(self.window)
        label(self.setting_things, "Name: ")
        button(self.setting_things, "Set your name", self.set_name)
        label(self.setting_things, "")
        self.setting_things.pack(pady=5)
        
    def set_name(self):
        self.name = simpledialog.askstring("Pick your Name", "Name:")


window = Window()
window