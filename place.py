import random

# Define Items and Backpack
backpack = []
items_found = []

# Function to display map
def openmap():
    print()
    print("#-------'#######---###  ----  ######  --___----######_--  --####___--- ")
    print("#-       ---                                       ---          ---")
    print(" ##               ~~~map of the maze of secrets~~~                      l")
    print("##        ~~use with caution~~~                                          |")
    print("|                                     ####____ _____ ----____--_        l")
    print("|                                     #           |     --    |        l")
    print("|                                     #           |   lair    |        l")
    print("|                                     |   castle  |    of    |         l")
    print("|                                     l           |   death   l        l")
    print("  |                                   l           l           |       l")
    print("  |         ##____________-------------________###---------__ #        l")
    print("  #      |         l         |          l          #          l        l")
    print("  #      #          |          | haunted l          #         |        l")
    print("  #      l    cave   |  mine   |  house  l  library l  forest |       l")
    print(" #       #          |         l          l          |          #        l")
    print(" ##      l          #         l          l          |           #       l")
    print(" l       ####--------#  _ ____l  ___  _l  ____    |## ________###        l")
    print("l                                                                        l")
    print("  l                                                                      l")
    print("l                                                                         l")
    print("#             ___                           __              ______##     l")
    print("--###______--##__#####___-  ####  ---######-#-   ----___==######----    -- ")
    print()

# Define Items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Create Items
axe = Item("Axe", "A sharp axe, useful for cutting trees or breaking things.")
key = Item("Key", "A rusty key, possibly for an old door.")
torch = Item("Torch", "A lit torch, illuminating the dark areas.")
hammer = Item("Hammer", "A heavy hammer, perfect for smashing things.")

# Create Room with Items
class Room:
    def __init__(self, name, description, items, clues):
        self.name = name
        self.description = description
        self.items = items
        self.clues = clues
    
    def describe(self):
        print(self.description)
        print("Items available in this room:")
        for item in self.items:
            print(f"- {item.name}: {item.description}")
        print("Clues:")
        for clue in self.clues:
            print(f"- {clue}")

# Function to move between rooms
def move_to_next_room(room):
    print(f"\nYou enter the {room.name}.")
    room.describe()

# Function to place items on pedestal
def place_item_on_pedestal(item_name, pedestal_items):
    if item_name in pedestal_items:
        pedestal_items.remove(item_name)
        print(f"You have placed the {item_name} on the pedestal.")
    else:
        print(f"The {item_name} is not needed for the pedestal.")

# Abandoned Cottage Puzzle
def abandoned_cottage():
    print("\nYou enter an abandoned cottage, its wooden floor creaks under your feet.")
    print("There is a pedestal in the center of the room with a sign that reads: 'Place the right items on the pedestal to proceed.'")
    
    # Define rooms with items and clues
    living_room = Room("Living Room", 
                       "The living room is dusty, with cobwebs in the corners. You see some items scattered around.", 
                       [axe, key, torch], 
                       ["You use this to cut down a tree.", "This opens an old door."])
    
    kitchen = Room("Kitchen", 
                   "The kitchen is in disarray, with old plates and food scattered about. There's a drawer with tools.", 
                   [hammer], 
                   ["This can help you break things open."])
    
    bedroom = Room("Bedroom", 
                   "The bedroom is empty except for a few old pieces of furniture. There are some drawers that might contain something useful.", 
                   [key], 
                   ["This could unlock a door."])
    
    pedestal_items = ["Axe", "Key", "Torch", "Hammer"]
    
    rooms = [living_room, kitchen, bedroom]
    found_items = []

    # Game Loop: Move through rooms and collect items for pedestal
    while pedestal_items:
        print("\nWhere would you like to go?")
        print("1. Living Room")
        print("2. Kitchen")
        print("3. Bedroom")
        choice = input("Choose a room (1, 2, 3): ")

        if choice == "1":
            move_to_next_room(living_room)
            item_choice = input("\nWhat item would you like to take from this room? ")
            if item_choice == "Axe":
                found_items.append("Axe")
                print("You have taken the Axe.")
            elif item_choice == "Key":
                found_items.append("Key")
                print("You have taken the Key.")
            elif item_choice == "Torch":
                found_items.append("Torch")
                print("You have taken the Torch.")
            else:
                print("Invalid item.")
        
        elif choice == "2":
            move_to_next_room(kitchen)
            item_choice = input("\nWhat item would you like to take from this room? ")
            if item_choice == "Hammer":
                found_items.append("Hammer")
                print("You have taken the Hammer.")
            else:
                print("Invalid item.")
        
        elif choice == "3":
            move_to_next_room(bedroom)
            item_choice = input("\nWhat item would you like to take from this room? ")
            if item_choice == "Key":
                found_items.append("Key")
                print("You have taken the Key.")
            else:
                print("Invalid item.")
        
        else:
            print("Invalid room choice. Try again.")

        # Check if player has gathered enough items for the pedestal
        print("\nWhat would you like to do next?")
        print("1. Place item on pedestal")
        print("2. Continue searching the rooms")
        action = input("Choose an action (1 or 2): ")

        if action == "1":
            item_to_place = input("\nWhich item would you like to place on the pedestal? ")
            if item_to_place in found_items:
                place_item_on_pedestal(item_to_place, pedestal_items)
                found_items.remove(item_to_place)
            else:
                print("You do not have this item.")

        elif action == "2":
            continue
        else:
            print("Invalid action. Try again.")

    print("\nYou have placed all the required items on the pedestal!")
    print("The pedestal glows and a hidden door opens, leading to the next room.")
    print("You have successfully solved the puzzle!")

# Start the game
def start_game():
    print("Welcome to the Maze of Secrets!")
    print("In this part of your journey, you must find and place the correct items on the pedestal to unlock the next room.")
    abandoned_cottage()

start_game()
