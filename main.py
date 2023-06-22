import tkinter as tk
from tkinter import messagebox

class Menu: #Main menu class
    def __init__(self):
        self.menu=tk.Tk()
        self.menu.title("Main Menu")
        self.menu.geometry("400x300")
        
        self.label = tk.Label(self.menu, text="MAIN MENU")

        self.label.pack()
    
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
        
        option=tk.Tk()
        option.title("Settings")
        option.geometry("200x200")
        obt1=tk.Button(option, text="Exit", command=option.destroy)
        obt1.place(relx=0.5, rely=0.9, anchor="s")
        obt2=tk.Button(option, text="Name change", command=User)
        obt2.pack()
        obt3=tk.Button(option, text="nill", command="nill")
        obt3.pack()


class User:
    pass


Menu()