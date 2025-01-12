import pyfiglet as pf
from termcolor import colored, cprint

class Player():
    def __init__(self, name):
        self.name = name
        self.inventory_max_weight = 50
        self.inventory = []
        self.current_place=None
        self.health = 50
        self.energy = 50
        self.item_usage_count = {}
        self.level = 0
        
       

       

    def calculate_inventory_size(self):
        return sum(item.weight for item in self.inventory)
    

    def add_item(self, item_instance):
        if self.calculate_inventory_size() + item_instance.weight <=self.inventory_max_weight:
            self.inventory.append(item_instance)
            cprint(f"{item_instance.name} added to inventory", 'green')
        else:
            cprint("Your inventory is full...", 'red')

    def use_item(self, item_to_use):
        if item_to_use.use_count < 3:
            self.energy += item_to_use.value
            item_to_use.use_count += 1
            cprint(f"You have used {item_to_use.name} Your health bar is at {self.energy}", 'green')
            cprint(f"{item_to_use.name} has been used {item_to_use.use_count} times", 'yellow')
        else:
            cprint(f"Sorry, you cannot use {item_to_use.name} anymore. It has been used 3 times", 'red')

        

    def display_stats(self):
        print(f"Health: {self.health}, Energy: {self.energy}")

        
    
    def get_inventory(self):
        if not self.inventory:
            cprint(f"Your inventory is empty", 'cyan')
        else: 
            cprint("Your iventory contains...", 'light_green')
            for item in self.inventory:
                item_colour = item.get_item_colour()
                print(f" - {colored(item.name, item_colour )}: {item.description}")

       
    
    def move(self, direction):
        next_place = None
        for place in self.current_place.next_places:
            if direction.lower() == place.name.lower():
                next_place = place
                break 
            if next_place:
                self.current_place = next_place
                print(f"Moved to {self.current_place.name}")
            else:
                print(f"You cannot move to {direction} from here ")


   
    def pick_up(self, item_name):
        item_to_add = None
        for item in self.current_places.items:
            if item_name.lower() == item_name.lower():
                item_to_add = item
                break 
        if item_to_add:
            self.inventory.append(item_to_add)
            self.current_place.items.remove(item_to_add)
            cprint(f"You have picked up{item_to_add.name}", 'light_yellow')
        else:
            cprint(f"Item {item_name} not found", 'light_grey')
       
    
    def talk(self, npc_name):
        npc = next((npc for npc in self.npcs if npc.name.lower() == npc_name.lower()), None)
        if npc:
            return npc.interact()
        else:
            return f"{npc_name} is not here "
    
    def fight(self, villain_name):
        return f"You have defeated {villain_name}"
    
    def get_map(self):
        map_text = """
                     MAP OF THE STRANGE TOWN

                  home                     library 
                  
                  
                   garden   
     
     forest                                              mountains 

                                   palace
        cave

             park                    cafe                          desert   
             
 """
  
        cprint(map_text, 'green')

    def get_help(self):
        cprint("Collect all the items in the places on Earth 616 and the universe, defeat the villains in each of those places....and prepare for thr final fight with...THANOS", 'light_cyan')

    def __str__(self):
        return f"Player {self.player_name} is in {self.current_place.name} with {len(self.inventory)} items in the inventory"
    
    def move_to_next_places(self, places):
        if self.level < len(places):
            next_place = places[self.level]
            if self.current_place != next_place:
                self.level +=1
                self.current_place = places[self.level - 1]
                cprint(f"Moved to {self.current_place.name}", 'red')
            else:
                return


        else:
            cprint("You have completed all levels", 'green')
      