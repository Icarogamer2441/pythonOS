import subprocess
import platform
import os
import time

class System:
    def __init__(self):
        self.clear_screen()
        self.username = input("What's your name? > ")
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

    def RunOS(self, username):
        print("+------------------------------+")
        print("|                              |")
        print("|  pythonOS 1.2 by jose icaro  |")
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
                    subprocess.run(f"touch {itemname}", shell=True) or subprocess.run(f'echo "" >> {itemname}', shell=True)
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
                print("pythonOS by jose icaro. version: 1.2")
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
            else:
                print(f"Err: command not found. {command}")

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
