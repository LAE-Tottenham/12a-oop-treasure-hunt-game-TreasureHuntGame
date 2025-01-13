class Player:
    def __init__(self, name, max_weight):
        self.name = name
        self.current_location = None
        self.inventory = []
        self.max_weight = max_weight

    def move(self, direction):
        if direction in self.current_location.connections:
            self.current_location = self.current_location.connections[direction]
            print(f"You moved to {self.current_location.name}.")
            self.current_location.describe()
        else:
            print("You can't go that way.")

    def pick_up(self, item_name):
        item = self.current_location.get_item(item_name)
        if item:
            if self.can_carry(item):
                self.inventory.append(item)
                print(f"You picked up {item.name}.")
            else:
                print("You can't carry that much weight!")
        else:
            print(f"No {item_name} found here.")

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name:
                self.inventory.remove(item)
                self.current_location.add_item(item)
                print(f"You dropped {item.name}.")
                return
        print(f"You don't have {item_name} in your inventory.")

    def can_carry(self, item):
        return sum(i.weight for i in self.inventory) + item.weight <= self.max_weight

    def view_inventory(self):
        if self.inventory:
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item.name}: {item.description}")
        else:
            print("Inventory is empty.")

class Place:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.connections = {}
        self.entities = []

    def add_connection(self, direction, place, reverse_direction):
        self.connections[direction] = place
        place.connections[reverse_direction] = self

    def add_item(self, item):
        self.items.append(item)

    def get_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name:
                self.items.remove(item)
                return item
        return None  # Item not found

    def describe(self):
        print(f"{self.name}: {self.description}")
        if self.items:
            print("Items here:")
            for item in self.items:
                print(f"- {item.name}: {item.description}")
        if self.connections:
            print("Exits:")
            for direction in self.connections:
                print(f"- {direction}")
        if self.entities:
            print("You see:")
            for entity in self.entities:
                print(f"- {entity.name}")

class Item:
    def __init__(self, name, weight, description):
        self.name = name
        self.weight = weight
        self.description = description

class Person:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def talk(self):
        print(f"{self.name} says:")
        for question, response in self.dialogue.items():
            print(f"Q: {question}")
            print(f"A: {response}")

class Enemy:
    def __init__(self, name, health, strength, loot):
        self.name = name
        self.health = health
        self.strength = strength
        self.loot = loot

    def attack(self, player):
        print(f"{self.name} attacks {player.name}! You lose {self.strength} health points.")

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} is defeated!")
            return self.loot
        else:
            print(f"{self.name} has {self.health} health remaining.")
        return []

def setup_game():
 ]
    outside = Place("Outside", "You are standing outside a spooky building.")
    entrance = Place("Entrance", "You are in the entrance hall. There's a faint smell of dust and old wood.")
    room_1 = Place("Room 1", "An empty room with a broken chair in the corner.")

    outside.add_connection("north", entrance, "south")
    entrance.add_connection("west", room_1, "east")

    red_key = Item("Red Key", 1, "A small, shiny key painted red.")
    sword = Item("Sword", 5, "A sharp blade. Useful for fighting enemies.")

    outside.add_item(red_key)
    room_1.add_item(sword)

    narrator = Person("Narrator", {"defeat the enemy"})
    enemy_1 = Enemy("Goblin", 10, 2, [red_key])

    entrance.entities.append(narrator)
    room_1.entities.append(enemy_1)


    player = Player("Adventurer", 10)
    player.current_location = outside

    return player

player = setup_game()

def game_loop(player):
    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "move":
            direction = input("Which direction? ").strip().lower()
            player.move(direction)

        elif command == "inventory":
            player.view_inventory()

        elif command == "pickup":
            item_name = input("Pick up what? ").strip().lower()
            player.pick_up(item_name)

        elif command == "drop":
            item_name = input("Drop what? ").strip().lower()
            player.drop_item(item_name)

        elif command == "interact":
            if player.current_location.entities:
                for entity in player.current_location.entities:
                    if isinstance(entity, Person):
                        entity.talk()
                    elif isinstance(entity, Enemy):
                        print(f"You encounter a {entity.name}!")
            else:
                print("There's no one to interact with here.")

        elif command == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Unknown command.")

game_loop(player)
