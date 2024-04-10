import tkinter as tk
import tkinter as tk
import os
import hashlib
from commands import Commands


class SignUpPage:
    def __init__(self, master):
        self.master = master
        master.title("Sign Up")
        master.configure(bg="#262626")  
        
        width = 400
        height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.title_label = tk.Label(master, text="Sign Up", font=("Helvetica", 24, "bold"), fg="white", bg="#262626")
        self.title_label.pack(pady=20)

        self.username_label = tk.Label(master, text="Username:", font=("Helvetica", 12), fg="white", bg="#262626")
        self.username_label.pack()
        self.username_entry = tk.Entry(master, font=("Helvetica", 12))
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:", font=("Helvetica", 12), fg="white", bg="#262626")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*", font=("Helvetica", 12))
        self.password_entry.pack()

        self.email_label = tk.Label(master, text="Email:", font=("Helvetica", 12), fg="white", bg="#262626")
        self.email_label.pack()
        self.email_entry = tk.Entry(master, font=("Helvetica", 12))
        self.email_entry.pack()

        self.sign_up_button = tk.Button(master, text="Sign Up", font=("Helvetica", 12), bg="#444444", fg="white", command=self.sign_up)
        self.sign_up_button.pack(pady=10)

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with open("user_database.txt", "a") as file:
            file.write(f"{username}:{hashed_password}\n")
        
        print("User account created successfully.")
        self.open_login()

    def open_login(self):
        self.master.destroy()

root = tk.Tk()
sign_up_page = SignUpPage(root)
root.mainloop()
