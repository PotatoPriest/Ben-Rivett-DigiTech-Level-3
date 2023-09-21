import tkinter as tk #importing stuff
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import StringVar
import random
option_menu = ["Empty", "Math", "Geography", "Trivia", "Test"] # list for options in the options menu

def button(master, text, command): # definition for making a button
    bt = tk.Button(master, text=text, command=command)
    bt.pack(pady=5)

def label(master, text): # definition for label
    la = tk.Label(master, text=text)
    la.pack(pady=5)

class Error: # This class is for error catching, will probobly change it alot later
    def __init__(self):
        tk.messagebox.showerror(title="Error", message="There has been an error")

class read: # used to read the save file
    def __init__(self):
        self.save_file = open("Game/save.txt", "r")
        self.name = self.save_file.readline()
        self.save_file.close()
    def __str__(self):
        return self.name

class Window: # class for the main window
    def menu_button(self):
        self.menuf = tk.Frame(self.window)
        button(self.menuf, "Menu", Error)
        self.menuf.place(anchor="nw")
        
    def __init__(self):
        self.question = "There is no question"
        self.qnumber = 1
        self.score = 0
        self.name = read()
        self.name
        self.window = tk.Tk()
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        self.menu_things = tk.Frame(self.window)
        label(self.menu_things, "Hello this is the title screen!")
        button(self.menu_things, "Play", self.start)
        button(self.menu_things, "Load Save", Error)
        button(self.menu_things, "Exit", self.exit)
        self.scoref = tk.Frame(self.window)
        self.scoref.pack(anchor="ne")
        self.scorel = tk.Label(self.scoref, text="Score: {}".format(self.score))
        self.scorel.pack()
        self.menu_things.pack(pady=5)
        
    def exit(self): # used when exiting the progam
        if messagebox.askyesno(title="Exit", message="Are you sure?"):
            self.window.destroy()
            
    def start(self): # this starts the game
        self.menu = StringVar()
        self.menu.set("Empty")
        self.menu_things.destroy()
        self.setting_things = tk.Frame(self.window)
        self.label = tk.Label(self.setting_things, text="Name: {}".format(self.name)) # I want to use the function but I dont know how to edit the label when its in a function.
        self.label.pack(pady=5)
        button(self.setting_things, "Set your name", self.set_name)
        label(self.setting_things, "What are you going to play?")
        self.play_option = tk.OptionMenu(self.setting_things, self.menu, *option_menu)
        self.play_option.pack(pady=5)
        button(self.setting_things, "Continue", self.next)
        self.setting_things.pack(pady=5)

    def next(self): # What happens when you pick something from the options menu
        self.option = self.menu.get()
        if self.option == "Empty":
            self.empty()
        elif self.option == "Math":
            self.math()
        elif self.option == "Geography":
            self.geography()
        elif self.option == "Trivia":
            self.trivia()
        else:
            Error()
    
    def set_name(self): #sets name and saves name
        self.name = simpledialog.askstring("Pick your Name", "Name:")
        if self.name == None:
            self.name = "None"

        else:
            self.name = self.name
            
        self.save_file = open("Game/save.txt", "w")
        self.save_file.writelines([self.name])
        self.save_file.close()
        self.label.config(text="Name: " + self.name)

    def back(self): # This sends you back to the start
        self.option = self.menu.get()
        if self.option == "Math":
            self.math_stuff.destroy()
            self.start()
            
        elif self.option == "Geography":
            self.geography_stuff.destroy()
            self.start()
            
        elif self.option == "Trivia":
            self.trivia_stuff.destroy()
            self.start()
            
        else:
            Error()
    
    def empty(self): # When the option is empty
        tk.messagebox.showerror(title="Empty", message="Please pick an option.")

    def setting_question(self): # This willm set the type of question
        if self.option == "Math":
            if self.qnumber < 3: # Addition
                self.one = random.randint(0, 10)
                self.two = random.randint(0, 10)
                self.answer = self.one + self.two
                self.question = "What is the sum of {} + {}?".format(self.one, self.two)
            elif self.qnumber > 2 and self.qnumber < 5: # Multiplication
                self.one = random.randint(1, 10)
                self.two = random.randint(1, 10)
                self.answer = self.one * self.two
                self.question = "What is the sum of {} x {}?".format(self.one, self.two)
                
            elif self.qnumber == 5: # Addition and Multiplication
                self.one = random.randint(1, 10)
                self.two = random.randint(1, 10)
                self.three = random.randint(0, 10)
                self.four = random.randint(0, 10)
                self.answer = self.one * self.two + self.three + self.four
                self.question = "What is the sum of {} x {} + {} + {}?".format(self.one, self.two, self.three, self.four)

            elif self.qnumber > 5 and self.qnumber < 8: # subtraction
                self.one = random.randint(10, 20)
                self.two = random.randint(0, 10)
                self.answer = self.one - self.two
                self.question = "What is the sum of {} - {}?".format(self.one, self.two)

            elif self.qnumber > 7 and self.qnumber < 10: # division
                self.one = random.randrange(8, 22, 2) # fuck you ill see you tommorow (I have decimals) (Make bigger?!?!?!?!?!!?!, will it work?)
                self.two = random.randint(1, 10)
                self.answer = self.one / self.two
                self.question = "What is the sum of {} / {}?".format(self.one, self.two)

            elif self.qnumber == 10: # division and subtraction
                self.one = random.randrange(8, 22, 2) # fuck you ill see you tommorow (I have decimals)
                self.two = random.randint(1, 10)
                self.three = random.randint(10, 20)
                self.four = random.randint(0, 10)
                self.answer = self.one / self.two + self.three - self.four
                self.question = "What is the sum of {} / {} + {} - {}?".format(self.one, self.two, self.three, self.four)
                
            else:
                Error()
                
        elif self.option == "Geography":
            pass

        elif self.option == "Trivia":
            pass

        else:
            Error()
    
    def math(self):
        self.setting_things.destroy()
        self.math_stuff = tk.Frame(self.window)
        label(self.math_stuff, """{}, This area of the game will test your knoledge
on Mathmatics, starting with addition and subtraction
then moving on to multiplication and divition.""".format(self.name))
        button(self.math_stuff, "Continue", self.math_questions)
        button(self.math_stuff, "Back", self.back)
        self.math_stuff.pack(pady=5)
        
    def geography(self):
        self.setting_things.destroy()
        self.geography_stuff = tk.Frame(self.window)
        label(self.geography_stuff, """{}, This area of the game will test your knoledge
on Geography, this will incluce naming the country
based on its siluete as well as its flag.""".format(self.name))
        button(self.geography_stuff, "Continue", Error)
        button(self.geography_stuff, "Back", self.back)
        self.geography_stuff.pack(pady=5)

    def trivia(self):
        self.setting_things.destroy()
        self.trivia_stuff = tk.Frame(self.window)
        label(self.trivia_stuff, """{}, This area of the game will test your knoledge
on random Trivia, this will include questions on anything.""".format(self.name))
        button(self.trivia_stuff, "Continue", Error)
        button(self.trivia_stuff, "Back", self.back)
        self.trivia_stuff.pack(pady=5)
        
    def math_questions(self):
        self.math_stuff.destroy()
        self.math_qf = tk.Frame(self.window)
        self.setting_question()
        label(self.math_qf, "Question {}: {}".format(self.qnumber, self.question))
        self.aentry = tk.Entry(self.math_qf)
        self.aentry.pack()
        self.mathsubmitbt = tk.Button(self.math_qf, text="Submit", command=self.submit)
        self.mathsubmitbt.pack(pady=5)
        self.math_qf.pack(pady=5)

    def submit(self):
        try:
            self.player_answer = int(self.aentry.get())
            self.answer_check()
        except ValueError:
            tk.messagebox.showinfo("No Input", "Please input a valid responce")

        
    
    def answer_check(self):
            
        self.qnumber = self.qnumber + 1
        if self.player_answer == self.answer:
            self.math_qf.destroy()
            self.correct = tk.Frame(self.window)
            label(self.correct, "Well done {} was the correct answer!".format(self.answer))
            button(self.correct, "Next question", self.intermission)
            self.correct.pack(pady=5)
            self.score = self.score + 1
            self.scorel.config(text="Score: {}".format(self.score))
            
        else:
            self.math_qf.destroy()
            self.incorrect = tk.Frame(self.window)
            label(self.incorrect, """Im sorry but {} was not the correct answer.
The correct answer was {}.""".format(self.player_answer, self.answer))
            button(self.incorrect, "Next question", self.intermission)
            self.incorrect.pack(pady=5)

    def intermission(self):
        if self.player_answer == self.answer:
            self.correct.destroy()
            self.setting_question()
            self.math_questions()
        else:
            self.incorrect.destroy()
            self.setting_question()
            self.math_questions()
            
window = Window()
window
window.window.mainloop()