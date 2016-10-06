#This module (a module is a ".py" file) is run when the package ("../textgame") is executed, it runs the game using functions, classes and other resources from the other modules
import __init__
import os
import cohorts
import rooms
import save_operations
import world_operations
import entity_operations

import functions

#print('Use "/help" or "/?" for help')
#print("Welcome to A Python Text Adventure")

def local():
    print("===============================\nYou are playing a local singleplayer game")
    print('Type "/load" to select a save game')
    __init__.player = entity_operations.char(0, "player")
    while True:
        action = input(">")
        functions.command(action)
        while __init__.game_loop:
            print("===" + __init__.player.location.description())
            action = input("-->")
            functions.command(action)
            action = action.lower()

            __init__.player.direction(action)

            if action == "i": print("INVENTORY")
            elif action == "character":
                print("Strength:", __init__.player.str)
                print("Intelligence:", __init__.player.int)
                print("Agility:", __init__.player.agl)
                print("Speed:", __init__.player.speed)
            
            if action == "/break": __init__.game_loop = False

            for f in range(0, len(__init__.entity)):
                if __init__.entity[f].location == __init__.player.location:
                    __init__.player.health -= 10
                    print("You have been damaged for 10 points")

            print("--------------------------------")
            print("Health: \t" + str(__init__.player.health) + "/" + str(__init__.player.max_health))
            print("Magicka: \t" + str(__init__.player.magicka) + "/" + str(__init__.player.max_magicka))
            ###stamina

            if __init__.player.health <= 0:
                print("================================")
                print("You are dead")
                __init__.game_loop = False




def client():
    print("This feature has not been implimented yet")

def server():
    print("This feature has not been implimented yet")


while True:
    print('Type "local" to play singleplayer, "client" to play multiplayer, or "server" to host a multiplayer game')
    #mode = input("")
    local()
    if mode == "local": local()
    elif mode == "client": client()
    elif mode == "server": server()
    else: print("Invalid option, please retry")




