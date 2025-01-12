from place import Place
from player import Player
from item import Item
from character import Character





import pyfiglet as pf
from termcolor import colored, cprint
import pyfiglet
from colorama import Fore, Style





def welcome():
   styled_text = pyfiglet.figlet_format("MARVEL....... EARTH  616  AND  BEYOND", font="doom")
   print(Fore.RED + styled_text + Style.RESET_ALL)


welcome()

def display_map():
   map_text = f"""                                                  {colored(" HERE IS THE MAP OF EARTH 616 🌍.... AND BEYOND", 'light_green', attrs=['bold'])}



                                                                                                                                  {colored("Avengers Tower 🏙️ 🛡️ 🏹",attrs=['bold'] )}         
                                                                                                                                                 |
                                                                                                                                                 |
                                                        {colored(" oscorp 🕷️ 🕸️ ", 'grey', attrs=['bold'])} ------------------------------------------------------------------------------                                                                          
                                                                     |
                                                                     |
                                                                     |
     {colored("X mansion 🌲🏰🌲", 'light_yellow',attrs=['bold'] )}----------------------------------------------------
                    |
                    |
                    |
                    --------------------------------  {colored("Hell's kitchen 🏠🏪🏙️", 'light_red' , attrs=['bold'])}
                                                                     |
                                                                     |
                                                                     |
                                                                  ----------------------------------------------------   {colored("Sanctum sanctorum 🧙✨", 'blue' , attrs=['bold'])}
                                                                                                                                           |
                                                                                                                                           |
                                                                                                                                           |
                                                      {colored("Asgard 💎⚡🔨", 'yellow', attrs=['bold'] )}----------------------------------------------------------------------------
                                                                  |
                                                                  |
                                                                  |                                    
          {colored("Wakanda 🏜️🖤", 'magenta', attrs=['bold'] )}---------------------------------------------------
                     |
                     |
                     |
                     -----------------------------------------------------{colored("Ta Lo 🌺🌳🌼", 'green',attrs=['bold'] )}
                                                                                 |
                                                                                 |
                                                                                 |
                                                                                 |
                                                                              -------------------{colored("Sakaar 🌕", 'light_grey', attrs=['bold'])}     
                                                                                                         |
                                                                                                         |
                                                   {colored("Titan 🌑",'light_red', attrs=['bold'] )}-----------------------------------------------                                                                                                      

   """
   cprint(map_text, 'white')


display_map()

             






class Game(Player):
    def __init__(self, player_name):
        super().__init__(player_name)
        
        self.places = self.create_places()
        self.current_place = self.places[0]
        self.inventory = []
        self.level = 1
        self.energy = 100
        self.xp = 0
        self.quests = []
        self.infinity_stones_collected =[]

    

    def give_infinity_stone_quest(self):
      self.give_quest("Infinity Stones Collection", "Collect all 6 infinity stones and prepare for the final battle")

    def check_hidden_victory_condition(self):
      required_stones = ["Space stone", "Soul stone", "Reality stone", "Time stone", "Power stone", "Mind stone"]
      collected_stones = [item.name for item in self.inventory if item.name in required_stones]

      if len(collected_stones)== 6:
         self.hidden_victory()
         return True
      return False

    def hidden_victory(self):
      cprint(f"Congratulations! You have unlocked the true victory! Using the infinity stones, you can defeat Thanos!", 'light_yellow')
      self.xp += 500
      self.level_up()




   
    
    def create_places(self):
        avengers_tower = Place('Avengers tower', "The headquarters for the avengers ")
        x_mansion = Place('X mansion', "training ground for the X-men")
        wakanda = Place('Wakanda', "A hidden, technologially advanced African nation")
        sanctum_sanctorum = Place("Sanctum sanctorum", "Home of Dr strange ")
        ta_lo = Place("Ta Lo", "A mystical village...home to Shang-hi")
        oscorp = Place("oscorp", "A building involved in scientific research....leads to dangerous experiments!!!")
        titan = Place("Titan", "A desolate moon...the home of thanos")
        asgard = Place("Asgard", "A mythical realm")
        sakaar = Place("Sakaar", "A chaotic planet known for its gladiatorial games")
        hells_kitchen = Place("Hell's kitchen", "A gritty neighbourhood in manhattan")




        avengers_tower.add_item(Item('Space stone', "control over space", 20, "weapon"))
        avengers_tower.add_item(Item("Soul stone", "control over souls and life", 30, "weapon" ))
        sakaar.add_item(Item("Reality stone","control over reality", 25, "weapon" ))
        sanctum_sanctorum.add_item(Item("Time stone", "control over time", 20, "weapon"))
        hells_kitchen.add_item(Item("Power stone", "gives immense strength and energy", 40, "weapon"))
        asgard.add_item(Item("Mind stone", "control over minds and intelligence", 25, "weapon"))
        avengers_tower.add_item(Item("Captain america's shield", "Nearly indestructible vibranium shield", 30, "weapon"))
        oscorp.add_item(Item("Spider-man's web shooters", "devices that shoots powerful webs", 20, "weapon"))
        avengers_tower.add_item(Item("Hawkeye's bow and arrow", "A specialised bow and a variety of trick arrows", 20, "weapon"))
        asgard.add_item(Item("Mjolnir", "Thor's enchanted hammer....only lifted by those who are worthy", 70, "weapon"))
        x_mansion.add_item(Item("Wolverine's claws", "Adamantium claws", 10, "weapon"))
        avengers_tower.add_item(Item("Iron man's armour", "Advanced power armour suits", 20, "weapon"))
        sanctum_sanctorum.add_item(Item("Eye of agamotto", "A mystical amulet", 10, "weapon"))
        x_mansion.add_item(Item("Ebony blade", "A cursed sword", 15, "weapon"))
        oscorp.add_item(Item("Pym particles", "Alter the size of objects and living things", 5, "weapon" ))
        ta_lo.add_item(Item("Ten rings", "Powerful alien rings", 30, "weapon"))
        wakanda.add_item(Item("Vibranium", "Rare metal with unique properties", 5, "weapon"))
        sanctum_sanctorum.add_item(Item("Darkhold", "Mystical book of dark magic", 5, "weapon"))
        sakaar.add_item(Item("Sakaaran Battle Axe", "A powerful axe", 20, "weapon"))
        titan.add_item(Item("Infinity gauntlet", "Gauntlet capable of harnessing the infinity stones", 100, "weapon"))


        captain_america = Character("Captain america", "A super soldier", 70, "hero", "Help me fight Red skull, we can do this all day!!!" )
        red_skull = Character("Red skull", "Archenemy of Captain america", 150, "villain", "HAIL HYDRA!!! You will never be able to defeat me..")
        wolverine = Character("Wolverine", "A mutant with healing factors", 90, "hero", "We must continue to defeat magneto....give everything you got!!!")
        magneto = Character("Magneto", "A mutant with the ability to control magnetic fields", 170, "villain", "Don't get in my way....I'm unstoppable")
        black_panther = Character("black panther", "King of wakanda", 90, "hero", "Use everything you got...wakanda forever!!!")
        killmonger = Character("Killmonger", "A formidable adversary of black panther", 175, "villain", "I've waited my whole life for this fight....BRING IT ON!")
        dotor_strange = Character("Dr strange", "A former neurosurgeon who becomes the sorcerer supreme", 100, "hero", "Help me defeat Dormmamu!!")
        dormammu = Character("Dormammu", "A powerful other-dimensional entity and the ruler of the dark dimension", 200, "villain", "You will never defeat me...MUWHAHAH")
        shang_chi = Character("Shang-hi", "A master martial artist and....son of the mandarin", 170, "hero", "Help me protect our future!!")
        mandarin = Character("Mandarin", "Leader of the ten rings organisation", 220, "villain", "I've lived ten of your lifetimes, you can't defeat me")
        spider_man = Character("Spider-man", "A young hero with spider-like abilities", 150, "hero", "With great power comes great responsibility....WE NEED TO DEFEAT GREEN GOBLIN")
        green_goblin = Character("Green goblin", "A wealthy industrialist turned supervillain", 280, "villain", "You know, I'm something of a scientist myself, let me help you....we can work together")
        gamora = Character("Gamora", "A skilled assassin...adopted daughter of thanos", 100, "hero", "You must help me defeat my father....THANOS")
        thanos = Character("Thanos", "The Mad Titan", 550, "villain", "I am inevitable")    
        thor = Character("Thor", "God of Thunder", 150, "hero", "Help me defeat my brother...LOKI")
        loki = Character("Loki", "God of mischief", 310, "villain", "You cannot stop me")   
        hulk = Character("Hulk", "A scientist who transforms into a green monstrous creature when angry", 300, "hero", "HULK SMASH!!!")
        grandmaster = Character("Grandmaster", "A powerful osmi being who loves games", 370, "villain", "Let's just have a good contest...LET THE GAMES BEGIN...")
        daredevil = Character("Daredevil", "A blind lawyer with heightened senses and agility", 200, "hero", "Help me defeat Kingpin")
        kingpin = Character("Kingpin", "A powerful crime lord", 400, "villain", "You cannot stop me...")

        avengers_tower.add_hero(captain_america)
        avengers_tower.add_villain(red_skull)
        x_mansion.add_hero(wolverine)
        x_mansion.add_villain(magneto)
        wakanda.add_hero(black_panther)
        wakanda.add_villain(killmonger)
        sanctum_sanctorum.add_hero(dotor_strange)
        sanctum_sanctorum.add_villain(dormammu)
        ta_lo.add_hero(shang_chi)
        ta_lo.add_villain(mandarin)
        oscorp.add_hero(spider_man)
        oscorp.add_villain(green_goblin)
        titan.add_hero(gamora)
        titan.add_villain(thanos)
        asgard.add_hero(thor)
        asgard.add_villain(loki)
        sakaar.add_hero(hulk)
        sakaar.add_villain(grandmaster)
        hells_kitchen.add_hero(daredevil)
        hells_kitchen.add_villain(kingpin)
        avengers_tower.add_next_place(oscorp)
        oscorp.add_next_place(x_mansion)
        x_mansion.add_next_place(hells_kitchen)
        hells_kitchen.add_next_place(sanctum_sanctorum)
        sanctum_sanctorum.add_next_place(asgard)
        asgard.add_next_place(wakanda)
        wakanda.add_next_place(ta_lo)
        ta_lo.add_next_place(sakaar)
        sakaar.add_next_place(titan)

                                   
      

        return [avengers_tower, x_mansion, wakanda, sanctum_sanctorum, ta_lo, oscorp, titan, asgard, sakaar, hells_kitchen]


        
      
 
 
                            

     
       
    def show_places(self):
       cprint(f"You are currently in {self.current_place.name}", 'light_red')
       cprint(self.current_place.description, 'light_red')

       cprint(f"ITEMS IN THIS PLACE: ", 'cyan')
       for item in self.current_place.items:
          print(f" - {item.name}: {item.description}")

       cprint(f"HEROES IN THIS PLACE: ", 'yellow')
       for hero in self.current_place.heroes:
          print(f" - {hero.name}: {hero.description}")

       if self.current_place.villains:
          cprint(f"VILLAINS IN THIS CURRENT PLACE: ", 'light_magenta')
          for villain in self.current_place.villains:
             print(f" - {villain.name}: {villain.description}")
       else:
          cprint("No villains here! ", 'grey')

       cprint(f"You can go to the following Places: ", 'blue')
       for place in self.current_place.next_places:
          print(f" - {place.name}")


     
          
       


    def move(self, place_name):
       target_place = next((place for place in self.current_place.next_places if place.name.lower() == place_name.lower()), None)
      
       if target_place:
         self.current_place = target_place
             
         self.current_place = target_place
         cprint(f"Moved to {self.current_place.name}", 'light_red')
         self.show_places()
         
             
       else:
          print(f"There is no place named {place_name}")
             
          
          
       




    def pick_up(self, item_name):
       item_name = item_name.lower()
       item_to_pick = next((item for item in self.current_place.items if item_name in item.name.lower()), None)


       if item_to_pick:
         self.inventory.append(item_to_pick)
         self.current_place.items.remove(item_to_pick)
         cprint(f"You have picked up {item_to_pick.name}", 'blue')

       else:
          cprint(f"No item called {item_name} here", 'light_yellow')

    def show_inventory(self):
       if not self.inventory:
          cprint("Your inventory is empty", 'light_red')
       else:
          cprint("Your inventory contains....", 'light_green')
          for item in self.inventory:
             item_colour = item.get_item_colour()
             cprint(f" - {colored(item.name, item_colour)}: {item.description}")

    def gain_xp(self, amount):
      self.xp += amount
      if self.xp >= self.level * 100:
         self.level_up()

    def level_up(self):
      self.level += 1
      self.xp = 0
      cprint(f"Congratulations!! You leveled up to level {self.level}", 'cyan' )

    def give_quest(self, quest_name, description):
      self.quests.append({"name": quest_name, "description": description, "completed": False})
      cprint(f"Bonus mission: {quest_name} - {description}", 'green')

    def complete_quest(self, quest_name):
      quest = next((q for q in self.quests if q["name"] == quest_name), None)
      if quest:
         quest["completed"] = True
         cprint(f"Quest '{quest_name}' completed!", 'cyan')

       
    def get_map(self):
       display_map()

    def start(self):
        print(f"Welcome {player_name}, YOU ARE NOW AN AVENGER!!!")
        print(f"{player_name}, Your mission is to teleport to these different places in our universe and collect powerful weapons, defeat enemies, and interact with heroes. Are you ready for this....AVENGERS ASSEMBLE!!!")
        print("Here's a hint on how to win.....collect as many weapons as you can in each place that you visit, and defeat the villains in that area, however.... you can only use the same item 3 times so think wisely!!!")

        self.give_infinity_stone_quest()
        self.show_places()

        while True:
             opt = input("""
What would you like to do? (Enter the number)
1. Go to a Place
2. Pickup item
3. Check inventory
4. fight with villain
5. Use item
6. Talk to hero
7. get map
8. Help
9. Show items, villains, heroes and nearby places
10. Quit
                           
""")
             if opt == "1":
                self.show_places()
                place_name = input("Enter the Place you want to go to: ")
                self.move(place_name)
               


             elif opt == "2":
                item_name = input("Enter the item name: ")
                self.pick_up(item_name)
                self.show_inventory()
           
             elif opt == "3":
                self.show_inventory()


             elif opt == "4":
                villain = input("Enter the name of the villain you are going to fight: ")
                self.fight(villain)
               


             elif opt == "5":
                item_name = input("Enter the name of the item you want to use: ")
                item_to_use = None
                for item in self.inventory:
                   if item.name.lower() == item_name.lower():
                      item_to_use = item
                      break
                if item_to_use:
                   self.use_item(item_to_use)
                else:
                   ("Item not found in inventory ")


                     


             elif opt == "6":
                person_name = input("Enter the hero you want to speak to: ")
                (self.talk(person_name))


             elif opt == "7":
                self.get_map()

             elif opt == "8":
                self.get_help()

             elif opt == "9":
                self.show_places()
             
             elif opt == "10":
                print(".........End of game..............")
               
                break
           
             else:
                print("Unknown command. Type 'help' to see available commands")
       

        

    def fight(self, villain_name):
      
      villain = next((villain for villain in self.current_place.villains if villain.name.lower() == villain_name.lower()), None)
     
      if not villain:
         cprint(f"There is no villain named {villain_name}", 'light_grey')
         return

      if self.energy <= 0:
         cprint("Your health bar is low, collect more items to increase your health percentage", 'light_red')
         return
      
        
      cprint(f"You are fighting {villain.name}", 'light_magenta')
      cprint(f"{villain.name} says: {villain.dialogue}", 'blue')

      if self.check_hidden_victory_condition():
         cprint("The ininity stones are glowing, giving you immense power!", 'cyan')
         villain.health -= self.energy * 2
      
      villain.health -= self.energy
      self.energy -= 30

      cprint(f"{villain.name}'s health: {villain.health}", 'red')
      cprint(f"Your remaing health: {self.energy}", 'light_yellow')

      if villain.health <= 0:
         cprint(f"You have defeated {villain.name}!!!!", 'light_green')
         self.gain_xp(50)
         self.current_place.villains.remove(villain)

         if not self.current_place.villains:
            self.current_place.villain_defeated = True
            cprint(f"All villains in {self.current_place.name} are defeated! you can move to the next place and defeat your next villain", 'magenta')

       

   
           
 
        

    def talk(self, person_name):
       hero_to_talk = next((hero for hero in self.current_place.heroes if hero.name.lower()==person_name.lower()), None)
       if hero_to_talk:
         cprint(f"You are talking to {hero_to_talk.name}: {hero_to_talk.description}", 'light_yellow')
         cprint(f"{hero_to_talk.name} says: {hero_to_talk.dialogue}", 'light_magenta')

       else:
         cprint(f"{person_name} is not here ", 'grey')

    

   


        
        

player_name = input("Enter your name: ")
game = Game(player_name)
places = game.create_places()
player = Player(player_name)
player.current_place = places[0]
player.current_place.villains[0].defeat()
player.move_to_next_places(places)


game.start()
   


   
   
   






       