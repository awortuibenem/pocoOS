import tkinter as tk
from welcome_page_logic import WelcomePageLogic

class WelcomePage:
    def __init__(self, master):
        self.master = master
        master.title("Welcome to PocoOS")
        master.configure(bg="#262626")  

class WelcomePage:
    def __init__(self, master, show_sign_up_page, show_sign_in_page):
        self.master = master
        master.title("Welcome to PocoOS")
        master.configure(bg="#262626")  
        
        width = 800
        height = 600
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.welcome_label = tk.Label(master, text="Welcome to PocoOS", font=("Helvetica", 24, "bold"), fg="white", bg="#262626")
        self.welcome_label.pack(pady=(100, 10))

        self.developer_label = tk.Label(master, text="Developed By Awortu Ibenem", font=("Helvetica", 14), fg="white", bg="#262626")
        self.developer_label.pack()

        self.button_frame = tk.Frame(master, bg="#262626")
        self.button_frame.pack(pady=20)

        self.sign_up_button = tk.Button(self.button_frame, text="Sign Up", font=("Helvetica", 12), bg="#444444", fg="white", width=10, command=show_sign_up_page)
        self.sign_up_button.pack(side=tk.LEFT, padx=10)

        self.sign_in_button = tk.Button(self.button_frame, text="Sign In", font=("Helvetica", 12), bg="#444444", fg="white", width=10, command=show_sign_in_page)
        self.sign_in_button.pack(side=tk.LEFT, padx=10)

