# please, install the pytkinterui (my own GUI library made with tkinter for my projects). install using "pip install pytkinterui"
import subprocess
import platform
import os
import time
import random
from pytkinterui import Window

class Bootloader:
    def __init__(self):
        self.clear_screen()
        print("welcome to pythonloader, an custom pythonOS bootloader! customize if you're creating your own pythonOS version")
        print("=======================")
        print("=                     =")
        print("=  #######   #     #  =")
        print("=  #      #   #   #   =")
        print("=  #######      #     =")
        print("=  #            #     =")
        print("=  #            #     =")
        print("=                     =")
        print("=======================")
        self.runos = input("do you want to run this pythonOS version? (y/n) > ")
        if self.runos.lower() == "yes" or self.runos.lower() == "y":
            System()
    
    def clear_screen(self):
        if platform.system() == "Windows":
            subprocess.run("cls", shell=True)
        else:
            subprocess.run("clear", shell=True)

class System:
    def __init__(self):
        self.clear_screen()
        self.username = input("What's your name? > ")
        self.password = input("your new password? > ")
        self.computername = input("what name will be your computer? (type 'nothing' to be default) > ")
        self.foodcount = 0
        if self.computername.lower() == "nothing":
            self.computername = "pythonOS"
        else:
            pass
        self.base_directory = os.getcwd()
        self.customcmds = {} # dictionary to store custom commands
        print(f"You're using your host system to work with the file system!\nCurrent working directory: {self.base_directory}")
        self.RunOS()
        if self.relogin == True:
            System()
        else:
            pass
    
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

    def RunOS(self):
        print("+------------------------------+")
        print("|                              |")
        print("|  pythonOS 3.5 by jose icaro  |")
        print("|        made with love        |")
        print("|    98% me and 2% chatgpt     |")
        print("|                              |")
        print("+------------------------------+")
        while True:
            if self.computername == "" or self.computername.lower() == "nothing":
                self.computername = "pythonOS"
            self.relogin = False
            cwd = os.getcwd()
            command = input(f"\n{self.username}@{self.computername} {cwd} >$ ")
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
                    if platform.system() == "Windows":
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
                        yourmessage = input(f"{self.username} > ")
                        print(yourmessage)
                        fakemessage = input(f"{fakeperson} > ")
                        print(fakemessage)
                        if yourmessage == "exit" or fakemessage == "exit":
                            break
                elif app.lower() == "-a":
                    print("Existing apps:")
                    print("1 - fakechat")
                    print("2 - guesstnumber")
                    print("3 - createpyosver")
                    print("4 - todolist")
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
                elif app.lower() == "createpyosver":
                    vername = input("Enter an custom name to your pythonOS version > ")
                    with open(f"{vername}.py", "w") as file1:
                        with open("system.py", "r") as file2:
                            sourcecode = file2.read()
                        file1.write(sourcecode)
                    print("pythonOS custom version file created!")
                    editfile = input("do you want to edit the created file? (you need vim installed) (y/n) > ")
                    if editfile.lower() == "yes" or editfile.lower() == "y":
                        os.system('vim ' + f"{vername}.py")
                    else:
                        print("you now have the custom system file but you dont gonna edit. (you can edit with other file editor)")
                elif app.lower() == "todolist":
                    print("use 'end' to end your todolist, and use 'show' to show all your items")
                    items = []
                    while True:
                        additem = input("> ")
                        if additem.lower() == "end":
                            print("ended...")
                            break
                        elif additem.lower() == "show":
                            for item in items:
                                print(item)
                        else:
                            items.append(additem)
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
                print("aptinstall -s <pkgname> -e                       : downloads pkgs to your computer using sudo apt install (only works with linux that uses 'sudo apt install pkg1-name pkg2-name ...')")
                print("coy --filedir <filetocopy> --targetdir <targetofthecopiedfile> : copy an file")
                print("author                                           : shows the pythonOS creator")
                print("realcmd                                          : starts an venv on pythonOS that uses your real pc commands")
                print("evig                                             : shows the Evig version (linux is bash, pythonOS is named Evig)")
                print("date                                             : Show the current date")
                print("calculator                                       : Opens a simple calculator")
                print("reminder                                         : Set a reminder for an event")
                print("osname                                           : shows the os name")
                print("becreator                                        : shows an simple guide of be an pythonOS creator")
                print("howtoversion                                     : shows an complete description of how to make your own pythonOS version (be an pythonOS creator)")
                print("cretecmd                                         : creates an custom command that you have to use an real cmd of your terminal")
                print("execmd <customcmdname>                           : executes your custom cmd")
                print("newterminal                                      : new terminal, but you dont need to login")
                print("editcmd                                          : edits your custom command")
                print("newloginterminal                                 : new terminal, but with login")
                print("delallcmds                                       : delete all your custom commands")
                print("addedthings                                      : see what features are added in this update")
                print("developermode                                    : enters developer mode")
                print("imhungry                                         : you're really hungry?")
                print("removedthings                                    : shows all removed things (apps and commands)")
                print("renamcomputer                                    : renames your pythonOS computer name")
                print("changeusername                                   : changes your username")
                print("changepassword                                   : changes your password")
                print("showpass                                         : shows your pythonOS password")
                print("foods <foodtype>                                 : foods!")
                print("foods -a                                         : shows an help from the foods types")
                print("desktop                                          : activate desktop mode (dont have terminal commands, and need 5 foods or more)")
                print("youtube                                          : shows my youtube channel link")
                print("pytest                                           : test :D")
                print("allos                                            : show all my OS's projects")
                print("abouticaroos                                     : about my second OS (made in libreoffice impress)")
                print("aboutpythonos                                    : about this OS (made in python)")
                print("google                                           : open google.com")
                print("node -s <command. ex: file.js> -e                : executes a nodejs command")
                print("nodeinstall -s <pkgs-name> -e                    : executes a npm install <pkg-name>")
                print("kmpt                                             : don't use this command!")
                print("micro <filename>                                 : starts the micro text editor (you need to have it installed)")
                print("pyoscreatemode                                   : a Creator mode to you create and test your own pythonOS version")
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
                print("pythonOS by jose icaro. version: 3.5")
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
                file = command.split(" --filedir ")[1].split(" --targetdir ")[0].strip("\"\'")
                targetdir = command.split(" --targetdir ")[1].strip("\"\'")
                self.copy(file, targetdir)
            elif command.startswith("author"):
                print("josé icaro. github: https://github.com/icarogamer2441/")
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
                print("Evig pythonOS is like Bash from linux. Evig was made to make pythonOS a more realistic OS")
                print("version: 3.0")
                print("release type: oficial release")
            elif command.startswith("date"):
                self.date()
            elif command.startswith("calculator"):
                self.calculator()
            elif command.startswith("reminder"):
                self.reminder()
            elif command.startswith("osname"):
                print("Operating System name: pythonOS")
            elif command.startswith("becreator"):
                print("if you want to be an pythonOS creator you can make your own version using the pythonOS code! please, use 'py' or 'os' on your pythonOS version name")
            elif command.startswith("howtoversion"):
                veripassword = input("what's your password? > ")
                if veripassword != self.password:
                    print("incorrect password! use your pythonOS password!")
                else:
                    print("do you really want to create your version? okay, here the tutorial:")
                    print("learn python")
                    print("see the pythonOS code and put all the commands inside of the 'System' class")
                    print("inside system class, put an 'elif command.startswith('cmdname'):' in the RunOS function, after this, put your command function inside of the new 'elif'")
                    print("save the file")
                    print("if you want, add GUI to your pythonOS version (tkinter is super recommended to add gui)")
                    print("add apps inside of the 'start' command if you want")
                    print("costumize more and more your pythonOS version!")
                    print("put the credits that you made the version, and the real pythonOS creator. me (josÃ© icaro)")
                    print("publish in github")
                    print("enjoy your custom version!")
            elif command.startswith("cretecmd"):
                veripassword = input("you need your password to modify your OS! password: > ")
                if veripassword != self.password:
                    print("Err: incorrect password")
                else:
                    print("Warn! if you create an custom command, you need to use an real os command! (based on your OS)")
                    print("Warn! your custom command will not be saved forever! it will only work on this session.")
                    cmdname = input("command name (example: hello) > ")
                    executecmd = input('what command will execute? (example: echo "hello world!") > ')
                    self.customcmds[cmdname] = executecmd
            elif command.startswith("execmd"):
                customcmd = command.split(" ")[1].strip("\"\'")
                if customcmd in self.customcmds:
                    os.system(self.customcmds[customcmd])
                else:
                    print("Err: unknown custom command")
            elif command.startswith("editcmd"):
                veripassword = input("what's your password? > ")
                if veripassword != self.password:
                    print("Err: incorrect password")
                else:
                    newcmdname = input("what's your custom command? custom cmd name > ")
                    newexecutecmd = input("and what should be the execution? > ")
                    self.customcmds[newcmdname] = newexecutecmd
            elif command.startswith("newterminal"):
                self.clear_screen()
                print("+------------------------------+")
                print("|                              |")
                print("|  pythonOS 3.5 by jose icaro  |")
                print("|        made with love        |")
                print("|    98% me and 2% chatgpt     |")
                print("|                              |")
                print("+------------------------------+")
            elif command.startswith("newloginterminal"):
                self.relogin = True
                break
            elif command.startswith("delallcmds"):
                self.customcmds = {}
            elif command.startswith("addedthings"):
                print("apps:")
                print("commands:")
                print("1 - systemicon")
            elif command.startswith("developermode"):
                print("you will only do programming inside developer mode")
                enter = input("do you really want to start developer mode? (y/n) > ")
                if enter.lower() == "y" or enter.lower() == "yes":
                    while True:
                        devcommand = input("help to see commands > ")
                        if devcommand.lower() == "help":
                            print("commands:")
                            print("1 - exit                         : ends the developer mode")
                            print("2 - create-react-app <appname>   : creates react app (needs npm, npx and nodejs)")
                            print("3 - clear                        : clears the screen")
                            print("4 - run-react-app                : runs your react app")
                            print("5 - python <filename>            : executes a python file")
                            print("6 - node <filename>              : executes a node js file")
                            print("Warn! this developer mode is only for python, reactjs and nodejs")
                        elif devcommand == "exit":
                            print("ended developer mode")
                            break
                        elif devcommand == "clear":
                            self.clear_screen()
                        elif devcommand.startswith("create-react-app"):
                            appname = devcommand.split(" ")[1].strip("\"\'")
                            subprocess.run(f"npx create-react-app {appname}", shell=True)
                        elif devcommand == "run_react_app":
                            subprocess.run("npm run", shell=True)
                        elif devcommand.startswith("python"):
                            filename = devcommand.split(" ")[1].strip("\"\'")
                            with open(filename,"r") as f:
                                code = f.read()
                            exec(code)
                        elif devcommand.startswith("node"):
                            filename = devcommand.split(" ")[1].strip("\"\'")
                            subprocess.run(f"node {filename}", shell=True)
                        else:
                            print(f"Err: uknown command. {devcommand}")
            elif command.startswith("imhungry"):
                print("you're really hungry?")
                yesno = input("chose (y/n) > ")
                if yesno.lower() == "y" or yesno.lower() == "yes":
                    print("here some food! now bye")
                elif yesno.lower() == "n" or yesno.lower() == "no":
                    print("okay. bye")
                else:
                    print("okay? i dont understand what're you saying")
            elif command.startswith("removedthings"):
                print("removed things:")
            elif command.startswith("renamcomputer"):
                self.computername = input("what's your new pythonOS computer name? > ")
            elif command.startswith("changeusername"):
                self.username = input("your new username > ")
            elif command.startswith("changepassword"):
                oldpassword = input("what's your old password? > ")
                if oldpassword == self.password:
                    self.password = input("what's your new password? > ")
                else:
                    print("incorrect password! use the command 'showpass' to show your password")
            elif command.startswith("showpass"):
                print(f"your current password is: {self.password}")
            elif command.startswith("foods"):
                foodtype = command.split(" ")[1].strip("\"\'")
                if foodtype == "-a":
                    print("foods types:")
                    print("1 - show")
                    print("2 - take")
                elif foodtype == "show":
                    print(f"you have {self.foodcount} foods")
                elif foodtype == "take":
                    self.foodcount += random.randint(1,5)
            elif command.startswith("desktop"):
                if self.foodcount > 4:
                    self.foodcount -= 5
                    desktop = Window(750,570,"pythonOS desktop v1.1")
                    desktop.window.configure(bg="yellow")

                    def pythontext():
                        root = Window(300,300,"pythonText-v1.1")
                        
                        def save():
                            filename = root.new_input("filename","your file name: ")
                            with open(filename, "w") as f:
                                f.write(textbox.get("1.0", "end-1c"))

                        textbox = root.new_text(0,0,300,290,"black","white")
                        mainmenu = root.new_menu()

                        filemenu = root.new_submenu(mainmenu, "File")
                        root.new_submenu_button(filemenu,"Save",command=lambda: save())

                        root.window.mainloop()
                    
                    def pythonwelcome():
                        root = Window(300,300,"WELCOME!!!")
                        root.window.resizable(False,False)

                        messagelabel = root.new_label("welcome to pythonOS!",0,0,300,300,"white","black")

                        root.window.mainloop()

                    taskbar = desktop.new_menu()

                    startmenu = desktop.new_submenu(taskbar, "Start")
                    desktop.new_submenu_button(startmenu,"shutdown",command=lambda: desktop.window.destroy())
                    desktop.new_menu_separator(startmenu)
                    desktop.new_submenu_button(startmenu,"Python Text",command=lambda: pythontext())
                    desktop.new_submenu_button(startmenu,"Python Welcome",command=lambda: pythonwelcome())

                    desktop.window.mainloop()
                else:
                    print("you need 5 foods or more to run desktop!")
            elif command.startswith("youtube"):
                print("my youtube channel: https://www.youtube.com/channel/UC1rE1iC0w3sWgNCR4FKiqmg")
            elif command.startswith("pytest"):
                print("you corromped your system!")
                break
            elif command.startswith("allos"):
                print("All OS's:")
                print("icaroOS > icarogamer2441.github.io")
                print("pythonOS > this OS")
            elif command.startswith("abouticaroos"):
                print("About my other OS:")
                print("icaroOS is an operating system made with libreoffice impress (for this reason icaroOS is very limited) if you want to use it, download and install libreoffice and download icaroOS HOME EDITION through this link: 'icarogamer2441.github.io/' and the PRO EDITION through this link: icarogamer2441.github.io/pro/' because PRO EDITION is a PRO edition, it is more complete and less full of bugs, but there are some bugs in it, especially in the HOME EDITION")
            elif command.startswith("aboutpythonos"):
                print("About pythonOS:")
                print("pythonOS is a simple operating system made in python, it was made for other people to create their own customized operating systems, create what you want and add what you think, be happy customizing this system and if you want, you can post your pythonOS version and any place")
            elif command.startswith("google"):
                if platform.system() == "Windows":
                    subprocess.run("start https://www.google.com", shell=True)
                else:
                    subprocess.run("xdg-open https://www.google.com", shell=True)
            elif command.startswith("node"):
                nodecommand = command.split(" -s ")[1].split(" -e")[0].strip("\"\'")
                subprocess.run(f"node {nodecommand}", shell=True)
            elif command.startswith("nodeinstall"):
                nodeinstcmd = command.split(" -s ")[1].split(" -e")[0].strip("\"\'")
                subprocess.run(f"npm install {nodeinstcmd}", shell=True)
            elif command.startswith("kmpt"):
                print("K = kill. M = my. P = pythonOS. T = terminal")
                break
            elif command.startswith("micro"):
                filename = command.split(" ")[1].strip("\"\'")
                subprocess.run(f"micro {filename}", shell=True)
            elif command.startswith("secret"):
                print("DONT USE THIS COMMAND!")
                randomsss = input("DO YOU WANT TO DHUWIDWUIDHWIUDWTUDGW98SWIYDG? > ")
                if randomsss.lower() == "y":
                    print("O_O")
                else:
                    print("o_O")
            elif command.startswith("pyoscreatemode"):
                print("you need vim installed!")
                ihavevim = input("do you have a code editor installed (you need vim to use the edit file command)? (Y/n) > ")
                if ihavevim.lower() == "y" or ihavevim.lower() == "yes":
                    while True:
                        editmodecmd = input("type 'h' for help > ")
                        if editmodecmd == "h":
                            print("## Creator commands:")
                            print("c - create the pythonos version file")
                            print("e - edits the pythonos version file")
                            print("p - executes your pythonOS version")
                            print("## exit")
                            print("q - quit")
                            print("## clear")
                            print("o - clear the screen")
                            print("## steps")
                            print("first, create the pythonOS version file, and edit them, add your commands, remove the commands you want, edit the pythonOS version name, edit the commands (if you want), create a custom version of evig and the version of your pythonOS version, and the final step! publish your pythonOS version (if you want)")
                        elif editmodecmd == "c":
                            versioname = input("what's your pythonOS version name? (dont use spaces) > ")
                            with open("system.py", "r") as f:
                                with open(versioname + ".py", "w") as files:
                                    files.write(f.read())
                        elif editmodecmd == "e":
                            filename = input("what's your pythonOS version name? > ")
                            subprocess.run(f"vim {filename + '.py'}", shell=True)
                        elif editmodecmd == "q":
                            break
                        elif editmodecmd == "p":
                            filename = input("what's your pythonOS version name? > ")
                            if platform.system == "Windows":
                                subprocess.run(f"python {filename + '.py'}", shell=True)
                            else:
                                subprocess.run(f"python3 {filename + '.py'}", shell=True)
                        elif editmodecmd == "o":
                            self.clear_screen()
                else:
                    print("you only can create your own pythonOS version with vim!")
            elif command.startswith("systemicon"):
                print("""MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWXKK000NMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWkMMMMMMMMOMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMX; .....  lWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMW0xo  ...... 'xkkkOXMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWd  .........      KMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWc  ........  kXX  kMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWo  ......,  xKXX  x0OOOOKWMMMMMMMMMMMMMMMM
MMMMMMMMKl   .   Xx'kxxx  ..:::::;.lNMMMMMMMMMMMMM
MMMMMMMMMWNk   Xxccc     .kNWMMM0',0MMMMMMMMMMMMMM
MMMMMMMMMMMK  ''''''  lWX; .OMMMMM0''0MMMMMMMMMMMM
MMMMMMMMMMMWXkxdddddxKWK, .xMMMMM0';XMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMO. .o000OOo.:XNWWWWWWMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMXl',::::::. .;;::::;;oXMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWNWWWWWMMo.l000000Ol:0MMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo.oWWMMMMMWWMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO,,:::::ccldXMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXK00Okkxxc.lWMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0';XMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOONMMMMMMMO.:NMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc':::c:c::,.oWMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNK000OOOOOO0NMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM""")
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
            if platform.system() == "Windows":
                subprocess.run(f'echo "" >> {filename + ".py"}', shell=True)
            else:
                subprocess.run(f'touch {filename + ".py"}', shell=True)

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

Bootloader()
