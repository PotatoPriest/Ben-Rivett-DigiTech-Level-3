import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class User:
    def __init__(self):
        self.username_change()
        self.Uname = "none"
        
    def username_change(self):
        self.Uname = simpledialog.askstring( "Username", "What is your name?")

    def __str__(self):
        return self.Uname
        
class Menu: #Main menu class
    def __init__(self):
        self.name = User() #bruh
        self.menu=tk.Tk()
        self.menu.title("Main Menu")
        self.menu.geometry("400x300")
        
        self.label = tk.Label(self.menu, text="MAIN MENU")
        self.label.pack()
        self.namelabel = tk.Label(self.menu, text="Username: {}".format(self.name))
        self.namelabel.pack()
        
        self.menubts = tk.Frame(self.menu, bg="green")
        self.menubts.place(relx = .5, rely = .5, anchor="center")
        
        self.bt1 = tk.Button(self.menubts, text="Play")
        self.bt1.pack(pady=5)
        
        self.bt2 = tk.Button(self.menubts, text="Settings", command=Settings)
        self.bt2.pack(pady=5)
        
        self.bt3 = tk.Button(self.menubts, text="Exit", command=self.exit)
        self.bt3.pack(pady=5)

        self.menu.protocol("WM_DELETE_WINDOW", self.exit)
        self.menu.mainloop()
        
    def exit(self):
        if messagebox.askyesno(title="Exit", message="Are you sure?"):
            self.menu.destroy()
            
class Settings:
    def __init__(self):
        
        self.option=tk.Tk()
        self.option.title("Settings")
        self.option.geometry("200x200")
        self.obt1=tk.Button(self.option, text="Exit", command=self.option.destroy)
        self.obt1.place(relx=0.5, rely=0.9, anchor="s")
        self.obt2=tk.Button(self.option, text="Name change", command=User)
        self.obt2.pack()
        self.obt3=tk.Button(self.option, text="nill", command="nill")
        self.obt3.pack()


Menu()