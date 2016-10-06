#This module preforms operations on entities

import __init__
import cohorts
import world_operations
import functions
from random import randint

class char:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
    def __str__(self): return "char instance: " + str(self.ID) + " (name; " + self.name + ")"
     
    def call_race(self, race):
        self.race = race #right place for this?, or just replace self.race with race - in this method (becuase race_int and others can already be accessed with self.race_int, or self.something_else)
        if self.race == "r" or self.race == "random" or self.race == "0":   #use        if self.race in (ect ect ect)
            self.race = str(randint(1,2))
            print("Random selected")
            self.call_race(self.race)
        else:
            try: getattr(cohorts.Race, self.race)(self)
            except AttributeError: self.race = "invalid"
        ##add back in using indexed (0, 1, 2 ect) and first letters for a race input with this new cohorts module (also so random works)
    def call_clas(self, clas):
        self.clas = clas
        if self.clas == "r" or self.clas == "random" or self.clas == "0":
            self.clas = str(randint(1,2))
            print("Random selected")
            self.call_clas(self.clas)
        else:
            try: getattr(cohorts.Clas, self.clas)(self)
            except AttributeError: self.clas = "invalid"

    def calculate_stats(self):
        self.str = self.race_str + self.clas_str
        self.int = self.race_int + self.clas_int
        self.agl = self.race_agl + self.clas_agl
        
        self.baseline_health = self.str * 10
        self.baseline_magicka = self.int * 10
        self.baseline_speed = self.agl * 10

        self.max_health = self.baseline_health
        self.max_magicka = self.baseline_magicka
        self.max_speed = self.baseline_speed

        self.health = self.baseline_health
        self.magicka = self.baseline_magicka
        self.speed = self.baseline_speed

    def location_set(self):
        try:
            #try: print(self.name + "(" + str(self.ID) + ")" + " at X:" + str(self.x) +  " Y:" + str(self.y) + " Z:" + str(self.z))
            #except AttributeError: print(self.name + "(" + str(self.ID) + ")" + " not in world space. " + self.name[0].upper() + self.name[1:] + " in limbo???")
            #print(self.name + "(" + str(self.ID) + ")" + "at trying to go to X:" + str(self.new_x) +  " Y:" + str(self.new_y) + " Z:" + str(self.new_z))#
            if self.new_x <= world_operations.x_range and self.new_x >= 0 and self.new_y <= world_operations.y_range and self.new_y >= 0 and self.new_z <= int(world_operations.z_range[1]) and self.new_z >= int(world_operations.z_range[0]):
                if __init__.world[self.new_z][self.new_y][self.new_x] != None:
                    self.location = __init__.world[self.new_z][self.new_y][self.new_x]
                    self.x = self.new_x
                    self.y = self.new_y
                    self.z = self.new_z
                else: raise AttributeError
            else: raise IndexError
        except IndexError:
            print("IndexError --- Coordinate Error")#
            #print("There is no path that way (replace w/ room text for wall in the way")
            print("There is a wall in the way")
        except AttributeError:
            print('NameError --- "NoneType" cell')
            #print("There is no path that way (replace w/ room text for wall in the way")
            print("There is a wall in the way")
        #print(self.name + "(" + str(self.ID) + ")" + " at X:" + str(self.x) +  " Y:" + str(self.y) + " Z:" + str(self.z))
        #print(self.location)
    def location_input(self, coords):
        self.new_x = coords[2]
        self.new_y = coords[1]
        self.new_z = coords[0]
        self.location_set()
    def direction(self, direction):
        self.new_x = self.x
        self.new_y = self.y
        self.new_z = self.z
        if direction[0:3] == "go ":
            direction = direction[3:]
        if direction in ("north", "w"):
            self.new_y = self.y - 1
        elif direction in ("south", "s"):
            self.new_y = self.y + 1
        elif direction in ("east", "d"):
            self.new_x = self.x + 1
        elif direction in ("west", "a"):
            self.new_x = self.x - 1
        self.location_set()
        #add up and down, and north_east, south_west_down, ect
    #make location input in __init__ ?
    #race and clas too ?

def input_race(entity):
    sure = False
    while not sure:
        checked = False
        race = input(">>Race: ")
        functions.command(race)
        race = race.lower()
        if race in ("white", "black", "asian", "nigga", "nigger"):
            print("D&D style races please, and don't be racist")
            race = "invalid"
        #functions.command(entity.race)
        
        
        entity.call_race(race)

        if entity.race == "invalid":
            print("Invalid race, please re-enter")
            check = False
        else:
            print(entity.race[0].upper() + entity.race[1:] + " selected")
            check = True
        
        while check:
            sure = input(">>>Are you sure you want to select " + str(entity.race_determiner) + " " + str(entity.race) + ": ")
            functions.command(sure)
            sure = sure.lower()
            if sure in ("y", "yes", "yeah", "yep", "yar", "affirmative", "positive", "ya", "ya mun", "ya man", "aye", "sure"):
                sure = True
                break
            elif sure in ("n", "no", "naw", "na", "nay", "negative","na mun", "na man", "naw mun", "naw man", "not sure"):
                sure = False
                break
            else:
                print("Please enter yes or no (yes/no, y/n): ")

def input_clas(entity):
    sure = False
    while not sure:
        checked = False
        clas = input(">>Class: ")
        functions.command(clas)
        clas = clas.lower()
        
        entity.call_clas(clas)

        if entity.clas == "invalid":
            print("Invalid class, please re-enter")
            check = False
        else:
            print(entity.clas[0].upper() + entity.clas[1:] + " selected")
            check = True
        
        while check:
            sure = input(">>>Are you sure you want to select " + str(entity.clas_determiner) + " " + str(entity.clas) + ": ")
            functions.command(sure)
            sure = sure.lower()
            if sure in ("y", "yes", "yeah", "yep", "yar", "affirmative", "positive", "ya", "ya mun", "ya man", "aye", "sure"):
                sure = True
                break
            elif sure in ("n", "no", "naw", "na", "nay", "negative","na mun", "na man", "naw mun", "naw man", "not sure"):
                sure = False
                break
            else:
                print("Please enter yes or no (yes/no, y/n): ")

def create_entity(race, clas, z, y, x): ###needs work
    #entity = __init__.entity[len(__init__.entity) - 1]
    #entity = char(str(len(__init__.entity)), race + "-" + clas)
    __init__.entity.append(char(str(len(__init__.entity)), race + "-" + clas))  ###io thing a big redundant
    entity = __init__.entity[-1]
    entity.call_race(race)
    entity.call_clas(clas)
    entity.calculate_stats()

    entity.new_z = z
    entity.new_y = y
    entity.new_x = x
    
    #entity.location_input(coords)
    
    #entity.new_z = z
    #entity.new_y = y
    #entity.new_x = x
    #entity.location_set()
    return str(len(__init__.entity))
    ###make if only race given 'monster' created

