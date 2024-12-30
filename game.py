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
    print("dont worry, you can find weapons ti help you defeat the monsters")

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
print()    
print("You step cautiously into the abandoned mine, the air is cold and stale and the ground is covered with jagged rocks ")
print("you spot strange symbols carved into the wall, faint but unmistakably deliberate.")
print("As you explore, your gaze catches something glinting on the ground, shiny object buried in the dirt.-its a golden sword!")
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




#------------------------------------------------------------------------------------------
print("you have entered the haunted house")
print("an eerie voice whispers behind you, filling you with a sense of unease")
print("impressive..... You solved the riddle. But dont think that this is over! Every step you take brings you closer to your doom. I will be waiting in the darkness, watching as you struggle. So enjoy this small triumph, for it will be your last. MWAHAHAHAHAHAHAH")
print()
print("the voice fades...but its message still echoes in your ears.... a cold shiver runns down your spine")
print("The warning only pushes you to move forward. You can’t let fear hold you back.")
print()
print("you decide to look around the house, and a dull fog wraps around its decaying structure, ")
print("The staircase rises steeply, its steps covered in dust, and at the top, a heavy door looms like a barrier between you and the unknown.")
print("you notice that your only path is to go up the stairs...")

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
