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
room8=rooms("mysterious cottage")


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
    print("map")

def talktonpc1():
    print()
    print("welcome to the maze of secrets")
    print("your task is to get through all the rooms and collect the magical stone to escape")
    print("be careful, there are monsters that can kill you, if you die you die in real life "+"\U0001F608")
    print("dont worry, you can find weapons to/ help you defeat the monsters")

def solve_riddle():
    print("You approach the cold, moss-covered wall.")
    print("Etched into the stone is a riddle, faint but legible:")
    print("\"I have keys but open no locks. I have space but no room. You can enter, but you can’t go outside. What am I?\"")
    
    correct_answer=False
    key=False

    while not correct_answer:
        answer = input("enter the answer: ")
        answer=answer.lower()
        if answer == "keyboard":
            print("The wall rumbles and a hidden compartment opens, revealing a rusty key!")
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
print("In the distance, a folded parchment lies on the ground, and a mysterious figure looms in the darkness.")

print()
print("press a to talk to the mysterious figure")
print("press b to pick up the parchment")
input1=" "
while input1!="a" and input1!="b":
    input1=input()

hasmap=False
completed=False


if input1=="a":
    output=talktonpc1()  
    print(output)
    completed=True
else:
    print()
    print("you have found the map")
    print("the map is in your backpack, remember you can only hold 6 items at once")
    backpack.append("map")
    hasmap=True

input2=" "
while input2!="c":
    print()
    print("press a to talk to the mysterious figure")
    print("press b to pick up the parchment ")
    if completed==True:
        print("press c to enter the next room")
    if hasmap==True:
        print("press m to open map")    
    input2=input()    

    if input2=="a":
        output=talktonpc1()  
        print(output)
        completed=True
    elif input2=="b":
        print()
        print("you have found the map")
        print("the map is in your backpack, remember you can only hold 6 items at once")
        backpack.append("map")
        hasmap=True
    elif input2=="m" and hasmap==True:
        print(openmap())
    elif input2=="c":
        room2.enterroom()        

#-------------------------------------------------------------------------------------------
#####################################   room 2   ##############################################

print()    
print("You step cautiously into the abandoned mine, the air is cold and stale and the ground is covered with jagged rocks ")
print("you spot strange symbols carved into the wall, faint but unmistakably deliberate.")
print("As you explore, your gaze catches something glinting on the ground,a shiny object buried in the dirt.-its a golden sword!")
x=" "
while x!="a":
    x=input("press a to pick up the sword")
print("you have picked up the sword")
backpack.append("sword")
print()

key=False
input3=" "
while input3!="b":
    print("press a to examine the writing")
    print("press b to enter the next room")
    print("press m to open map")
    input3=input()
    if input3=="a":
        output=solve_riddle()
        key=True
        print(output)
    elif input3=="b" and key==True:
        print("you can now enter the next room")   
    elif input3=="b" and key==False:
        print("you need a key to open the door")
        print()
        input3=" "     
    else:
        input3=" "




#------------------------------------------------------------------------------------------------------
####################################    room 3   ###############################################

print("you have entered the haunted house")
print("an eerie voice whispers behind you, filling you with a sense of unease")
print("impressive..... You solved the riddle. But dont think that this is over! Every step you take brings you closer to your doom. I will be waiting in the darkness, watching as you struggle. So enjoy this small triumph, for it will be your last. MWAHAHAHAHAHAHAH")
print()
print("the voice fades...but its message still echoes in your ears.... a cold shiver runs down your spine")
print("The warning only pushes you to move forward. You can’t let fear hold you back.")
print()
input31=" "
while input32 !="a":
    input32=input("press a to continue")
print("you decide to look around the house, and a dull fog wraps around its decaying structure, ")
print("The staircase rises steeply, its steps covered in dust, and at the top, a heavy door looms like a barrier between you and the unknown.")
print("you notice that your only path is to go up the stairs...")
input32=" "
while input32 !="a":
    input32=input("enter a to ascend the stairs")

def room3_monster():
    print("A terrifying creature emerges from the shadows! Its massive form towers over you, with glowing red eyes and sharp claws gleaming in the dim light.")
    print("You have the option to:")
    print("a. Distract the monster.")
    print("b. Kill it with the golden sword.")
    print("c. Run away while you still can.")
    
    combat_choice=input()

    if combat_choice == "a":
        print("You attempt to distract the monster with a loud noise. But it turns toward you and pounces")
        print("You have died.")
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

output=room3_monster()
print(output)

print("you can now enter the secret library")

#------------------------------------------------------------------------------------------------------
###################################   room 4    ##############################################################

input4=" "
doorunlocked=False
while input4 !="c" and input4 != "d":
    print("press a to inspect the bookshelves.")
    print("press b to ask the old man for more information.")
    if doorunlocked==True:
        print("press c to enter the twisted forest")
        print("press d to enter the abandoned castle")
    print("press m to look at map")
    input4=" "
    input4=input()
    if input4 == "a":
        print("You walk towards the bookshelves and begin scanning the spines of the many books")
        print("You search the shelves and spot a small vial tucked behind an old book. It's a glowing green potion, labeled 'Essence of strength'.")
        input41=" "
        while input41 !="a":
            input41=input("press a to pick up the potion")
        print("You now have the Essence of strength potion!")
    
    elif input4 == "b":
        print("'To proceed, you must solve my riddle,' the old man says, his lips curling into a cryptic smile.")

        print()
        print("The old man asks in a low, mysterious tone: 'The more of me there is, the less you see. What am I?'")
        correctanswer=False
        while correctanswer==False
            player_answer = input("enter your answer: ").lower()
            if player_answer == "hint":
               print("The old man’s eyes glimmer as if amused by your request. 'Very well... Here is your hint.'")
               print("Hint: I am something that grows as the light fades.")
            elif player_answer == "darkness":
                print("He nods slowly, his voice echoing, 'You have answered correctly.'")
                correctanswer=True
            else:
                print("incorrect,  Think carefully.'")
    
        print("With the riddle solved, you approach the old man.")
        print("'Now,' he whispers, his voice barely audible, 'Look at the bookshelf ahead. Four books glow with an eerie light. Choose wisely.'")
        print("He gestures towards a shelf that holds four glowing books. The titles read:")
        print("a. 'The Realm of Darkness'")
        print("b. 'The Lost Echoes'")
        print("c. 'The Forbidden spellbook'")
        print("d. 'tales of an evil wizard'")  
    
        input42=" "
        while input42 != "a":
            input42=input("choose the correct book")
            if input42 ="b":
                print("you inspect the book but dont find anything useful...try again")
            elif input42 ="c":
                print("incorrect.try again")
            elif input42 ="a":
                print("'The key to the door is not where the light shines brightest, but where the shadows hide secrets.'")
                print("you walk towards the darkest corner of the library, you find a lever and pull it")
                print("suddenly you hear the sound of doors open. you realsie that you have two choices:The twisted forest or the abandoned castle")
                doorunlocked=True
            else:
                print("try again")
    elif input4 == "c":
        nextroom="twisted forest"
    elif input4 == "d":
    nextroom="abandoned castle"
    elif input4 == "m" and hasmap==True:
        print(openmap())
    else:
        print("try again")   