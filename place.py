import pyfiglet as pf
from termcolor import colored, cprint

class Place():
    def __init__(self, given_name, description):
       
        self.name = given_name
        self.description = description
        self.items = []
        self.heroes = []
        self.villains = []
        self.next_places = []
        self.villain_defeated=False
        
        
       

    def add_next_place(self, place):
        self.next_places.append(place)

    def add_item(self, item):
        self.items.append(item)
        # add code here
        pass
    def add_hero(self, hero):
        self.heroes.append(hero)

    def add_villain(self, villain):
        self.villains.append(villain)

    def show_next_places(self):
        if not self.next_places:
            print(f"There are no places to go from here. ")
        else:
            print(f"You can go to the following places: ")
            for place in self.next_places:
                print(f" - {place.name}")

    def show_places(self):
       print(f"You are currently in {self.current_place.name}")
       print(self.current_place.description)

       if self.current_place.items:
          cprint("ITEMS AVAILABLE IN YOUR CURRENT PLACE:", 'light_magenta') 
          for item in self.current_place.items:
             print(f" - {item.name}: {item.description}")  
       else:
          cprint("NO ITEMS AVAILABLE HERE", 'light_yellow')

       if self.current_place.heroes:
          cprint("HEROES IN THIS CURRENT PLACE:", 'light_green')
          for hero in self.current_place.heroes:
             print(f" - {hero.name}: {hero.description}")
       else:
          print("NO HEROES HERE ")

       if self.current_place.villains:
          cprint("VILLAINS IN THIS CURRENT PLACE: ", 'light_blue')
          for villain in self.current_place.villains:
             cprint(f"- {villain.name}: {villain.description}")
       else:
          cprint("NO VILLAINS HERE", 'light_green')


    def defeat_villain(self, villain_name):
        villain = None
        for v in self.villains:
            if v.name.lower() == villain_name.lower():
                villain = v
                break 
        
        if villain:
            villain.health = 0
            self.villain_defeated = True
            cprint(f"{villain.name} has been defeated")
        else:
            cprint(f"No villain named {villain_name} found here", 'light_green')
            

    
    def __str__(self):
       return f"{self.name}: {self.description}"
    
