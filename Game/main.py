import tkinter as tk #importing stuff
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import StringVar
option_menu = ["Empty", "Math", "Geograhy", "Trivia"]

def button(master, text, command): # definition for making a button
    bt = tk.Button(master, text=text, command=command)
    bt.pack(pady=5)

def label(master, text): # definition for label
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
        self.name = update()
        self.name
        self.window = tk.Tk()
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        self.menu_things = tk.Frame(self.window)
        label(self.menu_things, "Hello this is the title screen!")
        button(self.menu_things, "Play", self.start)
        button(self.menu_things, "Exit", self.exit)
        self.menu_things.pack(pady=5)

    def exit(self): # used when exiting the progam
        if messagebox.askyesno(title="Exit", message="Are you sure?"):
            self.window.destroy()
            
    def start(self): # this starts the game
        menu = StringVar()
        menu.set("Empty")
        self.menu_things.destroy()
        self.setting_things = tk.Frame(self.window)
        self.label = tk.Label(self.setting_things, text="Name: {}".format(self.name)) # I want to use the function but I dont know how to edit the label when its in a function.
        self.label.pack(pady=5)
        button(self.setting_things, "Set your name", self.set_name)
        label(self.setting_things, "What are you going to play?")
        self.play_option = tk.OptionMenu(self.setting_things, menu, *option_menu)
        self.play_option.pack(pady=5)
        button(self.setting_things, "Continue", self.next)
        self.setting_things.pack(pady=5)

    def next(self):
        if self.play_option == "Empty":
            self.empty
        elif self.play_option == "Math":
            self.math
            print("Math")
        elif self.play_option == "Geography":
            self.geography
        elif self.play_option == "Trivia":
            self.trivia
        else:
            print("bruh")
    
    def set_name(self): #sets name and saves name
        self.name = simpledialog.askstring("Pick your Name", "Name:")
        self.save_file = open("Game/save.txt", "w")
        self.save_file.writelines([self.name])
        self.save_file.close()
        self.label.config(text="Name: " + self.name)

    def empty(self):
        pass
    
    def math(self):
        self.setting_things.destroy()

    def geography(self):
        self.setting_things.destroy()

    def trivia(self):
        self.setting_things.destroy()


window = Window()
window