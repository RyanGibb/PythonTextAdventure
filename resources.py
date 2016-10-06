#This module conatains information on items, weapons, armour and any other resources that need atributes stored

class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "Name: {}\nType: Item\nDescription: {}\nValue: {}".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__("Gold", "A heavy gold coin", amount)


#class Weapon(Item):
#    def __init__(self, name, description, value, damage):
#        self.damage = damage
#        super().__init__(name, description, value)
#    def __str__(self):
#        return "Name: {}\nType: Weapon\nDescription: {}\nDamage: {}\nValue: {}".format(self.name, self.description, self.damage, self.value)

#class Rock(Weapon):
#    def __init__(self):
#        super().__init__(name = "Rock", description = "heavy", value = "1", damage = "5")



#class sword/cutting

#class blunt_cleaving/blunt

#class polearm/penetrating/stab
    #e.g. spear, pike, poleaxe, halberd, lance

#class ranged
    #darts to bows, etc





#https://en.wikipedia.org/wiki/List_of_medieval_weapons


#add sub weapon classes like blunt, stab, ect
#and ranged
#and long (like poles/pikes)



#inport resources from .txt file?



