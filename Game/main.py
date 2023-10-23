import tkinter as tk #importing stuff
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import StringVar
import random
from PIL import ImageTk, Image
option_menu = ["Empty", "Math", "Geography", "Trivia"] # list for options in the options menu
flag_dict = {"Game/Images/Flag_Argentina.png" : "Argintina", "Game/Images/Flag_Australia.png" : "Australia", "Game/Images/Flag_Austria.png" : "Austria", "Game/Images/Flag_Belgium.png" : "Belgium", "Game/Images/Flag_Brazil.png" : "Brazil", "Game/Images/Flag_Bulgaria.png" : "Bulgaria", "Game/Images/Flag_Canada.png" : "Canada", "Game/Images/Flag_China.png" : "China", "Game/Images/Flag_Croatia.png" : "Croatia", "Game/Images/Flag_Denmark.png" : "Denmark", "Game/Images/Flag_Dominican_Republic.png" : "Dominican Republic", "Game/Images/Flag_Egypt.png" : "Egypt", "Game/Images/Flag_France.png" : "France", "Game/Images/Flag_Germany.png" : "Germany", "Game/Images/Flag_Greece.png" : "Greece", "Game/Images/Flag_Hong_Kong.png" : "Hong Kong", "Game/Images/Flag_Hungary.png" : "Hungary", "Game/Images/Flag_Iceland.png" : "Iceland", "Game/Images/Flag_India.png" : "India", "Game/Images/Flag_Indonesia.png" : "Indonesia", "Game/Images/Flag_Ireland.png" : "Ireland", "Game/Images/Flag_Italy.png" : "Italy", "Game/Images/Flag_Japan.png" : "Japan", "Game/Images/Flag_Jordan.png" : "Jordan", "Game/Images/Flag_Malaysia.png" : "Malaysia", "Game/Images/Flag_Mexico.png" : "Mexico", "Game/Images/Flag_Morocco.png" : "Morocco", "Game/Images/Flag_Netherlands.png" : "Netherlands", "Game/Images/Flag_North_Korea.png" : "North Korea", "Game/Images/Flag_Norway.png" : "Norway", "Game/Images/Flag_NZ.png" : "New Zealand", "Game/Images/Flag_Philippines.png" : "Philippines", "Game/Images/Flag_Poland.png" : "Poland", "Game/Images/Flag_Portugal.png" : "Portugal", "Game/Images/Flag_Russia.png" : "Russia", "Game/Images/Flag_Saudi_Arabia.png" : "Saudi Arabia", "Game/Images/Flag_Singapore.png" : "Singapore", "Game/Images/Flag_South_Africa.png" : "South Africa", "Game/Images/Flag_South_Korea.png" : "South Korea", "Game/Images/Flag_Spain.png" : "Spain", "Game/Images/Flag_Sweden.png" : "Sweden", "Game/Images/Flag_Switzerland.png" : "Switzerland", "Game/Images/Flag_Thailand.png" : "Thailand", "Game/Images/Flag_Turkey.png" : "Turkey", "Game/Images/Flag_UAE.png" : "United Arab Emirates", "Game/Images/Flag_UK.png" : "United Kingdom", "Game/Images/Flag_Ukraine.png" : "Ukraine", "Game/Images/Flag_USA.png" : "United States of America", "Game/Images/Flag_Vietnam.png" : "Vietnam"} # Dictonairy of flag images

def button(master, text, command): # definition for making a button
    bt = tk.Button(master, text=text, command=command)
    bt.pack(pady=5)

def label(master, text): # definition for label
    la = tk.Label(master, text=text)
    la.pack(pady=5)

def image(master, path, x, y): # this imports an image to be used in code
    imageframe = tk.Frame(master)
    img = ImageTk.PhotoImage(Image.open(path).resize((x, y)))
    image = tk.Label(imageframe, image=img)
    image.image = img
    image.pack()
    imageframe.pack()

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
    def __init__(self): # This happens when the class is initilised
        self.img_path = "No path"
        self.state = 0
        self.math_done = 0
        self.geography_done = 0
        self.trivia_done = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.question = "There is no question"
        self.qnumber = 1
        self.score = 0
        self.name = "None"
        self.window = tk.Tk()
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        self.scoref = tk.Frame(self.window)
        self.scoref.pack(anchor="ne")
        self.scorel = tk.Label(self.scoref, text="Score: {}".format(self.score))
        self.scorel.pack()
        self.main_menu()

    def main_menu(self): # This is the main menu
        self.menu_things = tk.Frame(self.window)
        label(self.menu_things, "Hello this is the title screen!")
        button(self.menu_things, "Play", self.start)
        button(self.menu_things, "Save Menu", self.save_menu)
        button(self.menu_things, "Exit", self.exit)
        self.menu_things.pack(pady=5)

    def save_menu(self): # this menu does save stuff
        self.state = 0
        self.menu_things.destroy()
        self.savef = tk.Frame(self.window)
        button(self.savef, "Save Game", self.save_file)
        button(self.savef, "Load Save", self.load_file)
        button(self.savef, "Back", self.back_menu)
        self.savef.pack(pady=5)

    def back_menu(self): # this is to go back to the main menu
        if self.state == 1:
            self.setting_things.destroy()
            self.main_menu()
        else:
            self.savef.destroy()
            self.main_menu()
        
    def save_file(self): # Saves the players progress
        self.save_file = open("Game/save.txt", "w")
        self.save_file.writelines("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.name, self.score, self.correct_answers, self.incorrect_answers, self.math_done, self.geography_done, self.trivia_done))
        self.save_file.close()
        tk.messagebox.showinfo(title="Save Game", message="Your game has been saved!")
        
    def load_file(self): # loads the players progress
        self.save_file = open("Game/save.txt", "r")
        self.name = self.save_file.readline()
        self.score = self.save_file.readline()
        self.correct_answers = self.save_file.readline()
        self.incorrect_answers = self.save_file.readline()
        self.math_done = self.save_file.readline()
        self.geograhpy_done = self.save_file.readline()
        self.trivia_done = self.save_file.readline()
        self.save_file.close()
        self.scorel.config(text="Score: {}".format(self.score))
        tk.messagebox.showinfo(title="Load Save", message="Your save has been loaded")
    
    def exit(self): # used when exiting the progam
        if messagebox.askyesno(title="Exit", message="Are you sure?"):
            self.window.destroy()
            
    def start(self): # this starts the game
        self.state = 1
        self.menu = StringVar()
        self.menu.set("Empty")
        self.menu_things.destroy()
        self.setting_things = tk.Frame(self.window)
        self.label = tk.Label(self.setting_things, text="Name: {}".format(self.name))
        self.label.pack(pady=5)
        button(self.setting_things, "Set your name", self.set_name)
        label(self.setting_things, "What are you going to play?")
        self.play_option = tk.OptionMenu(self.setting_things, self.menu, *option_menu)
        self.play_option.pack(pady=5)
        button(self.setting_things, "Continue", self.next)
        button(self.setting_things, "Back", self.back_menu)
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
    
    def set_name(self): #sets name
        self.name = simpledialog.askstring("Pick your Name", "Name:")
        if self.name == None:
            self.name = "None"

        else:
            self.name = self.name

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
                self.one = random.randint(0, 100)
                self.two = random.randint(0, 100)
                self.answer = self.one + self.two
                self.question = "What is the sum of {} + {}?".format(self.one, self.two)
            elif self.qnumber > 2 and self.qnumber < 5: # Multiplication
                self.one = random.randint(1, 25)
                self.two = random.randint(1, 10)
                self.answer = self.one * self.two
                self.question = "What is the sum of {} x {}?".format(self.one, self.two)
                
            elif self.qnumber == 5: # Addition and Multiplication
                self.one = random.randint(1, 25)
                self.two = random.randint(1, 10)
                self.three = random.randint(0, 100)
                self.four = random.randint(0, 100)
                self.answer = self.one * self.two + self.three + self.four
                self.question = "What is the sum of {} x {} + {} + {}?".format(self.one, self.two, self.three, self.four)

            elif self.qnumber > 5 and self.qnumber < 8: # subtraction
                self.one = random.randint(10, 100)
                self.two = random.randint(0, 75)
                while self.one < self.two:
                    self.one = random.randint(10, 100)
                self.answer = self.one - self.two
                self.question = "What is the sum of {} - {}?".format(self.one, self.two)

            elif self.qnumber > 7 and self.qnumber < 10: # division
                self.one = random.randint(1, 10)
                self.two = random.randint(1, 5)
                while self.one <= self.two:
                    self.one = random.randint(1, 10)
                self.answer = round(self.one / self.two)
                self.question = """What is the sum of {} / {}?
(Round to the nearest whole number.)""".format(self.one, self.two)

            elif self.qnumber == 10: # division and subtraction
                self.one = random.randint(10, 20)
                self.two = random.randint(1, 5)
                self.three = random.randint(10, 100)
                self.four = random.randint(0, 75)
                while self.three < self.four:
                    self.three = random.randint(10, 100)
                while self.one <= self.two:
                    self.one = random.randint(1, 20)
                self.answer = round(self.one // self.two + self.three - self.four)
                self.question = """What is the sum of {} / {} + {} - {}?
(Round to the nearist whole number.)""".format(self.one, self.two, self.three, self.four)
            elif self.qnumber > 10: # This is so there is no error after the player has finnished answering questions
                self.question = """Well done {}!
You have completed the Math questions.""".format(self.name)   
            else:
                Error()
                
        elif self.option == "Geography":
            if self.qnumber < 10:
                self.img_path, self.answer = random.choice(list(flag_dict.items())) # Needs to work
                image(self.geography_qf, self.img_path, 200, 100)
                self.question = "What country does this flag belong too?"
                self.flags_set()
                print(self.answer)

            else:
                self.question = """Well done {}!
You have completed the Math questions.""".format(self.name)
                
        elif self.option == "Trivia":
            pass

        else:
            Error()
    
    def flags_set(self): ### HEAVY WORK IN PROGRESS!!!!
        pass
    
    def math(self): # This starts the math questions
        self.setting_things.destroy()
        self.math_stuff = tk.Frame(self.window)
        
        if self.math_done == 0:
            label(self.math_stuff, "You have NOT done the Math questions.")
        else:
            label(self.math_stuff, "You have done the Math questions.")
            
        label(self.math_stuff, """{}, This area of the game will test your knoledge
on Mathmatics, starting with addition and subtraction
then moving on to multiplication and divition.""".format(self.name))
        button(self.math_stuff, "Continue", self.math_questions)
        button(self.math_stuff, "Back", self.back)
        self.math_stuff.pack(pady=5)

    def done(self): # this is for when the player is done answering the questions
        self.completef.destroy()
        self.start()
        self.qnumber = 1
            
    def geography(self): # This starts the geography questions
        self.setting_things.destroy()
        self.geography_stuff = tk.Frame(self.window)
        
        if self.geography_done == 0:
            label(self.geography_stuff, "You have NOT done the Geography questions.")
        else:
            label(self.geography_stuff, "You have done the Geography questions.")
            
        label(self.geography_stuff, """{}, This area of the game will test your knoledge
on Geography, this will incluce naming the country
based on its siluete as well as its flag.""".format(self.name))
        button(self.geography_stuff, "Continue", self.geography_questions)
        button(self.geography_stuff, "Back", self.back)
        self.geography_stuff.pack(pady=5)

    def trivia(self): # This starts the trivia questions
        self.setting_things.destroy()
        self.trivia_stuff = tk.Frame(self.window)
        
        if self.trivia_done == 0:
            label(self.trivia_stuff, "You have NOT done the Trivia questions.")
        else:
            label(self.trivia_stuff, "You have done the Trivia questions.")
            
        label(self.trivia_stuff, """{}, This area of the game will test your knoledge
on random Trivia, this will include questions on anything.""".format(self.name))
        button(self.trivia_stuff, "Continue", Error)
        button(self.trivia_stuff, "Back", self.back)
        self.trivia_stuff.pack(pady=5)
        
    def math_questions(self): # This is the math questions
        if self.qnumber == 11:
            self.completef = tk.Frame(self.window)
            label(self.completef, self.question)
            label(self.completef, """Your score is {}.
You have gotten {} correct answers,
You have gotten {} incorrect answers.""".format(self.score, self.correct_answers, self.incorrect_answers))
            self.math_done = 1
            button(self.completef, "Continue", self.done)
            self.completef.pack(pady=5)
        else:
            self.math_stuff.destroy()
            self.math_qf = tk.Frame(self.window)
            self.setting_question()
            label(self.math_qf, "Question {}: {}".format(self.qnumber, self.question))
            self.aentry = tk.Entry(self.math_qf)
            self.aentry.pack()
            button(self.math_qf, "Submit", self.submit)
            self.math_qf.pack(pady=5)
                
    def geography_questions(self): #!!!!!MAJOUR WORK IN PROGRESS!!!!!
        if self.qnumber == 11:
            self.completef = tk.Frame(self.window)
            label(self.completef, self.question)
            label(self.completef, """Your score is {}.
You have gotten {} correct answers,
You have gotten {} incorrect answers.""".format(self.score, self.correct_answers, self.incorrect_answers))
            self.geography_done = 1
            button(self.completef, "Continue", self.done)
            self.completef.pack(pady=5)
        else:
            self.geography_stuff.destroy()
            self.geography_qf = tk.Frame(self.window)
            self.setting_question()
            label(self.geography_qf, "Question {}: {}".format(self.qnumber, self.question))
            self.geo_choices()
            self.geography_qf.pack(pady=5)

    def geo_choices(self):
        self.rc_list = []
        while self.answer not in self.rc_list:
            while len(self.rc_list) !=4:
                self.rc_list.append(random.choice(list(flag_dict.values())))
            
        self.choice_1 = tk.Button(self.geography_qf, text=self.rc_list[0], command=Error)
        self.choice_1.pack()
        self.choice_2 = tk.Button(self.geography_qf, text=self.rc_list[1], command=Error)
        self.choice_2.pack()
        self.choice_3 = tk.Button(self.geography_qf, text=self.rc_list[2], command=Error)
        self.choice_3.pack()
        self.choice_4 = tk.Button(self.geography_qf, text=self.rc_list[3], command=Error)
        self.choice_4.pack()
        print(self.rc_list)
        
    def submit(self): # This is so that the player has to input an intiger when answering the math questions.
        if self.option == "Math":
            try:
                self.player_answer = int(self.aentry.get())
                self.answer_check()
            except ValueError:
                tk.messagebox.showinfo("No Input", "Please input a valid responce")
        else:
            self.player_answer = self.aentry.get()
            if self.player_answer == "":
                tk.messagebox.showinfo("No Input", "Please input a valid responce")
            else:
                self.answer_check()
        
    
    def answer_check(self):  # This checks the players answer            
        self.qnumber = self.qnumber + 1
        if self.option == "Math":
            if self.player_answer == self.answer:
                self.math_qf.destroy()
                self.correct = tk.Frame(self.window)
                self.correct_answers = self.correct_answers + 1
                label(self.correct, "Well done {} was the correct answer!".format(self.answer))
                button(self.correct, "Next question", self.intermission)
                self.correct.pack(pady=5)
                self.score = self.score + 1
                self.scorel.config(text="Score: {}".format(self.score))
                
            else:
                self.math_qf.destroy()
                self.incorrect = tk.Frame(self.window)
                self.incorrect_answers = self.incorrect_answers + 1
                label(self.incorrect, """Im sorry but {} was not the correct answer.
    The correct answer was {}.""".format(self.player_answer, self.answer))
                button(self.incorrect, "Next question", self.intermission)
                self.incorrect.pack(pady=5)
                
        elif self.option == "Geography":
            if self.player_answer == self.answer:
                self.geography_qf.destroy()
                self.correct = tk.Frame(self.window)
                self.correct_answers = self.correct_answers + 1
                label(self.correct, "Well done {} was the correct answer!".format(self.answer))
                button(self.correct, "Next question", self.intermission)
                self.correct.pack(pady=5)
                self.score = self.score + 1
                self.scorel.config(text="Score: {}".format(self.score))

            else:
                self.geography_qf.destroy()
                self.incorrect = tk.Frame(self.window)
                self.incorrect_answers = self.incorrect_answers + 1
                label(self.incorrect, """Im sorry but {} was not the correct answer.
            The correct answer was {}.""".format(self.player_answer, self.answer))
                button(self.incorrect, "Next question", self.intermission)
                self.incorrect.pack(pady=5)
                
        elif self.option == "Trivia":
            if self.player_answer == self.answer:
                self.trivia_qf.destroy()
                self.correct = tk.Frame(self.window)
                self.correct_answers = self.correct_answers + 1
                label(self.correct, "Well done {} was the correct answer!".format(self.answer))
                button(self.correct, "Next question", self.intermission)
                self.correct.pack(pady=5)
                self.score = self.score + 1
                self.scorel.config(text="Score: {}".format(self.score))

            else:
                self.trivia_stuff_qf.destroy()
                self.incorrect = tk.Frame(self.window)
                self.incorrect_answers = self.incorrect_answers + 1
                label(self.incorrect, """Im sorry but {} was not the correct answer.
            The correct answer was {}.""".format(self.player_answer, self.answer))
                button(self.incorrect, "Next question", self.intermission)
                self.incorrect.pack(pady=5)

        else:
            Error()
            
    def intermission(self): # This is for in between questions
        if self.option == "Math":
            if self.player_answer == self.answer:
                self.correct.destroy()
                self.setting_question()
                self.math_questions()
            else:
                self.incorrect.destroy()
                self.setting_question()
                self.math_questions()
                
        elif self.option == "Geography":
            if self.player_answer == self.answer:
                self.correct.destroy()
                self.geography_questions()
            else:
                self.incorrect.destroy()
                self.geography_questions()

        elif self.option == "Trivia":
            if self.player_answer == self.answer:
                self.correct.destroy()
                self.setting_question()
                self.trivia_questions()
            else:
                self.incorrect.destroy()
                self.setting_question()
                self.trivia_questions()
        else:
            Error()
            
window = Window() # this starts the game
window
window.window.mainloop()