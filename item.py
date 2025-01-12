from termcolor import colored
from colorama import init

class Item():
    def __init__(self, name, description, value, item_type):
        self.name = name 
        self.value = value
        self.description = description 
        self.type = item_type
        self.effect_value = value
        self.use_count = 0

    def use_item(item_name):
        print(f"You used the item_name")
      

    def get_item_colour(self):
        if self.name == "Space stone":
            return 'blue'
        elif self.name == "Soul stone":
            return 'yellow'
        elif self.name == "Reality stone":
            return 'red'
        elif self.name == "Time stone":
            return 'green'
        elif self.name == "Power stone":
            return 'magenta'
        elif self.name == "Captain America's sheild":
            return 'light_red'
        elif self.name == "Spider-man's web shooters":
            return 'red'
        elif self.name == "Pym particles":
            return 'cyan'
        elif self.name == "Wolverine's claws":
            return 'dark_grey'
        elif self.name == "Hawkeye's bow and arrow":
            return 'light_blue'
        elif self.name == 'Mjolnir':
            return 'grey'
        elif self.name == "Iron's man's armour":
            return 'red'
        elif self.name == "Eye of agammotto":
            return 'light_green'
        elif self.name == "Ebony blade":
            return 'light_grey'
        elif self.name == 'Pym particle':
            return 'blue'
        elif self.name == 'Ten rings':
            return 'red'
        elif self.name == "Vibranium":
            return 'light_magenta'
        elif self.name == 'Darkhold':
            return 'light_grey'
        elif self.name == "Sakaarab Battle Axe":
            return 'light_cyan'        
        elif self.name == "Infinity gaunlet":
            return 'yellow'


  
       