import tkinter as tk


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

    def exit(self):
        self.exit=tk.Tk()
        self.exit.title("Exit")
        self.label=tk.Label(self.exit, text="Are you sure?")
        self.label.pack()
        self.bt1=tk.Button(self.exit, text="Yes", command=self.close)
        self.bt1.pack(side="left")
        self.bt2=tk.Button(self.exit, text="No", command=self.exit.destroy)
        self.bt2.pack(side="right")
    def close(self): # this need fixing
        self.exit.destroy
        self.menu.destroy
        
        self.menu.mainloop()
        
        
class Settings:
    def __init__(self):
        option=tk.Tk()
        option.title("Settings")
        option.geometry("200x200")
        obt1=tk.Button(option, text="Exit", command=option.destroy)
        obt1.place(relx = .5, rely = .5, anchor="center")
        
Menu()