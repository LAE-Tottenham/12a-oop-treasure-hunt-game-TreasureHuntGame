class Item:
    def __init__(self,name,xpos,ypos,hidden,character,world):
        self.name=name
        self.xpos=xpos
        self.ypos=ypos
        self.hidden=hidden
        self.character=character
        self.world=world

class Food(Item):
    def __init__(self,name,hp,xpos,ypos,character,world):
        self.hp=hp
        self.name=name
        self.xpos=xpos
        self.ypos=ypos
        self.character=character
        self.world=world

    
        
        
class Weapon(Item):
    def __init__(self,name,xpos,ypos,character,damage,world):
        self.name=name
        self.xpos=xpos
        self.ypos=ypos
        self.character=character
        self.world=world
        self.damage=damage

class NPC:
    def __init__(self,name,xpos,ypos,character):
        self.name=name
        self.xpos=xpos
        self.ypos=ypos
        self.character=character





rucksack=['apple','pear']
print (rucksack)
rucksack.append('more')
print(rucksack)
