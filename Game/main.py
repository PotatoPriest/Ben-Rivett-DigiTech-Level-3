import tkinter as tk # These import tkinter
from tkinter import messagebox # This imports the messagebox function in tkinter
from tkinter import simpledialog # This imports the Simpledialog function from tkinter

class Nill: # This is for functions that does nothing (so I know they work)
    def __init__(self):
        print("Does Nothing")

class Error: # This class is for error catching
    def __init__(self):
        tk.messagebox.showerror(title="Error", message="There has been an error")

class User():
    def __init__(self, username):
        User.username = username
        print(User.username)
    def username_change(self):
        User.username = simpledialog.askstring("Username Change", "What would you like to change your username to?")
        self.save_file = open("Game/save.txt", "w")
        self.save_file.writelines([User.username])
        self.save_file.close()
        print(User.username)

class update:
    def __init__(self):
        self.save_file = open("Game/save.txt", "r")
        self.name = self.save_file.readline()
        self.save_file.close()
    def __str__(self):
        return self.name

class Window(User): # This class is for creating a basic window
    
    def __init__(self, title, size, colour): # This is the definition that is called when the class is initilized
        self.name = update()
        self.colour = colour
        self.title = title # This is the varable for the title bar of the window
        self.size = size # This is the variable for setting the size of the window
        self.window = tk.Tk() # This makes the window
        self.window.title(self.title) # This sets the title of the window
        self.window.geometry(self.size) # This sets the size of the window
        self.window.config(bg=self.colour)
        self.label = tk.Label(self.window, text=self.title)
        self.label.pack(pady=5)
        self.namelabel = tk.Label(self.window, text="Username:  {}".format(self.name))
        self.namelabel.pack()
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
            
    def instant_leave(self):
        self.window.destroy()

class Settings:
    def __init__(self):
        self.save_file = open("Game/save.txt", "r")
        self.name = self.save_file.readline()
        self.save_file.close()
        user = User(self.name)
        self.settings = Window("Settings", "300x300", "blue")
        self.settings.button("Change Name", user.username_change)
        self.settings.button2("Save Game", Save)
        self.settings.button3("Exit", self.settings.exit)

class Save:
    def __init__(self):
        self.new_line = simpledialog.askstring("Text file line", "Please add a new line into the text file")
        self.save_file = open("Game/save.txt", "a")
        self.save_file.write(self.new_line)
        self.save_file.close()
        

menu = Window("Menu", "400x300", "white")
menu.button("Play", Error)
menu.button2("Settings", Settings)
menu.button3("Exit", menu.exit)
menu.window.mainloop()
