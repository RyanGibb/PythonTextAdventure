#This module contains miscellaneous functions

import __init__
import world_operations
import os


def command(command_input):
    if command_input == "": return
    if command_input[0] == "/": command_input = command_input[1:]
    else: return
    command = command_input.lower().split()

    if command[0] in ("qs", "quick start", "quickstart"): world_operations.quick_start()
    elif command[0] == "quit": pass #run quit (function?), eg promt to save - ect

    elif command[0] == "load":
       save_operations.select_save()
        
    elif command[0] == "save":
        if save_operations.save_name == None:
            print("A save has neither been created nor loaded yet")
            return 0
        
        print("Current saves:")
        saves = save_operations.print_saves()
        print('Type "cancel" to cancel at any time')
        while True:
            if save_operations.save_name == "new":
                new_save_name = input("Save name: ")
                if new_save_name == "cancel": return "cancelled"
                elif new_save_name == "new": print('Save name can\'t be "new"')
                elif new_save_name in saves:
                    while True:
                        overwrite = input("Would you like to overwrite " + new_save_name + "?(y/n) ")
                        if overwrite in ("n", "no"): break
                        elif overwrite in ("y", "yes"):
                            while True:
                                confirmation = input("Are you sure you want to overwrite?(y/n) ")
                                if confirmation in ("n", "no"): break
                                elif confirmation in ("y", "yes"):
                                    save_operations.write_save(new_save_name)
                                    return "saved"
                                elif confirmation == "cancel": return "cancelled"
                        elif overwrite == "cancel": return "cancelled"
                else:
                    while True:
                        confirmation = input("Are you sure you want to save?(y/n) ")
                        if confirmation in ("n", "no"): break
                        elif confirmation in ("y", "yes"):
                            save_operations.write_save(new_save_name)
                            return "saved"
                        elif confirmation == "cancel": return "cancelled"
            else:
                overwrite = input("Would you like to overwrite " + save_operations.save_name + "?(y/n) ")
                if overwrite in ("n", "no"):
                    while True:
                        new_save_name = input("Save name: ")
                        if new_save_name == "cancel": return "cancelled"
                        elif new_save_name == "new": print('Save name can\'t be "new"')
                        elif new_save_name in saves:
                            while True:
                                overwrite = input("Would you like to overwrite " + new_save_name + "?(y/n) ")
                                if overwrite in ("n", "no"): break
                                elif overwrite in ("y", "yes"):
                                    while True:
                                        confirmation = input("Are you sure you want to overwrite?(y/n) ")
                                        if confirmation in ("n", "no"): break
                                        elif confirmation in ("y", "yes"):
                                            save_operations.write_save(new_save_name)
                                            return "saved"
                                        elif confirmation == "cancel": return "cancelled"
                                elif overwrite == "cancel": return "cancelled"
                        else:
                            while True:
                                confirmation = input("Are you sure you want to save?(y/n) ")
                                if confirmation in ("n", "no"): break
                                elif confirmation in ("y", "yes"):
                                    save_operations.write_save(new_save_name)
                                    return "saved"
                                elif confirmation == "cancel": return "cancelled"
                elif overwrite in ("y", "yes"):
                    while True:
                        confirmation = input("Are you sure you want to overwrite?(y/n) ")
                        if confirmation in ("n", "no"): break
                        elif confirmation in ("y", "yes"):
                            save_operations.write_save(save_operations.save_name)
                            return "saved"
                        elif confirmation == "cancel": return "cancelled"
                elif overwrite == "cancel": return "cancelled"



        save_operations.write_save()
    elif command[0] in ("help", "?"):
        if len(command) > 1:
            if command[1] in ("help, ?"): print("Provides help with commands, which in turn provide help with gameplay")
            if command[1] == "exit": print("Exits game without immediately and without saving, used for debugging")
            if command[1] == "info": print("Provides info on various game concepts, use /info on it's own to get a list of possible subcommands")
        else:
            print("Commands: /help (?), /quick start (qs), /info, /exit")
            print('Use "?" or "help" and a command name to get information on it, e.g. "/? exit"')
    elif command[0] == "info":
        if len(command) < 2: print("Subcommands: race, class")
        elif command[1] == "race":
            print("""Races:
Dwarf (dwarf/d/1):
    -race str = 7
    -race int = 3
    -race mag = 4
Orc (orc/o/2):
    -race str = 7
    -race int = 3
    -race mag = 4""")
        elif command[1] == "class":
            print("""Classes:
Warrior (warrior/w/1):
    -class str = 3
    -class int = 0
    -class mag = 0
Thief (thief/t/2):
    -class str = 0
    -class int = 3
    -class mag = 0""")
        else:
            print("Subcommand not recognised")
    else:
        try: eval(command_input) #############################################################
        except NameError: print("command", '"' + command_input + '"', "not recognised")
        #instead of lenght check to try and exept keyerror?
    #return True or False so messages like invalid race don't get sent



def validate_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def validate_file(file):
    split_file_path = file.split(os.sep)
    directory = (os.sep).join(split_file_path[0:len(split_file_path)-1])
    validate_directory(directory)
    if not os.path.isfile(file):
        file_creation = open(file, 'a')
        file_creation.close()
    return file

def location_key(z, y, x): return str(x) + "," + str(y) + "," + str(z)





import save_operations



