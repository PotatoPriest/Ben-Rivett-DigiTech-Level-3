import tkinter as tk # These import tkinter
from tkinter import messagebox # This imports the messagebox function in tkinter
from tkinter import simpledialog # This imports the Simpledialog function from tkinter

class Nill: # This is for functions that does nothing (so I know they work)
    def __init__(self):
        print("Does Nothing")

class Error: # This class is for error catching
    def __init__(self):
        tk.messagebox.showerror(title="Error", message="There has been an error")

class User:
    def __init__(self, username):
        self.username = username

class Window(User): # This class is for creating a basic window
    def __init__(self, title, size, colour): # This is the definition that is called when the class is initilized
        self.colour = colour
        self.title = title # This is the varable for the title bar of the window
        self.size = size # This is the variable for setting the size of the window
        self.window = tk.Tk() # This makes the window
        self.window.title(self.title) # This sets the title of the window
        self.window.geometry(self.size) # This sets the size of the window
        self.window.config(bg=self.colour)
        self.label = tk.Label(self.window, text=self.title)
        self.label.pack(pady=5)
        self.window.protocol("WM_DELETE_WINDOW", self.exit)
        
    def button(self, text, command): # Definition for adding buttons to the window
        self.text = text
        self.command = command
        self.button = tk.Button(self.window, text=self.text, command=self.command) # Setting what the button does and says
        self.button.pack(pady=5)
        
    def button2(self, text, command):
        self.text = text
        self.command = command
        self.button = tk.Button(self.window, text=self.text, command=self.command)
        self.button.pack(pady=5)
        
    def button3(self, text, command):
        self.text = text
        self.command = command
        self.button = tk.Button(self.window, text=self.text, command=self.command)
        self.button.pack(pady=5)
    
    def exit(self):
        if messagebox.askyesno(title="Exit", message="Are you sure?"):
            self.window.destroy()

class Settings:
    def __init__(self):
        self.settings = Window("Settings", "300x300", "blue")
        self.settings.button("Change Name", Nill)
        self.settings.button2("Exit", self.settings.exit)

menu = Window("Menu", "400x300", "white")
menu.button("Play", Error)
menu.button2("Settings", Settings)
menu.button3("Exit", menu.exit)
menu.window.mainloop()