import os
from commands import Commands

class PocoOS:
    def __init__(self):
        self.default_directories = ["Downloads", "Pictures", "Videos", "Audio", "Documents"]
        self.current_directory = os.getcwd()

    def show_welcome_page(self):
        print("Welcome to PocoOS! Developed by Awortu Ibenem")
        print("Directories:")
        for directory in self.default_directories:
            print(f"- {directory}")

    def enter_directory(self, directory_name):
        if directory_name in self.default_directories:
            path = os.path.join("directories", directory_name)
            if os.path.exists(path):
                os.chdir(path)
                self.current_directory = os.getcwd()
                print(f"Entered directory: {directory_name}")
            else:
                print(f"Directory '{directory_name}' does not exist.")
        else:
            print(f"Invalid directory name: {directory_name}")

    def run(self):
        self.show_welcome_page()

        while True:
            user_input = input("Enter a command or directory name (type 'exit' to quit): ")
            if user_input.lower() == "exit":
                print("Exiting PocoOS.")
                break
            elif user_input.startswith("cd "):
                self.enter_directory(user_input[3:])
            elif user_input == "ls":
                Commands.list_directory_contents()
            elif user_input == "pwd":
                Commands.print_working_directory()
            elif user_input.startswith("create "):
                Commands.create_file(user_input[7:])
            elif user_input.startswith("cp "):
                Commands.copy_file(*user_input[3:].split())
            elif user_input.startswith("mv "):
                Commands.move_file(*user_input[3:].split())
            elif user_input.startswith("rm "):
                Commands.remove_file_or_directory(user_input[3:])
            elif user_input.startswith("cat "):
                Commands.display_file_contents(user_input[4:])
            elif user_input.startswith("touch "):
                Commands.create_file(user_input[6:])
            elif user_input.startswith("writein "):
                Commands.write_to_file(user_input[8:])
            elif user_input.startswith("mkdir "):
                Commands.make_directory(user_input[6:])
            elif user_input.startswith("download "):
                Commands.download(user_input[9:])
            elif user_input == "help":
                Commands.display_help()
            elif user_input == "whoispoco":
                Commands.who_is_poco()
            elif user_input == "back":
                Commands.change_directory("..")
            elif user_input == "..":
                Commands.change_directory("../..")
            elif user_input.startswith("rename "):
                old_name, new_name = user_input[7:].split()
                Commands.rename(old_name, new_name)
            elif user_input.startswith("zip "):
                zip_filename, *files = user_input[4:].split()
                Commands.zip_files(zip_filename, *files)
            elif user_input.startswith("unzip "):
                Commands.unzip(user_input[6:])
            elif user_input == "view":
                Commands.view()
            elif user_input == "clear":
                Commands.clean()
            else:
                print(f"Command '{user_input}' not recognized. Type 'help' to get a list of commands.")

if __name__ == "__main__":
    poco_os = PocoOS()
    poco_os.run()
