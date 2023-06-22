import tkinter as tk


class Menu():
    def __init__(self):
        menu=tk.Tk()
        menu.title("Main Menu")
        menu.geometry("400x300")
        
        label = tk.Label(menu, text="MAIN MENU")

        label.pack()

        menubts = tk.Frame(menu, bg="green")
        menubts.place(relx = .5, rely = .5, anchor="center")
        
        bt1 = tk.Button(menubts, text="Play")
        bt1.pack(pady=5)
        
        bt2 = tk.Button(menubts, text="Settings", command=Settings)
        bt2.pack(pady=5)
        
        bt3 = tk.Button(menubts, text="Exit", command=menu.destroy)
        bt3.pack(pady=5)
        
        tk.mainloop()

class Settings():
    def __init__(self):
        option=tk.Tk()
        option.title("Settings")
        option.geometry("200x200")
        obt1=tk.Button(option, text="Exit", command=option.destroy)
        obt1.place(relx = .5, rely = .5, anchor="center")
        
Menu()