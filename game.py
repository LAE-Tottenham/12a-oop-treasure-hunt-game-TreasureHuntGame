import pyfiglet
#--------------------------------------------------------------------------------

class rooms:
    def __init__(self,name):
        self.name=name

    def enterroom(self):
        print("you have entered the "+self.name)    

class object:
    def __init__(self,name,):
        self.name=name

    def useobject(self):
        print("you are using"+self.name)    
                

#myobject=object("sword")    
#myobject.useobject()

class npc:
    def __init__(self,name):
        self.name=name


class monster:
    def __init__(self,name):
        self.name=name 

#--------------------------------------------------------------------------------

room1=rooms("cave")
room2=rooms("abandoned mine")
room3=rooms("haunted house")
room4=rooms("secret library")
room5=rooms("dark room")
room6=rooms("deserted castle")
room7=rooms("ancient treasury")
room8=rooms("lair of death")


goldensword=object("golden sword")
goldenkey=object("golden key")
map=object("map")
diamondsword=object("diamond sword")
bowandarrow=object("bow and arrow")
potion=object("potion")
armor=object("armor")
shield=object("shield")
magicalstone=object("magical stone")
magicstaff=object("magic staff")
mysteriousbook=object("mysterious book")


#--------------------------------------------------------------------------------
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

#map=openmap()  

def talktonpc1():
    print()
    print("welcome to the maze of secrets")
    print("your task is to get through all the rooms, complete puzzles collect objects to help you escape")
    print("be careful, there are monsters that can kill you, if you die you die in real life "+"\U0001F608")
    print("dont worry, you can find weapons to help you defeat the monsters")
    print()
    input2345=input("press a to continue ")
    print("the figures sinister message fills you with a sense of unease but you must ecape!")

def solve_riddle():
    print()
    print("You approach the cold, moss-covered wall.")
    print("Etched into the stone is a riddle, faint but legible:")
    print()
    print("I have keys but open no locks. I have space but no room. You can enter, but you can’t go outside. What am I?\"")
    print()

    correct_answer=False
    key=False

    while not correct_answer:
        answer = input("enter the answer: ")
        answer=answer.lower()
        if answer == "keyboard":
            print("The wall rumbles and a hidden compartment opens, revealing a rusty key 🔑")
            key = True
            correct_answer = True
        elif answer == "hint":
            print("Hint: What are you using to play this game?")
        else:
            print("That’s not correct. Try again, or type 'hint' for a clue.")
    
    if key:
        print("You now have the key to continue your journey.")



#-------------------------------------------------------------------------------
styled_text=pyfiglet.figlet_format('MAZE OF SECRETS',font='doom')
print(styled_text)

backpack=[]

s=" "
while s!="s":
    s=input("enter s to start ")
#--------------------------------------------------------------------------------
################################    room 1   #####################################


print("You wake up in a cold, shadowy cave")
print("In the distance, a folded parchment lies on the ground, and a mysterious figure looms in the darkness....")

hasmap=False
completed=False

input1=" "
print()
print("press a to talk to the mysterious figure")
print("press b to pick up the parchment")
input1=" "
while input1!="c":
    input1=input()
    if input1=="a":
        output=talktonpc1()  
        completed=True
    elif input1=="b":
        print()
        print("you have found the map 📜")
        print("You feel a sense of hope rise within you as you realize this map might be your key to escaping.")
        print("the map is in your backpack, remember you can only hold 6 items at once")
        backpack.append("map")
        hasmap=True
    elif input =="c" and completed==True:
        ("you can now enter the abandoned mine")   
    elif input1=="m":
        print(openmap())    
    elif input1 !="c":
        print("try again")
    print()
    print("press a to talk to the mysterious figure")
    print("press b to pick up the parchment")
    if completed==True and hasmap==True:
        print("press c to go to the next room")
    if hasmap==True:
        print("press m to open map")    






#-------------------------------------------------------------------------------------------
#####################################   room 2   ##############################################
print()
input21=" "
while input21!="a":
    input21=input("press a to continues ")
print()    
print("You step cautiously into the abandoned mine ⛏️, the air is cold and stale and the ground is covered with jagged rocks ")
print("you spot strange symbols carved into the wall, faint but unmistakably deliberate.")
print("As you explore, your gaze catches something glinting on the ground,a shiny object buried in the dirt.-its a golden sword!")
print()
x=" "
while x!="a":
    x=input("press a to pick up the sword ")
print("you have picked up the sword🗡️")
print("you feel relieved, knowing you have a chance of defending yourself in this place...")
backpack.append("sword")
print()

key=False
input23=" "
while input23!="b":
    print()
    print("press a to examine the writing")
    print("press b to enter the next room")
    print("press m to open map")
    input23=input()
    if input23=="a":
        output=solve_riddle()
        key=True
        print(output)
    elif input23=="b" and key==True:
        print()
        print("you can now enter the next room")   
    elif input23=="b" and key==False:
        print()
        print("you need a key to open the door")
        print()
        input23=" "  
    elif input23=="m":
        print(openmap())       
    else:
        input23=" "




#------------------------------------------------------------------------------------------------------
####################################    room 3   ###############################################


print()
print("you have entered the haunted house")
input33=" "
while input33 !="a":
    input33=input("press a to continue  ")
print()
print("an eerie voice whispers behind you, filling you with a sense of unease....")
print()
print("impressive..... You solved the riddle. But dont think that this is over! Every step you take brings you closer to your doom. I will be waiting in the darkness..... watching as you struggle. So enjoy this small triumph, for it will be your last. MWAHAHAHAHAHAHAH")
print()
print("the voice fades...but its message still echoes in your ears.... a cold shiver runs down your spine")
print("The warning only pushes you to move forward. You can’t let fear hold you back.")
print()
input31=" "
while input31 !="a":
    input31=input("press a to continue  ")
print()    
print("you decide to look around the house, a dull fog wraps around its decaying structure, ")
print("Piles of bones and skeletons are scattered across the floor, some leaning against the crumbling walls")
print("The staircase rises steeply, its steps covered in dust, and at the top, a heavy door looms like a barrier between you and the unknown.")
print("you notice that your only path is to go up the stairs...")
print()
input32=" "
while input32 !="a":
    input32=input("enter a to go up the stairs ")


def room3_monster():
    print()
    print("A terrifying creature emerges from the shadows! Its massive form towers over you, with glowing red eyes and sharp teeth gleaming in the dim light.")
    print("You have the option to:")
    print("a. Distract the monster.")
    print("b. Kill it with the golden sword.")
    print("c. Run away while you still can.")
    
    combat_choice=input()

    if combat_choice == "a":
        print("You attempt to distract the monster with a loud noise. But it turns toward you and pounces")
        print("You have died.")
        exit(0)
    elif combat_choice == "b":
        print("You unsheathe the golden sword and strike the monster down with a powerful blow. It lets out a terrible roar before collapsing to the ground.")
        print("You have defeated the monster!")
    elif combat_choice == "c":
        print("You turn to flee, but the monster is too fast. It chases you, and your heart races with fear.")
        print("as you run, something within you shifts. The adrenaline kicks in, and you decide you won’t go down without a fight!")
        print("You turn around, drawing the golden sword, and charge back at the monster.")
        print("The battle is fierce, but with the strength of the golden sword, you strike a fatal blow, defeating the creature at last.")
        print("You have slain the monster!")
    else:
        print("Invalid choice. The monster seizes the opportunity to attack and kills you instantly.")
        print("You have died.")
        exit(0)
output=room3_monster()
print(output)

print("you can now enter the secret library 📚")
print()


#------------------------------------------------------------------------------------------------------
###################################   room 4    ##############################################################

input44=" "
while input44 !="a":
    input44=input("press a to continue  ")

print(" Ancient books line the dusty shelves, their pages yellowed and brittle. The air is thick with an unsettling silence,.")
print(" In the dim light, a shadowy figure stands motionless, an old man cloaked in tattered robes")
print()
input4=" "
doorunlocked=False
nextroom=" "
while input4 !="c" and input4 != "d":
    print("press a to inspect the bookshelves.")
    print("press b to ask the old man for more information.")
    if doorunlocked==True:
        print("press c to enter the twisted forest🌲")
        print("press d to enter the abandoned castle🏰s")
    print("press m to look at map")
    input4=" "
    input4=input()
    if input4 == "a":
        print("You walk towards the bookshelves and begin scanning the spines of the many books")
        print("You search the shelves and spot a small vial tucked behind an old book. It's a glowing green potion, labeled 'Essence of strength'.")
        input41=" "
        while input41 !="a":
            input41=input("press a to pick up the potion ")
        print("You now have the Essence of strength potion!")
        print()
    elif input4=="m":
        print(openmap())
    elif input4 == "b":
        print("'To proceed, you must solve my riddle,' the old man says, his lips curling into asmile.")

        print()
        print("The old man asks in a low, mysterious tone: 'The more of me there is, the less you see. What am I?'")
        correctanswer=False
        while correctanswer==False:
            player_answer = input("enter your answer: ").lower()
            if player_answer == "hint":
               print("The old man’s eyes glimmer as if amused by your request. 'Very well... Here is your hint.'")
               print("Hint: I am something that grows as the light fades.")
            elif player_answer == "darkness":
                print("He nods slowly, his voice echoing, 'You have answered correctly.'")
                print()
                input43=" "
                while input43 !="a":
                    input43=input("press a to continue  ")
                correctanswer=True
            else:
                print("incorrect,  Think carefully.'")

        print("you answered the riddle but to your surprise nothing happens, but it must be a clue")
        print("confused, you approach the old man.")
        print("'Now,' he whispers, his voice barely audible, 'Look at the bookshelf ahead. Four books glow with an eerie light. Choose wisely.'")
        print("He gestures towards a shelf that holds four glowing books. The titles read:")
        print()
        print("a. 'The Realm of Darkness'")
        print("b. 'The Lost Echoes'")
        print("c. 'The Forbidden spellbook'")
        print("d. 'tales of an evil wizard'")  
        print()

        input42=" "
        while input42 != "a":
            input42=input("choose the correct book")
            if input42 =="b":
                print()
                print("you inspect the book but dont find anything useful...try again")
            elif input42 =="c":
                print()
                print("incorrect.try again")
            elif input42 =="a":
                print()
                print("this must be the one! inside the book you find a crumpled sheet of paper with a clue!")
                print()
                print("'The key to the door is not where the light shines brightest, but where the shadows hide secrets.'")
                print("you walk towards the darkest corner of the library, you find a lever and pull it")
                print()
                print("suddenly you hear the sound of doors open. you realise that you have two choices:The twisted forest or the abandoned castle")
                doorunlocked=True
            else:
                print()
                print("try again")
    elif input4 == "c":
        nextroom="twisted forest"
    elif input4 == "d":
        nextroom="abandoned castle"
    elif input4 == "m" and hasmap==True:
        print(map)
    else:
        print("try again")   

#----------------------------------------------------------------------------------------------------        
####################################    room 5    ####################################################
def twisted_forest(backpack):
    print()
    print("You have entered the Twisted Forest.")
    print()
    print("The air is thick with mist, and the trees seem to whisper among themselves.")
    print("The forest is dense and foreboding, with multiple paths leading deeper into the woods.")
    print("You feel an unsettling presence around you...")
    print()

    input51 = " "
    while input51 != "a" and input51 != "b" and input51 != "c":
        print()
        print("What would you like to do?")
        print("a. Follow the sound of distant whispers")
        print("b. Examine a glowing flower by your feet")
        print("c. Head down one of the shadowy paths")
        input51 = input()

    if input51 == "a":
        print()
        print("You follow the sound of the voices, deeper into the forest. The air grows colder")
        print("you suddenly hear a low intimidating wisper, and turn around but theres nothing there, you decide the venture further")
        print("Suddenly, a large creature with glowing eyes and broad wings appears in front of you!")
        print("You must choose what to do:")
        input52 = " "
        while input52 != "a" and input52 != "b":
            print("a. Try to communicate with the creature.")
            print("b. Fight the creature with your sword.")
            input52 = input()

        if input52 == "a":
            print()
            print("The creature lets out a low growl, but then seems to understand you. It nods and moves aside, letting you pass.")
            print("You continue deeper into the forest.")
        elif input52 == "b":
            print()
            print("You draw your sword and charge at the creature. It's a tough battle, but with your strength, you defeat it!")
            print("You move on, now with a slight sense of victory.")
        
    elif input51 == "b":
        print()
        print("You bend down and examine the glowing flower. It seems to be magical!")
        print("As you touch it,a metallic shield appears. You now possess the shield of protection.")
        backpack.append("shield")
        print("The flower disappears, and you are left with a sense of wonder.")
        backpack.append("shield")
    
    elif input51 == "c":
        print()
        print("You decide to head down one of the shadowy paths. The trees seem to close in around you as you walk.")
        print("After a while, you reach a fork in the path. Two ways lie ahead:")
        print("a. Take the left path towards a distant light.")
        print("b. Take the right path that leads to a dark cave.")
        
        input53 = " "
        while input53 != "a" and input53 != "b":
            input53 = input("Which path will you choose? ")

        if input53 == "a":
            print()
            print("You follow the light and find yourself in a clearing, with a beautiful, ancient tree in the center.")
            print("you hear a faint whisper, and turn around but theres nothing there, you decide the venture further-you must keep going!")
            print("There is an inscription on the tree that reads: 'To find the heart of the forest, you must leave no path untaken.'")
            print("You feel this is an important clue.")
        elif input53 == "b":
            print()
            print("You head into the dark cave. It ’s eerily silent, and the air is cold.")
            print("you hear a faint whisper, and turn around but theres nothing there, you decide the venture further")
            print("Inside, you find a hidden chest! It contains a rare gemstone that could help you later.")
            backpack.append("rare gemstone")

    print()
    print("You've made it through this part of the Twisted Forest. The path ahead is still unclear...")
    print("you turn to continue exploring but a door appears infront of you, its intricate engravings pull you closer....")
    print()
    print("you reach your hand out to open it, but suddenly the forest fades into darkness...")
    print()
    return  

#------------------------------------------------------------------------------------------------------
#################################     room 6    #######################################################
input63=" "
def ancient_castle(backpack):

    print()
    print("You step into the ancient abandoned castle.")
    input63=" "
    while input63 !="a":
        input63=input("press a to continue  ")

    print()
    print("The walls are covered in dust, and cobwebs hang from the ceilings. A cold, eerie wind whispers through the halls.")
    print("you hear a faint whisper, and turn around but theres nothing there, you decide the venture further")
    print("There are two staircases ahead.")
    print("One leads upward, to the unknown heights of the castle. The other leads down, where the air smells damp and musty.")


    input61 = " "
    while input61 != "a" and input61 != "b":
        print()
        print("What would you like to do?")
        print("a. Go upstairs.")
        print("b. Go downstairs.")
        input61 = input()

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
    
    if "shield" in backpack:
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
        input62 = input()

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
    print("you reach your hand out to open the door when everything goes dark.....")



if nextroom=="twisted forest":
    x=twisted_forest()
    print()
elif nextroom=="abandoned castle":
    x=ancient_castle(backpack)
    print(x)    

#-------------------------------------------------------------------------------------------------------------------
import random

input7=" "
while input7!="a":
    input7=input("press a to continue  ")
print()    
print("You slowly open your eyes. The world around you is shrouded in darkness. You can barely make out your surroundings.")
print()
print("The cold, damp air clings to your skin.")
print("The walls around you are broken and dilapidated, with large cracks running through them.")
print("Ancient, crumbling statues loom in the corners of the room, their features worn and distorted, it is as though this place holds long-forgotten memories of death and despair.")
print()
print("Suddenly, a strange presence fills the air, sending an icy chill down your spine. Something... or someone... is watching you.")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue  ")
print()    
print("'You are here at last... Welcome to the Lair of Death.'")
print("'I have been watching you... all this time. You are but a pawn in my game.'")
print("'I am the Demon of Terror, the final boss you could never defeat.'")
print()
print("'I have waited patiently for your arrival. Now, the time has come.'")
print("'No one has ever escaped the Lair of Death... and neither shall you.'")
print("The demon laughs manically.")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue  ")
print()    
print("You realize this is who you have been hearing the whole time.")
print("You have been playing their games....")
print("A sense of unease grows in your stomach...")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue  ")
print()    
print("A faint red glow begins to emanate from the shadows. You feel the ground tremble beneath you.")
print("Suddenly, the shadows form a menacing figure: the Demon of Terror, its eyes glowing with malice 👹")
print("A tall menacing shadow looms over you, its face concealed with a large, dark hood, its bony long fingers point at you mockingly.")
print("It steps forward, its voice echoing in your mind, 'Prepare yourself.'")
print("You feel your heart racing. There's no turning back.")
print()
input7=" "
while input7!="a":
    input7=input("press a to continue  ")

print("The anticipation grows as you ready yourself for the fight. The room is still... for now.")
print("You can feel the Demon of Terror preparing for the final showdown...")

print("A heavy silence fills the room....")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue  ")

############################################################################################################################
playerhealth = 100
player_attack_power = 15
bosshealth = 150
boss_attack_power = 20
special_ability = "Shadow Blast"

backpack = ["shield", "golden sword", "healing potion", "armor", "magical staff"]

print()
print(f"Your health: {playerhealth}")
print(f"final boss's health: {bosshealth}")
print()

while input7!="a":
    input7=input("press a to continue  ")

print("The evil monster cackles, 'You'll never get out alive!'")
print("Before you can react, it extends its long arm in front of it, and effortlessly causes a giant boulder to explode, sending small bits of rocks flying at you.")
print()
print("You don't dodge it in time!")
print("You take 5 damage")
playerhealth -= 5
print()
print(f"Your health: {playerhealth}")
print(f"final boss's health: {bosshealth}")
print()
input7=" "
while input7!="a":
    input7=input("press a to continue  ")

print("The monster laughs at its victory, but you know this is far from over. You seize the opportunity to:")
print("a. Attack by throwing a brick at the monster.")
print("b. Prepare to dodge the next attack.")
print("c. Panic and do nothing.")
option = input()

if option == "a":
    print("The demon is distracted, so it doesn't anticipate this attack! However, the effects are only weak.")
    bosshealth -= 3
    print("The boss takes 3 damage.")
    print()
elif option == "b":
    print("The monster quietly laughs to itself until it causes another boulder to accelerate toward you.")
    print("Luckily, you manage to dodge it just in time!")
else:
    print("Unfortunately, your lack of appropriate response causes you to fall victim to the next attack!!")
    print("Luckily, you manage to dodge it just in time!")

def playerturn(backpack):
    global playerhealth, bosshealth
    print()
    list1=["You take a deep breath, trying to steady your racing heart. The air is thick with tension.",
        "The air feels thick with anticipation as you steady yourself for the attack",
        "The world seems to slow down as you prepare your decisive move.",
        "You summon the courage within you, the blade gleaming as you prepare to strike."
    ]
    print(random.choice(list1))


    print("What will you do?")
    print("a. Strike with all your might!")
    print("b. Try to heal your wounds")
    input81 = input()

    if input81 == "a":

        damage = random.randint(20, 30)  
        print()
        print("With a roar, you raise your Golden Sword high and slash downward with all your strength!")
        print(f"The sword glows as it strikes, dealing {damage} damage to final boss. The ground shakes beneath you.")
        print()

        bosshealth -= damage
        print(f"You dealt {damage} damage to the final boss.")
        list2=[ "The demon staggers back, surprised by your strength!",
            "You see the demon’s eyes narrow in fury!",
            "The impact leaves a deep scar across the demon's form.",
            "The demon roars in pain, but it's not enough to stop it!"
            "you think you can defeat me you pathetic little mortal"
        ]
        print(random.choice(list2))
           
    elif input81 == "b":
        if "healing potion" in backpack:
            healamount = random.randint(10, 30)
            playerhealth += healamount
            if playerhealth > 100:  
                playerhealth = 100
            print()    
            print(f"You uncork the healing potion, feeling warmth spread through your body as you restore {healamount} health.")
            backpack.remove("healing potion") 
            print("The potion feels like a surge of life... but how long will it last?")
        else:
            print()
            print("You reach for your healing potion... but it's gone. You’re on your own now.")
    else:
        print("You hesitate, torn between your options. The final boss grows impatient...")

def bossturn():
    global playerhealth, bosshealth
    print()
    print("final boss stands tall, its eyes gleaming with malevolent intent. The room feels colder with every passing second.")

    input82 = random.choice(["attack", "special"])  
    if input82 == "special":
        print()
        print(f"With a terrifying roar, final boss conjures dark energy, its form warping with the power of {special_ability}!")
        damage = random.randint(15, 30) 
        playerhealth -= damage
        print(f"Shadowy tendrils surge toward you, wrapping around you with crushing force! {damage} damage!")
        list3=["The demon’s laugh echoes in your ears as the shadows tighten.",
            "You feel your very soul being crushed by the darkness.",
            "The demon grows stronger with each passing moment!"]
        print(random.choice(list3))

    else:
        damage = random.randint(5, 21) 
        playerhealth -= damage
        print()
        print(f"final boss raises its fist and smashes it down with terrifying force. You feel the impact as {damage} damage shakes your body!")
        list4=["The demon mocks you, grinning as you stagger back.",
            "It seems the demon is enjoying your suffering.",
            "The shadowy figure of the demon looms over you, relentless."]
        print(random.choice(list4))

        
    print(f"final boss attacks, you take {damage} damage.")
    
def isalive(health):
    return health > 0

def gameloop():
    global playerhealth, bosshealth

    while isalive(playerhealth) and isalive(bosshealth):
        print()
        print(f"Your health: {playerhealth}")
        print(f"final boss's health: {bosshealth}")

        if playerhealth < 20 and "healing potion" not in backpack:
            print()
            print("Your vision begins to blur, and every breath feels like a struggle.")
            print("The final boss takes notice, its grin widening as it prepares to finish you off.")
            print("The battle is almost over... You need to win this to get out!")

        playerturn(backpack)

        if not isalive(bosshealth):
            print()
            print(f"With a final, devastating blow, you defeat final boss! Victory is yours!")
            print("You fall to your knees, exhausted. The darkness around you seems to fade, but you're too weary to celebrate.")
            break

        if not isalive(playerhealth):
            print()
            print("You fall to the ground, your body numb with fatigue. The final boss stands victorious over you.")
            print("You feel the cold grip of darkness closing in. It's over.")
            break

        bossturn()

gameloop()

print()
input7=" "
while input7!="a":
    input7=input("press a to continue  ")

print()
print("Suddenly, you hear a loud, guttural growl. The ground shakes violently.")
print("You look up to see the final boss's body rising from the ground, a dark aura surrounding it.")
print("It is not dead... not yet. The monster’s eyes glow with a malevolent light as it laughs maniacally.")
print("'You thought you had defeated me? Foolish mortal. I am eternal! I will crush you!'")

print()
print("The final boss lurches forward, its claws ready to rip you apart.")

print()
print("You're barely hanging on. The monster is relentless, and you can feel your strength fading.")
print("But you know you can't give up. This is the final battle. You must end it.")
print()
print("With a burst of desperation and strength, you throw your sword at the final boss!")

print("The sword flies through the air and lands with a mighty strike")

print()
print("With a final, dramatic roar, the final boss has been pierced through the heart by your sword!")
print("It collapses to the ground, defeated for good.")
print("You’ve won. You’ve survived the maze of secrets.")