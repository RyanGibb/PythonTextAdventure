#This module preforms operations on the world space and the global list "world" (declared in __init__.py)

import __init__
import os
import functions
import rooms
import entity_operations
import save_operations

def quick_start():
    world_name = "default"
    print("WORLD:", world_name, "selected")
    start_coords = load_map("default")    

    while start_coords == None:
        print("ERROR: no start room in world, please edit accordingly or select a new world")
        print()
        start_coords = world_operations.load_map(select_world())

    for f in range(0, len(__init__.entity)):
        __init__.entity[f].location_set()

    __init__.player.call_race("orc")
    print("Orc selected")
    __init__.player.call_clas("warrior")
    print("Warrior selected")
    __init__.player.calculate_stats()

    print("\nYou are", __init__.player.race_determiner, __init__.player.race_adjective, __init__.player.clas)
    __init__.player.location_input(start_coords)
    __init__.game_loop = True
    save_operations.save_name = "new"

def initiate():#add player number/name here if turned into MUD (multi-user dungeon)
    start_coords = load_map(select_world())

    while start_coords == None:
        print('ERROR: no "Start" room in world, please edit accordingly or select a new world')
        print()
        start_coords = world_operations.load_map(select_world())

    for f in range(0, len(__init__.entity)):
        __init__.entity[f].location_set()

    entity_operations.input_race(__init__.player)
    entity_operations.input_clas(__init__.player)
    __init__.player.calculate_stats()

    print("\nYou are", __init__.player.race_determiner, __init__.player.race_adjective, __init__.player.clas)
    __init__.player.location_input(start_coords)
    __init__.game_loop = True



def load_map(world_name):#,world
    directory = functions.validate_directory(os.path.join(os.path.dirname(__file__), "worlds", world_name))
    
    #how to import rooms.py (now world_info) from a relative file path - inputting rooms.py from the world, that is to say in the directory world_name
    #for now, rooms.py in main directory

    global z_range
    z_range = (open(functions.validate_file(os.path.join(directory, "z.txt"))).readline()).split()
    z_range = [int(z_range[0]), int(z_range[1])]
    
    start_coords = None

    #world = [[[0 for k in range(0, )] for j in xrange(n)] for i in xrange(n)]
    __init__.world = [None for z in range(z_range[0], z_range[1] + 1)]

    global y_range
    global x_range
    y_range = 0
    x_range = 0

    #room_number_with_enemies = 0
    #entities = {}   ###

    for z in range(z_range[0], z_range[1]):
        file = open(functions.validate_file(os.path.join(directory, str(z) + ".csv")))
        __init__.world[z] = file.readlines()
        if len(__init__.world[z]) > y_range: y_range = len(__init__.world[z])###
        ###if y_range == 0: __init__.world[z] = [[]]
        for y in range(len(__init__.world[z])):
            __init__.world[z][y] = __init__.world[z][y][0:-2].split(",")    #[0:-2] for getting rid of /n at each line
            if len(__init__.world[z][y]) > x_range: x_range = len(__init__.world[z][y])###
            for x in range(len(__init__.world[z][y])):
                if __init__.world[z][y][x] == "#": __init__.world[z][y][x] = None #"-", or any other placeholder put it cell when there is no room there        #http://excel.tips.net/T003068_Inconsistent_Output_for_Empty_Columns_in_a_CSV_File.html
                else: 
                    room_split = __init__.world[z][y][x].replace('"', "").replace(")", "").split("(")
                    room_name = room_split[0]
                    try:
                        getattr(rooms, room_name)
                        legitamate_room = True
                    except AttributeError:
                        legitamate_room = False
                        __init__.world[z][y][x] = None
                        #print('Room "' + room_name + '" not found, coordinate set to "None"')
                    if legitamate_room == True:
                        try:
                            room_arguments_split = room_split[1].split("/")
                            #print(room_arguments_split)
                            has_arguments = True
                        except IndexError: has_arguments = False
                        
                        if has_arguments == True and len(room_arguments_split[0]) > 0:  #what if room_arguments_split not defined?
                            #entities[room_number_with_enemies] = room_arguments_split[0].split()
                            #room_number_with_enemies += 1
                            entity = room_arguments_split[0].split()
                            for f in range(len(entity)):
                                entity[f] = entity[f].split("-")
                                if len(entity[f]) > 0: entity_operations.create_entity(entity[f][0], entity[f][1], z, y, x) #for "people" enemies
                                #else: create_entity(entity[f][0], None, z, y, x) ###for "monster enemies
                            

                        if len(room_arguments_split) > 1: items = room_arguments_split[1].split()
                        else: items = None

                        #try:
                        __init__.world[z][y][x] = getattr(rooms, room_name)(z, y, x, items)

                        #print("ROOM:", __init__.world[z][y][x].__class__.__name__, "instance created at X:" + str(x) +  " Y:" + str(y) + " Z:" + str(z))
                        #print("ROOM (coords from instance its self):", __init__.world[z][y][x].__class__.__name__, "instance created at X:" + str(__init__.world[z][y][x].x) +  " Y:" + str(__init__.world[z][y][x].y) + " Z:" + str(__init__.world[z][y][x].z))

                        #except AttributeError:
                        #    __init__.world[z][y][x] = None
                        #    print('Room "' + room_name + '" not found, coordinate set to "None"')
                        if room_name == "Start":
                            start_coords = (z, y, x)
    #for f in range(room_number_with_enemies):
    #    for g in range(len(entities[f])):
    #        entities[f][g] = entities[f][g].split("-")
    #        if len(entities[f][g]) > 0: create_entity(entities[f][g][0], entities[f][g][1], (z, y, x)) #for "people" enemies
    #        #else: create_entity(entities[f][g][0], None, (z, y, x)) ###for "monster enemies

    print("WORLD:", world_name, "loaded")

    return start_coords

def select_world():
    print("Choose your world to create this save in:")
    worlds_file = os.path.join(os.path.dirname(__file__), "worlds", "worlds.txt")
    worlds = open(worlds_file, "r").read().split(", ")
    for counter in range(0, len(worlds)):
        if len(worlds) > 0:
            print("\t" + worlds[counter])
        else:
            print("\tNO EXISTING WORLDS")
    while True:
        world_name = input(">World: ")
        functions.command(world_name)
        if world_name in worlds:
            print("WORLD:", world_name, "selected")
            return world_name
        else:
            print("Invalid world")

