import subprocess
import platform
import os
import time
import random

class System:
    def __init__(self):
        self.clear_screen()
        self.username = input("What's your name? > ")
        self.password = input("your new password > ")
        self.base_directory = os.getcwd()
        print(f"You're using your host system to work with the file system!\nCurrent working directory: {self.base_directory}")
        self.RunOS(self.username)
    
    def clear_screen(self):
        if platform.system() == "Windows":
            subprocess.run("cls", shell=True)
        else:
            subprocess.run("clear", shell=True)

    def delete_file(self, filename):
        if os.path.isfile(filename):
            if platform.system() == "Windows":
                subprocess.run(["del", filename], shell=True)
            else:
                subprocess.run(["rm", filename])
        else:
            print("Invalid target: not a file")

    def delete_folder(self, foldername):
        if os.path.isdir(foldername):
            if platform.system() == "Windows":
                subprocess.run(["rmdir", "/s", "/q", foldername], shell=True)
            else:
                subprocess.run(["rm", "-r", foldername])
        else:
            print("Invalid target: not a folder")

    def list_directory(self):
        if platform.system() == "Windows":
            subprocess.run("dir", shell=True)
        else:
            subprocess.run("ls", shell=True)

    def change_directory(self, directory):
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print("Directory not found.")
        except PermissionError:
            print("Permission denied to change directory.")

    def execute_python_command(self, command):
        if platform.system() == "Windows":
            subprocess.run(f"python {command}", shell=True) or subprocess.run(f"python3 {command}", shell=True)
        else:
            subprocess.run(f"python3 {command}", shell=True)

    def install_python_lib(self, libname):
        if platform.system() == "Windows":
            subprocess.run(f"pip install {libname}", shell=True) or subprocess.run(f"pip3 install {libname}", shell=True)
        else:
            subprocess.run(f"pip3 install {libname}", shell=True)

    def date(self):
        current_date = time.strftime("%Y-%m-%d", time.localtime())
        print(f"Current date: {current_date}")

    def calculator(self):
        expression = input("Enter an expression: ")
        try:
            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

    def reminder(self):
        reminder_text = input("Enter your reminder: ")
        reminder_time = input("Enter reminder time (HH:MM): ")
        print(f"Reminder set: {reminder_text} at {reminder_time}")

    def RunOS(self, username):
        print("+------------------------------+")
        print("|                              |")
        print("|  pythonOS 1.5 by jose icaro  |")
        print("|        made with love        |")
        print("|    98% me and 2% chatgpt     |")
        print("|                              |")
        print("+------------------------------+")
        while True:
            cwd = os.getcwd()
            command = input(f"\n{username}/pythonOS {cwd} >$ ")
            if command.startswith("print"):
                message = command.split("-s ")[1].split(" -e")[0].strip("\"\'")
                print(message)
            elif command.startswith("vim"):
                filename = command.split(" ")[1].strip("\"\'")
                subprocess.run(f"vim {filename}", shell=True)
            elif command.startswith("crte"):
                typename = command.split(" --type ")[1].split(" ")[0].strip("\"\'")
                itemname = command.split(" --name ")[1].strip("\"\'")
                if typename.startswith("file"):
                    if platform.system == "Windows":
                        subprocess.run(f'echo "" >> {itemname}', shell=True)
                    else:
                        subprocess.run(f"touch {itemname}", shell=True)
                elif typename.startswith("folder"):
                    subprocess.run(f"mkdir {itemname}", shell=True)
                else:
                    print("Unknown item type, use 'file' or 'folder'")
            elif command.startswith("delete"):
                target = command.split(" ")[1].strip("\"\'")
                if os.path.isfile(target):
                    self.delete_file(target)
                elif os.path.isdir(target):
                    self.delete_folder(target)
                else:
                    print("Invalid target: file or folder does not exist.")
            elif command.startswith("shutdown"):
                print("shutting down...")
                time.sleep(2)
                print("only one more second...")
                time.sleep(1)
                self.clear_screen()
                break
            elif command.startswith("start"):
                app = command.split(" ")[1].strip("\"\'")
                if app.lower() == "fakechat":
                    fakeperson = input("Fake person name > ")
                    print("Use 'exit' to stop the chat")
                    while True:
                        yourmessage = input(f"{username} > ")
                        print(yourmessage)
                        fakemessage = input(f"{fakeperson} > ")
                        print(fakemessage)
                        if yourmessage == "exit" or fakemessage == "exit":
                            break
                elif app.lower() == "-a":
                    print("Existing apps:")
                    print("1 - fakechat")
                    print("2 - guesstnumber")
                elif app.lower() == "guesstnumber":
                    veripassword = input("what's your password? >$ ")
                    if veripassword != self.password:
                        print("password incorrect. try your real password!")
                    else:
                        self.clear_screen()
                        print("correct password. now play!")
                        print("try put 10+ numbers or 0- numbers to exit the game")
                        while True:
                            guessnumber = int(input("guess the number of 1 to 10 > "))
                            self.clear_screen()
                            number = random.randint(1,10)
                            if guessnumber == number:
                                print("correct number. play again!")
                            elif guessnumber > 10 or guessnumber < 1:
                                print("exiting the game")
                                break
                            else:
                                print("incorrect number. play again!")
            elif command.startswith("help"):
                print("print -s <message> -e                            : prints a message")
                print("vim <filename>                                   : open a file using vim (only works if you have vim installed)")
                print("crte --type <typename> --name <itemname>         : creates a file or folder with the specified name")
                print("delete <target>                                  : deletes a file or folder")
                print("cad <directory>                                  : change current working directory")
                print("shutdown                                         : close the pythonOS")
                print("start <appname>                                  : starts an app that the pythonOS has")
                print("start -a                                         : show all the apps that exist in pythonOS")
                print("help                                             : show all the commands")
                print("dl                                               : directory list")
                print("python -s <command, example: <filename> > -e     : executes python command")
                print("pyinstall -s <libname> -e                        : downloads an python lib")
                print("version                                          : shows the recent version")
                print("uptime                                           : show system uptime")
                print("diskusage                                        : show disk usage")
                print("createpyfile --name <filename>                   : creates a Python file")
                print("openfile <filename>                              : open a file in the default editor")
                print("rename <oldname> <newname>                       : renames a file or folder")
                print("sc <filename>                                    : shows file content")
                print("aptinstall -s <pkgname> -e                       : downloads pkgs to your computer using sudo apt install (only works with linux debian based)")
                print("coy --filedir <filetocopy> --targetdir <targetofthecopiedfile> : copy an file")
                print("author                                           : shows the pythonOS creator")
                print("realcmd                                          : starts an venv on pythonOS that uses your real pc commands")
                print("evig                                             : shows the terminal system version (linux is bash, pythonOS is named Evig)")
                print("date                                             : Show the current date")
                print("calculator                                       : Opens a simple calculator")
                print("reminder                                         : Set a reminder for an event")
            elif command.startswith("clr"):
                self.clear_screen()
            elif command.startswith("dl"):
                self.list_directory()
            elif command.startswith("cad"):
                directory = command.split(" ")[1].strip("\"\'")
                self.change_directory(directory)
            elif command.startswith("python"):
                commandcontinue = command.split(" -s ")[1].split(" -e")[0].strip("\"\'")
                self.execute_python_command(commandcontinue)
            elif command.startswith("pyinstall"):
                libs = command.split(" -s ")[1].split(" -e")[0].strip("\"\'")
                self.install_python_lib(libs)
            elif command.startswith("version"):
                print("pythonOS by jose icaro. version: 1.5")
            elif command.startswith("uptime"):
                self.show_uptime()
            elif command.startswith("diskusage"):
                self.show_disk_usage()
            elif command.startswith("createpyfile"):
                filename = command.split(" --name ")[1].strip("\"\'")
                self.create_python_file(filename)
            elif command.startswith("openfile"):
                filename = command.split(" ")[1].strip("\"\'")
                self.open_file(filename)
            elif command.startswith("rename"):
                oldname = command.split(" ")[1].strip("\"\'")
                newname = command.split(" ")[2].strip("\"\'")
                self.rename(oldname, newname)
            elif command.startswith("sc"):
                filename = command.split(" ")[1].strip("\"\'")
                self.show_content(filename=filename)
            elif command.startswith("aptinstall"):
                pkgs = command.split(" -s ")[1].split(" -e")[0].strip("\"\'")
                subprocess.run("sudo apt install {pkgs}", shell=True)
            elif command.startswith("coy"):
                file = command.split(" --filedir ")[1].split(" --targetdir ")[1].strip("\"\'")
                targetdir = command.split(" --targetdir ")[1].strip("\"\'")
                self.copy(file, targetdir)
            elif command.startswith("author"):
                print("josé icaro. github: icarogamer2441")
            elif command.startswith("realcmd"):
                veripassword = input("what's your password? ")
                if veripassword != self.password:
                    print("incorrect password! you need to use your real pythonOS password to use your real cmd with an venv inside pythonOS")
                else:
                    self.clear_screen()
                    print("use 'shutvenvdown' to shutdown the venv but not your real pc")
                    while True:
                        commands = input(f"(realpcVenv) {self.username}/pythonOS {cwd} >$ ")
                        if commands.lower() == "shutvenvdown":
                            print("shutting down your venv")
                            time.sleep(2)
                            self.clear_screen()
                            break
                        else:
                            subprocess.run(commands, shell=True)
            elif command.startswith("evig"):
                print("Evig pythonOS terminal system name, made for make pythonOS more realistic OS")
                print("version: 1.0")
                print("release type: oficial release")
            elif command.startswith("date"):
                self.date()
            elif command.startswith("calculator"):
                self.calculator()
            elif command.startswith("reminder"):
                self.reminder()
            else:
                print(f"Err: command not found. {command}")

    def copy(self, filedir, targetdir):
        if platform.system == "Windows":
            subprocess.run(f"copy {filedir} {targetdir}")
        else:
            subprocess.run(f"cp {filedir} {targetdir}")

    def show_content(self, filename):
        if platform.system == "Windows":
            subprocess.run(f"type {filename}", shell=True)
        else:
            subprocess.run(f"cat {filename}", shell=True)

    def show_uptime(self):
        if platform.system() == "Windows":
            output = subprocess.check_output("systeminfo | findstr /C:\"System Boot Time\"", shell=True).decode()
            uptime = output.split(":")[1].strip()
        else:
            uptime = subprocess.check_output("uptime -p", shell=True).decode().strip()
        print(f"System uptime: {uptime}")

    def show_disk_usage(self):
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic logicaldisk get size,freespace,caption", shell=True).decode()
            print(output)
        else:
            output = subprocess.check_output("df -h", shell=True).decode()
            print(output)

    def create_python_file(self, filename):
        if not filename.endswith(".py"):
            filename += ".py"
        subprocess.run(f"touch {filename}", shell=True)

    def open_file(self, filename):
        if platform.system() == "Windows":
            os.startfile(filename)
        elif platform.system() == "Darwin":
            subprocess.run(["open", filename])
        else:
            subprocess.run(["xdg-open", filename])

    def rename(self, oldname, newname):
        try:
            os.rename(oldname, newname)
            print(f"{oldname} renamed to {newname}")
        except FileNotFoundError:
            print("File not found.")
        except PermissionError:
            print("Permission denied.")

System()
