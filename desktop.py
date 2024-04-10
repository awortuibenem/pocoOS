import tkinter as tk
from PIL import Image, ImageTk

class DesktopView:
    def __init__(self, master):
        self.master = master
        master.title("PocoOS Desktop")
        master.configure(bg="#262626")  
        
        width = 800
        height = 600
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.create_icon("pfp.png", "Dev", 0, 0, self.open_dev)
        self.create_icon("pfp.png", "File Explorer", 1, 0, self.open_file_explorer)
        self.create_icon("pfp.png", "Web Browser", 2, 0, self.open_web_browser)

    def create_icon(self, image_path, text, row, column, command):
        icon_image = Image.open(image_path)
        icon_image = icon_image.resize((64, 64), Image.LANCZOS) 
        icon_image = ImageTk.PhotoImage(icon_image)
        icon_button = tk.Button(self.master, image=icon_image, text=text, font=("Helvetica", 10), bg="#262626", fg="white", compound=tk.TOP, command=command)
        icon_button.image = icon_image  
        icon_button.grid(row=row, column=column, padx=10, pady=10)

    def open_dev(self):
        print("Opening Dev...")

    def open_file_explorer(self):
        print("Opening File Explorer...")

    def open_web_browser(self):
        print("Opening Web Browser...")

root = tk.Tk()
desktop_view = DesktopView(root)
root.mainloop()
