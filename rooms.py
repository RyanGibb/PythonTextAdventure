#This module contains information on rooms that can the accessed. The superclass "Room" provides a template for other rooms to use

class Room():
    def __init__(self, z, y, x, items): #enemies, items(, paths)
        self.z = z
        self.y = y
        self.x = x
        self.items = items #items = list

    def description(self):
        self.directions()               ####]
        return "You are in a room"
    def __str__(self): return '"' + str(self.__class__.__name__) + '"' + " at X:" + str(self.x) +  " Y:" + str(self.y) + " Z:" + str(self.z)

#make moving like finding paths - done with super().north(AND ARGUMENTS ABOUT PATH DESCIPTION HERE)

class Start(Room):
    def __init__(self, z, y, x, items):
        super().__init__(z, y, x, items)
    def description(self):
        return "You are in the start room"

class Balcony(Room):
    def __init__(self, z, y, x, items):
        super().__init__(z, y, x, items)
    def description(self):
        return "You are on a balcony"



