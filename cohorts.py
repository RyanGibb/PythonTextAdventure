#This module contains class and race options and their attributes

class Race:
    def dwarf(self):
        self.race = "dwarf"
        self.race_adjective = "dwarvern"
        self.race_plural = "dwarves"
        self.race_determiner = "a"
        self.race_str = 6
        self.race_int = 4
        self.race_agl = 2
    def orc(self):
        self.race = "orc"
        self.race_adjective = "orcish"
        self.race_plural = "urqui"
        self.race_determiner = "an"
        self.race_str = 7
        self.race_int = 2
        self.race_agl = 3

class Clas:
    def warrior(self):
        self.clas = "warrior"
        self.clas_determiner = "a"
        self.clas_str = 3
        self.clas_int = 0
        self.clas_agl = 1
    def thief(self):
        self.clas = "thief"
        self.clas_determiner = "a"
        self.clas_str = 0
        self.clas_int = 2
        self.clas_agl = 2


