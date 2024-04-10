import tkinter as tk
from WelcomePage import WelcomePage

def show_sign_up_page():
    root.destroy()  
    import SignUpPage 

def show_sign_in_page():
    root.destroy()  
    import SignInPage  

def show_welcome_page():
    global root  
    root = tk.Tk()  
    welcome_page = WelcomePage(root, show_sign_up_page, show_sign_in_page)  
    root.mainloop()  

if __name__ == "__main__":
    show_welcome_page()  
