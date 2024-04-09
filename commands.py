import os
import requests
import shutil
import zipfile

class Commands:
    @staticmethod
    def create_file(filename):
        try:
            with open(filename, 'w') as file:
                file.write("")  
            print(f"File '{filename}' created successfully.")
        except FileNotFoundError:
            print("Error: Could not create file.")
  
    @staticmethod
    def redirect_to_website():
        print("Redirecting to the developer's official website (https://awortu.000webhostapp.com)")

    @staticmethod
    def change_directory(directory_name):
        try:
            os.chdir(directory_name)
            print(f"Changed directory to '{directory_name}'")
        except FileNotFoundError:
            print(f"Directory '{directory_name}' not found.")

    @staticmethod
    def list_directory_contents():
        print("Contents of current directory:")
        for item in os.listdir():
            print(f"- {item}")

    @staticmethod
    def make_directory(directory_name):
        try:
            os.mkdir(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")

    @staticmethod
    def print_working_directory():
        print(f"Current directory: {os.getcwd()}")

    @staticmethod
    def copy_file(source_file):
        try:
            destination_file = os.path.join(os.getcwd(), os.path.basename(source_file))
            if os.path.exists(destination_file):
                print(f"File '{os.path.basename(destination_file)}' already exists in the current directory.")
                return
            shutil.copy(source_file, os.getcwd())
            print(f"File '{os.path.basename(source_file)}' copied successfully.")
        except FileNotFoundError:
            print(f"Error: File '{source_file}' not found.")

    @staticmethod
    def move_file(source, destination):
        try:
            shutil.move(source, destination)
            print(f"File '{source}' moved to '{destination}'.")
        except FileNotFoundError:
            print("Error: One or more files not found.")

    @staticmethod
    def remove_file_or_directory(name):
        try:
            if os.path.isdir(name):
                shutil.rmtree(name)
                print(f"Directory '{name}' and its contents deleted successfully.")
            elif os.path.isfile(name):
                os.remove(name)
                print(f"File '{name}' deleted successfully.")
            else:
                print(f"Error: '{name}' not found.")
        except OSError:
            print(f"Error: Unable to delete '{name}'.")

    @staticmethod
    def display_file_contents(filename):
        try:
            with open(filename, 'r') as file:
                print(f"Contents of '{filename}':")
                print(file.read())
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    @staticmethod
    def write_to_file(filename):
        try:
            with open(filename, 'a') as file:
                print("Enter text (press Ctrl + S to save and exit):")
                while True:
                    text = input()
                    file.write(text)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")


    @staticmethod
    def display_help():
        print("""
        Available commands:
        - cd <directory_name>: Change directory.
        - ls: List directory contents.
        - mkdir <directory_name>: Make a directory.
        - pwd: Print current working directory.
        - cp <source_file> <destination>: Copy a file.
        - mv <source> <destination>: Move a file.
        - rm <filename_or_directory>: Remove a file or directory.
        - cat <filename>: Display file contents.
        - touch <filename>: Create a new file.
        - writein <filename>: Write to a file.
        - download <url>: Download a file from a URL.
        - help: Display this help message.
        - whoispoco: Display developer information.
        - back: Navigate back one directory.
        - ..: Navigate back two directories.
        - rename <old_name> <new_name>: Rename a file or directory.
        - zip <filename> <file1> <file2> ...: Create a zip archive containing the specified files.
        - unzip <filename>: Extract files from a zip archive.
        - view: Print the directory of the current file for viewing in a web browser.
        """)

    @staticmethod
    def who_is_poco():
        print("Hi! My name is Awortu Ibenem, also known as Poco The Clown. I'm a Website Developer.")

    @staticmethod
    def download(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                filename = url.split("/")[-1]
                downloads_dir = os.path.join(os.getcwd(), "directories", "Downloads")
                if not os.path.exists(downloads_dir):
                    os.makedirs(downloads_dir)
                with open(os.path.join(downloads_dir, filename), 'wb') as file:
                    file.write(response.content)
                print(f"File '{filename}' downloaded successfully.")
            else:
                print("Error: Unable to download the file.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def rename(old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"Successfully renamed '{old_name}' to '{new_name}'.")
        except FileNotFoundError:
            print("Error: One or more files not found.")

    @staticmethod
    def zip_files(zip_filename, *files):
        try:
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for file in files:
                    zipf.write(file)
            print(f"Successfully created zip archive '{zip_filename}' containing the specified files.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def unzip(zip_filename):
        try:
            with zipfile.ZipFile(zip_filename, 'r') as zipf:
                zipf.extractall()
            print(f"Successfully extracted files from '{zip_filename}'.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def view():
        current_directory = os.getcwd()
        print(f"You can view the current directory by copying and pasting the following link into your web browser: file://{current_directory}")
        
    @staticmethod
    def clean():
        if os.name == 'nt':  
            os.system('cls')
        else:  
            os.system('clear')
