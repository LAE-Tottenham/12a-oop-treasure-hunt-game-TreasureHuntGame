input63=" "
hasshield=True
def ancient_castle():

    print()
    print("You step into the ancient abandoned castle.")
    input63=" "
    while input63 !="a":
        input63=input("press a to continue")

    print()
    print("The walls are covered in dust, and cobwebs hang from the ceilings. A cold, eerie wind whispers through the halls.")
    print("You hear distant sounds of movement. There are two staircases ahead.")
    print("One leads upward, to the unknown heights of the castle. The other leads down, where the air smells damp and musty.")


    input61 = " "
    while input61 != "a" and input61 != "b":
        print()
        print("What would you like to do?")
        print("a. Go upstairs.")
        print("b. Go downstairs.")
        input61 = input().lower()

    if input61 == "a":
        print("You decide to go upstairs. The staircase creaks beneath your weight, and the air grows colder with every step.")
        print("At the top, you find a large, dusty room with old furniture covered in sheets.")
        print("Suddenly, a loud noise from behind you makes you turn around!")
        print("A goblin appears, brandishing a rusted sword!")

    elif input61 == "b":
        print()
        print("You decide to go downstairs. The air smells damp, and you can hear faint dripping sounds.")
        print("In the corner, you spot an old shield leaning against the wall. You approach it carefully and add it to your inventory.")
        print("You hear a noise coming from the darkness ahead. Suddenly, a goblin jumps out of the shadows, wielding a rusted sword!")

        

        hasshield=True
        print("You now have a shield!")

    print()
    print("The goblin snarls and charges at you! You have to fight it!")
    print("The goblin's attacks are fierce, and it strikes you with a couple of quick blows.")
    
    if hasshield==True:
        print("You block one of the goblin's attacks with your shield, but the goblin is still strong!")
    else:
        print("You don't have a shield, and the goblin's attack hits you hard!")

    print("You're on the verge of losing the battle! Your strength is waning...")
    print("You remember the strength potion you have in your backpack.")
    print()
    print("You drink the strength potion and feel a surge of power! Your strength is renewed.")
    print("You push back the goblin, overwhelming it with your newfound strength.")

    print()
    print("With your renewed power, you defeat the goblin and stand victorious!")

    print()
    print("Everything goes dark...")

    print()
    print("You awaken in a dimly lit room. The walls are lined with glittering treasures: gold coins, jewels, and ancient artifacts.")
    print("You can hardly believe your eyes. This must be the Ancient Treasury, long forgotten by time.")
    print("The air is thick with the scent of old riches, but there’s something else... an eerie silence fills the room.")


    input62 = " "
    while input62 != "a" and input62 != "b":
        print()
        print("What would you like to do?")
        print("a. Examine the treasure in front of you.")
        print("b. Search the back of the room for hidden secrets.")
        input62 = input().lower()

    if input62 == "a":
        print()
        print("You examine the treasure before you, but as you touch the coins, they crumble to dust!")
        print("It seems these treasures are not meant for mortal hands.")
    elif input62 == "b":
        print()
        print("You approach the back of the room, carefully searching for anything that might hold more value.")
        print("After moving aside some old crates, you find a hidden door that leads to a deeper part of the castle.")
        print("This must be where the true secrets of the castle lie!")
    
    print()
    print("Your journey has only just begun. What awaits you beyond the hidden door is unknown...")

print(ancient_castle())