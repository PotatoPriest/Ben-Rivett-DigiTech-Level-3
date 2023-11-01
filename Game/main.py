import tkinter as tk #importing stuff
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import StringVar
import random
from PIL import ImageTk, Image
option_menu = ["Empty", "Math", "Geography", "Trivia"] # list for options in the options menu
flag_dict = {"Game/Images/Flag_Argentina.png" : "Argentina", "Game/Images/Flag_Australia.png" : "Australia", "Game/Images/Flag_Austria.png" : "Austria", "Game/Images/Flag_Belgium.png" : "Belgium", "Game/Images/Flag_Brazil.png" : "Brazil", "Game/Images/Flag_Bulgaria.png" : "Bulgaria", "Game/Images/Flag_Canada.png" : "Canada", "Game/Images/Flag_China.png" : "China", "Game/Images/Flag_Croatia.png" : "Croatia", "Game/Images/Flag_Denmark.png" : "Denmark", "Game/Images/Flag_Dominican_Republic.png" : "Dominican Republic", "Game/Images/Flag_Egypt.png" : "Egypt", "Game/Images/Flag_France.png" : "France", "Game/Images/Flag_Germany.png" : "Germany", "Game/Images/Flag_Greece.png" : "Greece", "Game/Images/Flag_Hong_Kong.png" : "Hong Kong", "Game/Images/Flag_Hungary.png" : "Hungary", "Game/Images/Flag_Iceland.png" : "Iceland", "Game/Images/Flag_India.png" : "India", "Game/Images/Flag_Indonesia.png" : "Indonesia", "Game/Images/Flag_Ireland.png" : "Ireland", "Game/Images/Flag_Italy.png" : "Italy", "Game/Images/Flag_Japan.png" : "Japan", "Game/Images/Flag_Jordan.png" : "Jordan", "Game/Images/Flag_Malaysia.png" : "Malaysia", "Game/Images/Flag_Mexico.png" : "Mexico", "Game/Images/Flag_Morocco.png" : "Morocco", "Game/Images/Flag_Netherlands.png" : "Netherlands", "Game/Images/Flag_North_Korea.png" : "North Korea", "Game/Images/Flag_Norway.png" : "Norway", "Game/Images/Flag_NZ.png" : "New Zealand", "Game/Images/Flag_Philippines.png" : "Philippines", "Game/Images/Flag_Poland.png" : "Poland", "Game/Images/Flag_Portugal.png" : "Portugal", "Game/Images/Flag_Russia.png" : "Russia", "Game/Images/Flag_Saudi_Arabia.png" : "Saudi Arabia", "Game/Images/Flag_Singapore.png" : "Singapore", "Game/Images/Flag_South_Africa.png" : "South Africa", "Game/Images/Flag_South_Korea.png" : "South Korea", "Game/Images/Flag_Spain.png" : "Spain", "Game/Images/Flag_Sweden.png" : "Sweden", "Game/Images/Flag_Switzerland.png" : "Switzerland", "Game/Images/Flag_Thailand.png" : "Thailand", "Game/Images/Flag_Turkey.png" : "Turkey", "Game/Images/Flag_UAE.png" : "United Arab Emirates", "Game/Images/Flag_UK.png" : "United Kingdom", "Game/Images/Flag_Ukraine.png" : "Ukraine", "Game/Images/Flag_USA.png" : "United States of America", "Game/Images/Flag_Vietnam.png" : "Vietnam"} # Dictonairy of flag images

trivia_dict = {"What is the world’s longest river called?" : ["The Nile", "The Amazon", "D River", "Flumen River"], "Where is the Great Barrier Reef located?" : ["Australia", "New Zealand", "Indonesia", "Japan"], """In Greek Mythology,
who is the Queen of the Underworld and wife of Hades?""" : ["Persephone", "Aphrodite", "Athena", "Demeter"], "Which house was Harry Potter ALMOST sorted into?" : ["Slytherin", "Grythindor", "Hufflpuf", "Ravenclaw"], "Which country gifted the Statue of Liberty to the US?" : ["France", "England", "Spain", "Germany"], """What was the name of the Robin Williams
film where he dresses up as an elderly British nanny?""" : ["Mrs. Doubtfire", "Jumanji", "Dead Poets Society", "What Dreams May Come"], "What is the rarest blood type?" : ["AB-Negative", "AB-Positive", "O-Negative", "A-Positive"], "How many bones are there in the human body?" : ["206", "207", "179", "267"], """What is the name of the longest river in
South America?""" : ["The Amazon River", "Orinoco", "pilcomayo", "Yellow River"], "What does Na stand for on the periodic table?" : ["Sodium", "Iron", "Gold", "Lithium"], "In which Disney movie is the villain Clayton from?" : ["Tarzan", "Aladin", "The Hunchback of Notre dame", "Brave"], "In which ocean is the Bermuda Triangle located?" : ["Atlantic Ocean", "Pasific Ocean", "Indian Ocean", "Arctic Ocean"], "What is the French name for Santa Claus?" : ["Pere Noel", "Pierre", "Louis", "Amélie"], "Which fictional city is the home of Batman?" : ["Gotham City", "New York City", "Springfield", "Emerald City"], "Which planet is closest to Earth?" : ["Venus", "Mars", "Jupiter", "Mercuary"], "What is the largest planet in the solar system?" : ["Jupiter", "Uranus", "Mercuary", "The Sun"], "What is Sodium Chloride referred to as?" : ["Salt", "Pepper", "Chilli", "Cinnamon"], "What is the capital of Australia?" : ["Canberra", "Sydney", "Melbourne", "Brisbane"], "Which fast food restaurant is known for its Big Macs?" : ["McDonalds", "Wendys", "Chick-fil-A", "Burger King"], "What are the 3 primary colors?" : ["Red, Yellow, Blue", "Green, Yellow, Blue", "Red, Yellow, Orange", "Red, Green, Blue"], """Who was the first American
astronaut to step foot on the moon?""" : ["Neil Armstrong", "Buzz Aldrin", "Edwin E. Aldrin", "Michael Collins"], "Where is the world’s largest active volcano located?" : ["Hawaii", "California", "Japan", "Spain"], "What is the capital of France?" : ["Paris", "Berlin", "Madrid", "Rome"], "Who founded Microsoft?" : ["Bill Gates", "Mark Zuckerberg", "Steve Jobs", "Larry Page"], """In Greek mythology, who had snakes for hair
and could turn people into stone if they looked at her?""" : ["Medusa", "Hera", "Aphrodite", "Athena"], "What kind of alcohol is Russia known for?" : ["Vodka", "Beer", "Wine", "Rum"], """What is the name of the city
that Spongebob Squarepants lives in?""" : ["Bikini Bottom", "Bikini Top", "Atlantas", "Seabed city"], """What’s the name of the company
that published the Mario Kart video game?""" : ["Nintendo", "Sony", "Sega", "Microsoft"], "Which country hosted the first Olympic Games in 1896?" : ["Greece", "Italy", "China", "USA"], "What do you call a geometric space with 5 sides?" : ["Pentagon", "Octagon", "Hexagon", "Heptagon"], "Who built the Great Wall of China?" : ["The Qin Dynasty", "The Ming Dynasty", "The Han Dynasty", "The Qing Dynasty"], "What is 5 x 30?" : ["150", "200", "300", "450"], "What is the capital of Japan?" : ["Tokyo", "Kyoto", "Osaka", "Hiroshima"], "How many days are in a leap year?" : ["366", "365", "342", "372"], "What year was Jesus Christ born?" : ["Between 6-4 B.C", "Between 27-29 A.D", "0 B.C", "Between 6-4 A.D"], """What is the scientific name of the
process where plants prepare their food?""" : ["Photosynthesis", "Respiration", "Fermentation", "Cell Biology"], "What date is Christmas?" : ["December 25th", "December 26th", "December 27th", "December 24th"], "Which U.S. State is the largest?" : ["Alaska", "Texas", "Florida", "California"], "What war took place during the years 1939-1945?" : ["World War II", "World War I", "The Vietnam War", "The Korean War"], "Which two planets in our solar system are known as “ice giants”?" : ["Neptune and Uranus", "Jupiter and Saturn", "Saturn and Uranus", "Jupiter and Neptune"], "What animal is Bambi?" : ["Deer", "Cow", "Boar", "Antelope"], "What year did the 9/11 terror attacks happen?" : ["2001", "2000", "2002", "1999"], "What is the day after christmas known as?" : ["Boxing day", "Wrapping day", "Feasting day", "After Christmas day"], "What is the name of the Earth’s largest ocean?" : ["The Pacific Ocean", "The Atlantic Ocean", "The Indian Ocean", "The Arctic Ocean"], "Which two countries share the longest international border?" : ["Canada and the USA", "Russia and China", "Russia and Kazakhstan", "Mongolia and China"], "What is the smallest country in the world?" : ["Vatican city", "San Marino", "Monaco", "Liechtenstein"]} # Dictonairy for trivia questions and answers

def button(master, text, command): # definition for making a button
    bt = tk.Button(master, text=text, command=command)
    bt.pack(pady=2)

def label(master, text, background): # definition for label
    la = tk.Label(master, text=text, background=background)
    la.pack(pady=3)

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

class Window: # class for the main window
    def __init__(self): # This happens when the class is initilised
        self.img_path = "No path"
        self.state = 0
        self.math_done = "No"
        self.geography_done = "No"
        self.trivia_done = "No"
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.question = "There is no question"
        self.qnumber = 1
        self.score = 0
        self.name = "None"
        self.bg_colour = "light gray"
        self.white_get = "False"
        self.white_price = 1
        self.red_get = "False"
        self.red_price = 5
        self.blue_get = "False"
        self.blue_price = 5
        self.green_get = "False"
        self.green_price = 5
        self.yellow_get = "False"
        self.yellow_price = 10
        self.orange_get = "False"
        self.orange_price = 10
        self.purple_get = "False"
        self.purple_price = 15
        self.window = tk.Tk()
        self.window.title("Game by: Benjamin Rivett")
        self.window.geometry("400x300")
        self.window.config(background=self.bg_colour)
        self.scoref = tk.Frame(self.window, background=self.bg_colour)
        self.scoref.pack(anchor="ne")
        self.scorel = tk.Label(self.scoref, text="Score: {}".format(self.score), background=self.bg_colour)
        self.scorel.pack()
        self.main_menu()

    def main_menu(self): # This is the main menu
        self.menu_things = tk.Frame(self.window, background=self.bg_colour)
        label(self.menu_things, "Hello this is the title screen!", self.bg_colour)
        button(self.menu_things, "Play", self.start)
        button(self.menu_things, "Save Menu", self.save_menu)
        button(self.menu_things, "Shop", self.shop_menu)
        button(self.menu_things, "Exit", self.exit)
        self.menu_things.pack(pady=2)

    def save_menu(self): # this menu does save stuff
        self.state = 0
        self.menu_things.destroy()
        self.savef = tk.Frame(self.window, background=self.bg_colour)
        button(self.savef, "Save Game", self.save_file_def)
        button(self.savef, "Load Save", self.load_file)
        button(self.savef, "Reset Save", self.reset_file)
        button(self.savef, "Check Save", self.check_file)
        button(self.savef, "Back", self.back_menu)
        self.savef.pack(pady=2)

    def shop_menu(self):
        self.state = 2
        self.menu_things.destroy()
        self.shopf = tk.Frame(self.window, background=self.bg_colour)
        button(self.shopf, "Background colours", self.background_colours)
        button(self.shopf, "Back", self.back_menu)
        self.shopf.pack(pady=2)

    def background_colours(self):
        self.shopf.destroy()
        self.state = 3
        self.bg_change = tk.Frame(self.window, background=self.bg_colour)
        self.bg_change_left = tk.Frame(self.bg_change, background=self.bg_colour)
        self.bg_change_right = tk.Frame(self.bg_change, background=self.bg_colour)
        self.cl = tk.Label(self.bg_change, text="""Choose a background colour
Colours are bought using score""", background=self.bg_colour)
        self.cl.pack(pady=2)
        button(self.bg_change, "Default", self.bg_default)
        
        if self.white_get == "False":
            self.wb = tk.Button(self.bg_change_left, text="White: {}".format(self.white_price), command=self.bg_white)
            self.wb.pack(pady=2)
        else:
            self.wb = tk.Button(self.bg_change_left, text="White", command=self.bg_white)
            self.wb.pack(pady=2)
        
        if self.red_get == "False":
            self.rb = tk.Button(self.bg_change_left, text="Red: {}".format(self.red_price), command=self.bg_red)
            self.rb.pack(pady=2)
        else:
            self.rb = tk.Button(self.bg_change_left, text="Red", command=self.bg_red)
            self.rb.pack(pady=2)
        
        if self.blue_get == "False":
            self.bb = tk.Button(self.bg_change_left, text="Blue: {}".format(self.blue_price), command=self.bg_blue)
            self.bb.pack(pady=2)
        else:
            self.bb = tk.Button(self.bg_change_left, text="Blue", command=self.bg_blue)
            self.bb.pack(pady=2)
            
        self.bbt = tk.Button(self.bg_change, text="Back", command=self.back_menu)
        self.bbt.pack(pady=3, side="bottom")
        self.bg_change.pack(pady=2)
        self.bg_change_left.pack(side="left")
        self.bg_change_right.pack(side="right")

    def background_change(self):
        self.window.config(background=self.bg_colour)
        self.bg_change.config(background=self.bg_colour)
        self.bg_change_left.config(background=self.bg_colour)
        self.bg_change_right.config(background=self.bg_colour)
        self.cl.config(background=self.bg_colour)
        self.scorel.config(text="Score: {}".format(self.score), background=self.bg_colour)

    def bg_default(self):
        self.bg_colour = "light gray"
        self.background_change()
        simpledialog.messagebox._show("Success", "Background colour changed to the default colour")

    def colour(self, colour, colour_price, colour_get, bt):
        if colour_get == "False":
            if int(self.score) >= colour_price:
                self.bg_colour = colour
                self.score = int(self.score) - colour_price
                if colour == "white":
                    self.white_get = "True"
                elif colour == "red":
                    self.red_get = "True"
                elif colour == "blue":
                    self.blue_get = "True"
                
                bt.config(text=colour.capitalize())
                self.background_change()
                simpledialog.messagebox.showinfo("Success", "You have bought the {} background colour".format(colour))
            else:
                simpledialog.messagebox.showinfo("Failure", "You don't have enough score for this item")

        else:
            self.bg_colour = colour
            self.background_change()
            simpledialog.messagebox.showinfo("Success", "You have changed the background to {}".format(colour))
            
    def bg_white(self):
        self.colour("white", self.white_price, self.white_get, self.wb)
                
    def bg_red(self):
        self.colour("red", self.red_price, self.red_get, self.rb)

    def bg_blue(self):
        self.colour("blue", self.blue_price, self.blue_get, self.bb)

    def back_menu(self): # this is to go back to the main menu
        if self.state == 1:
            self.setting_things.destroy()
            self.main_menu()

        elif self.state == 2:
            self.shopf.destroy()
            self.main_menu()

        elif self.state == 3:
            self.bg_change.destroy()
            self.shop_menu()
            
        else:
            self.savef.destroy()
            self.main_menu()

    def read_file(self): # Definition for reading the save file
        self.save_file = open("Game/save.txt", "r")
        self.name = self.save_file.readline().strip()
        self.score = self.save_file.readline().strip()
        self.correct_answers = self.save_file.readline().strip()
        self.incorrect_answers = self.save_file.readline().strip()
        self.math_done = self.save_file.readline().strip()
        self.geograhpy_done = self.save_file.readline().strip()
        self.trivia_done = self.save_file.readline().strip()
        self.white_get = self.save_file.readline().strip()
        self.red_get = self.save_file.readline().strip()
        self.blue_get = self.save_file.readline().strip()
        self.save_file.close()
    
    def save_file_def(self): # Saves the players progress !!!For some reason doesn't work sometimes
        self.save_file = open("Game/save.txt", "w")
        self.save_file.writelines("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.name, self.score, self.correct_answers, self.incorrect_answers, self.math_done, self.geography_done, self.trivia_done, self.white_get, self.red_get, self.blue_get))
        self.save_file.close()
        tk.messagebox.showinfo(title="Save Game", message="Your game has been saved!")
        
    def load_file(self): # loads the players progress
        self.read_file()
        self.scorel.config(text="Score: {}".format(self.score))
        tk.messagebox.showinfo(title="Load Save", message="Your save has been loaded")

    def reset_file(self): # Definition for reseting the save file
        self.save_file = open("Game/save.txt", "w")
        self.save_file.writelines("None\n0\n0\n0\nNo\nNo\nNo\nFalse\nFalse\nFalse")
        self.bg_colour = "light gray"
        self.window.config(bg=self.bg_colour)
        self.scorel.config(bg=self.bg_colour)
        self.savef.config(bg=self.bg_colour)
        self.save_file.close()
        self.read_file()
        self.scorel.config(text="Score: {}".format(self.score))
        tk.messagebox.showinfo(title="Reset Save", message="Your save has been reset!")

    def check_file(self): # Definition for cheaking the save file
        self.read_file()
        tk.messagebox.showinfo(title="Check Save", message="""Name = {}
Score = {}
Correct Answers = {}
Incorrect Answers = {}
Done Math questions = {}
Done Geography questions = {}
Done Trivia questions = {}
White = {} 
Red = {} 
Blue = {}""".format(self.name, self.score, self.correct_answers, self.incorrect_answers, self.math_done, self.geograhpy_done, self.trivia_done, self.white_get, self.red_get, self.blue_get))
    
    def exit(self): # used when exiting the progam
        if messagebox.askyesno(title="Exit", message="Are you sure?"):
            self.window.destroy()
            
    def start(self): # this starts the game
        self.state = 1
        self.menu = StringVar()
        self.menu.set("Empty")
        self.menu_things.destroy()
        self.setting_things = tk.Frame(self.window, background=self.bg_colour)
        self.label = tk.Label(self.setting_things, text="Name: {}".format(self.name), background=self.bg_colour)
        self.label.pack(pady=2)
        button(self.setting_things, "Set your name", self.set_name)
        label(self.setting_things, "What are you going to play?", self.bg_colour)
        self.play_option = tk.OptionMenu(self.setting_things, self.menu, *option_menu)
        self.play_option.pack(pady=2)
        button(self.setting_things, "Continue", self.next)
        button(self.setting_things, "Back", self.back_menu)
        self.setting_things.pack(pady=2)

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
    
    def set_name(self): #sets name # for some reason setting name breaks the save game button
        self.name = simpledialog.askstring("Pick your Name", "Name:")
        if self.name == "":
            self.name = "None"

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
            if self.qnumber < 11:
                self.img_path, self.answer = random.choice(list(flag_dict.items()))
                image(self.geography_qf, self.img_path, 180, 100)
                self.question = "What country does this flag belong too?"
                
            else:
                self.question = """Well done {}!
You have completed the Geography questions.""".format(self.name)
                
        elif self.option == "Trivia":
            if self.qnumber < 11:
                self.question, self.rc_list = random.choice(list(trivia_dict.items()))
                
                
                
            else:
                self.question = """Well done {}!
You have completed the Trivia questions.""".format(self.name)

        else:
            Error()
    
    def math(self): # This starts the math questions
        self.setting_things.destroy()
        self.math_stuff = tk.Frame(self.window, background=self.bg_colour)
        
        if self.math_done == "No":
            label(self.math_stuff, "You have NOT done the Math questions.", self.bg_colour)
        else:
            label(self.math_stuff, "You have done the Math questions.", self.bg_colour)
            
        label(self.math_stuff, """{}, This area of the game will test your knoledge
on Mathmatics, starting with addition and subtraction
then moving on to multiplication and divition.""".format(self.name), self.bg_colour)
        button(self.math_stuff, "Continue", self.math_questions)
        button(self.math_stuff, "Back", self.back)
        self.math_stuff.pack(pady=2)

    def done(self): # this is for when the player is done answering the questions
        self.completef.destroy()
        self.start()
        self.qnumber = 1
            
    def geography(self): # This starts the geography questions
        self.setting_things.destroy()
        self.geography_stuff = tk.Frame(self.window, background=self.bg_colour)
        
        if self.geography_done == "No":
            label(self.geography_stuff, "You have NOT done the Geography questions.", self.bg_colour)
        else:
            label(self.geography_stuff, "You have done the Geography questions.", self.bg_colour)
            
        label(self.geography_stuff, """{}, This area of the game will test your knoledge
on Geography, this will incluce naming the country
based on its siluete as well as its flag.""".format(self.name), self.bg_colour)
        button(self.geography_stuff, "Continue", self.geography_questions)
        button(self.geography_stuff, "Back", self.back)
        self.geography_stuff.pack(pady=2)

    def trivia(self): # This starts the trivia questions
        self.setting_things.destroy()
        self.trivia_stuff = tk.Frame(self.window, background=self.bg_colour)
        
        if self.trivia_done == "No":
            label(self.trivia_stuff, "You have NOT done the Trivia questions.", self.bg_colour)
        else:
            label(self.trivia_stuff, "You have done the Trivia questions.", self.bg_colour)
            
        label(self.trivia_stuff, """{}, This area of the game will test your knoledge
on random Trivia, this will include questions on anything.""".format(self.name), self.bg_colour)
        button(self.trivia_stuff, "Continue", self.trivia_questions)
        button(self.trivia_stuff, "Back", self.back)
        self.trivia_stuff.pack(pady=2)
        
    def math_questions(self): # This is the math questions
        if self.qnumber == 11:
            self.completef = tk.Frame(self.window, background=self.bg_colour)
            label(self.completef, self.question, self.bg_colour)
            label(self.completef, """Your score is {}.
You have gotten {} correct answers,
You have gotten {} incorrect answers.""".format(self.score, self.correct_answers, self.incorrect_answers), self.bg_colour)
            self.math_done = "Yes"
            button(self.completef, "Continue", self.done)
            self.completef.pack(pady=2)
        else:
            self.math_stuff.destroy()
            self.math_qf = tk.Frame(self.window, background=self.bg_colour)
            self.setting_question()
            label(self.math_qf, """Question {}:
{}""".format(self.qnumber, self.question), self.bg_colour)
            self.aentry = tk.Entry(self.math_qf)
            self.aentry.pack()
            button(self.math_qf, "Submit", self.submit)
            self.math_qf.pack(pady=2)
                
    def geography_questions(self): # this sets the geography questions 
        if self.qnumber == 11:
            self.completef = tk.Frame(self.window, background=self.bg_colour)
            label(self.completef, self.question, self.bg_colour)
            label(self.completef, """Your score is {}.
You have gotten {} correct answers,
You have gotten {} incorrect answers.""".format(self.score, self.correct_answers, self.incorrect_answers), self.bg_colour)
            self.geography_done = "Yes"
            button(self.completef, "Continue", self.done)
            self.completef.pack(pady=2)
        else:
            self.geography_stuff.destroy()
            self.geography_qf = tk.Frame(self.window, background=self.bg_colour)
            self.geography_qf.pack(pady=2)
            self.setting_question()
            label(self.geography_qf, """Question {}:
{}""".format(self.qnumber, self.question), self.bg_colour)
            self.geo_choices()

    def geo_choices(self):
        self.rc_list = []
        self.ln = [0, 1, 2, 3]
        while self.answer not in self.rc_list:
            if len(self.rc_list) == 4:
                self.rc_list.pop(0)
            while len(self.rc_list) !=4:
                random.shuffle(self.ln)
                self.rc_list.append(random.choice(list(flag_dict.values())))
                                

        self.button_frame1 = tk.Frame(self.geography_qf, background=self.bg_colour)
        self.button_frame2 = tk.Frame(self.geography_qf, background=self.bg_colour)
        self.choice_1 = tk.Button(self.button_frame1, text=self.rc_list[self.ln[0]], command=self.c1)
        self.choice_1.pack(side="left")
        self.choice_2 = tk.Button(self.button_frame1, text=self.rc_list[self.ln[1]], command=self.c2)
        self.choice_2.pack(side="right")
        self.choice_3 = tk.Button(self.button_frame2, text=self.rc_list[self.ln[2]], command=self.c3)
        self.choice_3.pack(side="left")
        self.choice_4 = tk.Button(self.button_frame2, text=self.rc_list[self.ln[3]], command=self.c4)
        self.choice_4.pack(side="right")
        self.button_frame1.pack(pady=2)
        self.button_frame2.pack(pady=2)

    def trivia_choices(self):
        self.ln = [0, 1, 2, 3]
        self.answer = self.rc_list[0]
        random.shuffle(self.ln)
        
        self.button_frame1 = tk.Frame(self.trivia_qf, background=self.bg_colour)
        self.button_frame2 = tk.Frame(self.trivia_qf, background=self.bg_colour)
        self.choice_1 = tk.Button(self.button_frame1, text=self.rc_list[self.ln[0]], command=self.c1)
        self.choice_1.pack(side="left")
        self.choice_2 = tk.Button(self.button_frame1, text=self.rc_list[self.ln[1]], command=self.c2)
        self.choice_2.pack(side="right")
        self.choice_3 = tk.Button(self.button_frame2, text=self.rc_list[self.ln[2]], command=self.c3)
        self.choice_3.pack(side="left")
        self.choice_4 = tk.Button(self.button_frame2, text=self.rc_list[self.ln[3]], command=self.c4)
        self.choice_4.pack(side="right")
        self.button_frame1.pack(pady=10)
        self.button_frame2.pack()
        
    def c1(self):
        self.player_answer = self.rc_list[self.ln[0]]
        self.answer_check()
                
    def c2(self):
        self.player_answer = self.rc_list[self.ln[1]]
        self.answer_check()

    def c3(self):
        self.player_answer = self.rc_list[self.ln[2]]
        self.answer_check()

    def c4(self):
        self.player_answer = self.rc_list[self.ln[3]]
        self.answer_check()


    def trivia_questions(self):
        if self.qnumber == 11:
            self.completef = tk.Frame(self.window, background=self.bg_colour)
            label(self.completef, self.question, self.bg_colour)
            label(self.completef, """Your score is {}.
You have gotten {} correct answers,
You have gotten {} incorrect answers.""".format(self.score, self.correct_answers, self.incorrect_answers), self.bg_colour)
            self.trivia_done = "Yes"
            button(self.completef, "Continue", self.done)
            self.completef.pack(pady=2)
        else:
            self.trivia_stuff.destroy()
            self.trivia_qf = tk.Frame(self.window, background=self.bg_colour)
            self.trivia_qf.pack(pady=2)
            self.setting_question()
            label(self.trivia_qf, """Question {}:
{}""".format(self.qnumber, self.question), self.bg_colour)
            self.trivia_choices()
            
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
                self.correct = tk.Frame(self.window, background=self.bg_colour)
                self.correct_answers = str(int(self.correct_answers) + 1)
                label(self.correct, "Well done {} was the correct answer!".format(self.answer), self.bg_colour)
                button(self.correct, "Next question", self.intermission)
                self.correct.pack(pady=2)
                self.score = self.score + 1
                self.scorel.config(text="Score: {}".format(self.score))
                
            else:
                self.math_qf.destroy()
                self.incorrect = tk.Frame(self.window, background=self.bg_colour)
                self.incorrect_answers = str(int(self.incorrect_answers) + 1)
                label(self.incorrect, """Im sorry but {} was not the correct answer.
The correct answer was {}.""".format(self.player_answer, self.answer), self.bg_colour)
                button(self.incorrect, "Next question", self.intermission)
                self.incorrect.pack(pady=2)
                self.score = self.score - 1
                self.scorel.config(text="Score: {}".format(self.score))
                
                
        elif self.option == "Geography":
            if self.player_answer == self.answer:
                self.geography_qf.destroy()
                self.correct = tk.Frame(self.window, background=self.bg_colour)
                self.correct_answers = str(int(self.correct_answers) + 1)
                label(self.correct, "Well done {} was the correct answer!".format(self.answer), self.bg_colour)
                button(self.correct, "Next question", self.intermission)
                self.correct.pack(pady=2)
                self.score = self.score + 1
                self.scorel.config(text="Score: {}".format(self.score))

            else:
                self.geography_qf.destroy()
                self.incorrect = tk.Frame(self.window, background=self.bg_colour)
                self.incorrect_answers = str(int(self.incorrect_answers) + 1)
                label(self.incorrect, """Im sorry but {} was not the correct answer.
The correct answer was {}.""".format(self.player_answer, self.answer), self.bg_colour)
                button(self.incorrect, "Next question", self.intermission)
                self.incorrect.pack(pady=2)
                self.score = self.score - 1
                self.scorel.config(text="Score: {}".format(self.score))
                
        elif self.option == "Trivia":
            if self.player_answer == self.answer:
                self.trivia_qf.destroy()
                self.correct = tk.Frame(self.window, background=self.bg_colour)
                self.correct_answers = str(int(self.correct_answers) + 1)
                label(self.correct, "Well done {} was the correct answer!".format(self.answer), self.bg_colour)
                button(self.correct, "Next question", self.intermission)
                self.correct.pack(pady=2)
                self.score = self.score + 1
                self.scorel.config(text="Score: {}".format(self.score))

            else:
                self.trivia_qf.destroy()
                self.incorrect = tk.Frame(self.window, background=self.bg_colour)
                self.incorrect_answers = str(int(self.incorrect_answers) + 1)
                label(self.incorrect, """Im sorry but {} was not the correct answer.
The correct answer was {}.""".format(self.player_answer, self.answer), self.bg_colour)
                button(self.incorrect, "Next question", self.intermission)
                self.incorrect.pack(pady=2)
                self.score = self.score - 1
                self.scorel.config(text="Score: {}".format(self.score))

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