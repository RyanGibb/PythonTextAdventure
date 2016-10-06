#This module preforms operations on save file, such as reading from and writing to them.

import os
import world_operations
import functions
import pickle
import __init__

save_folder = functions.validate_directory(os.path.join(os.path.dirname(__file__), "saves"))
#save_file = functions.validate_file(os.path.join(save_folder, ".saves.txt"))
save_name = None

def print_saves():
    #saves = [f for f in os.listdir(save_folder) if os.path.isfile(os.path.join(save_folder,f))] #from http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
    saves = next(os.walk(save_folder))[1] #from http://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
    if len(saves) == 0: print("\tNO EXISTING SAVES")
    else:
        for counter in range(0, len(saves)):
            #saves[counter] = saves[counter][:len(saves[counter])-4]
            #if saves[counter] == ".saves":
            #    continue
            if len(saves) != 0: 
                print("\t" + saves[counter])
            #else:
            #    print("\tNO EXISTING SAVES")
    return saves
    
def select_save():
    print("Choose your save:")
    saves = print_saves()
    print('Type "new" to start a new save')
    print('Type "cancel" to cancel save selection')
    global save_name
    while True:
        save = input(">Save: ")
        functions.command(save)
        if save == "new":
            #print("New save selected")
            save_name = "new"
            world_operations.initiate()
            break
        if save in saves:
            #print(save, "selected")
            save_name = save
            read_save(save)
            break
        if save == "cancel": break
        else: print("Invalid save")

def read_save(save):
    folder = os.path.join(save_folder, save)
     
    __init__.player = pickle.load(open(os.path.join(folder, "player"), "rb"))
    __init__.entity = pickle.load(open(os.path.join(folder, "entitiy"), "rb"))
    __init__.world = pickle.load(open(functions.validate_file(os.path.join(folder, "world")), "rb"))
    
    global save_name
    save_name = save
    __init__.game_loop = True
    print(save, "loaded")
    print("\nYou are", __init__.player.race_determiner, __init__.player.race_adjective, __init__.player.clas)


    
def write_save(save, mode=0): #mode 0 = normal storage, mode 1 = human readable storage
    #if save not in saves:
        #overwrite operation

    folder = functions.validate_directory(os.path.join(save_folder, save))
    
    pickle.dump(__init__.player, open(functions.validate_file(os.path.join(folder, "player")), "wb"))
    pickle.dump(__init__.entity, open(os.path.join(folder, "entitiy"), "wb"))
    pickle.dump(__init__.world, open(functions.validate_file(os.path.join(folder, "world")), "wb"))

    print(save + " saved")









