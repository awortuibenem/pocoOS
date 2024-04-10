import tkinter as tk
import os
import hashlib

class SignInPage:
    def __init__(self, master):
        self.master = master
        master.title("Sign In")
        master.configure(bg="#262626")  
        
        width = 400
        height = 300
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.title_label = tk.Label(master, text="Sign In", font=("Helvetica", 24, "bold"), fg="white", bg="#262626")
        self.title_label.pack(pady=20)

        self.username_label = tk.Label(master, text="Username:", font=("Helvetica", 12), fg="white", bg="#262626")
        self.username_label.pack()
        self.username_entry = tk.Entry(master, font=("Helvetica", 12))
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:", font=("Helvetica", 12), fg="white", bg="#262626")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*", font=("Helvetica", 12))
        self.password_entry.pack()

        self.sign_in_button = tk.Button(master, text="Sign In", font=("Helvetica", 12), bg="#444444", fg="white", command=self.sign_in)
        self.sign_in_button.pack(pady=10)

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if self.authenticate_user(username, hashed_password):
            print(f"Successfully Logged in as: {username}")
            self.open_desktop()
        else:
            print("Invalid username or password.")

    def authenticate_user(self, username, hashed_password):
        # Check if username and hashed_password exist in the user database file
        with open("user_database.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username and hashed_password == stored_password:
                    return True
        return False

    def open_desktop(self):
        self.master.destroy()
        import desktop

root = tk.Tk()
sign_in_page = SignInPage(root)
root.mainloop()
