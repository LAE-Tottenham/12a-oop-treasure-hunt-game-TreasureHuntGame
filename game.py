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
    print("")
    print("welcome to the maze of secrets")
    print("your task is to get through all the rooms and collect the magical stone to escape")
    print("be careful, there are monsters that can kill you, if you die you die in real life "+"\U0001F608")
    print("dont worry, you can find weapons ti help you defeat the monsters")

#-------------------------------------------------------------------------------
styled_text=pyfiglet.figlet_format('MAZE OF SECRETS',font='doom')
print(styled_text)

backpack=[]

s=" "
while s!="s":
    s=input("enter s to start ")

print("You wake up in a dark and ominous cave.")
print("Through the shadows you can make out the ouline of a folded parchment on the ground and mysterious figure standing in the distance")

print(" ")
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
    print(" ")
    print("you have found the map")
    print("the map is in your backpack, remember you can only hold 6 items at once")
    backpack.append("map")
    hasmap=True

input2=" "
while input2!="c":
    print(" ")
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
        print(" ")
        print("you have found the map")
        print("the map is in your backpack, remember you can only hold 6 items at once")
        backpack.append("map")
        hasmap=True
    elif input2=="m" and hasmap==True:
        print(openmap())
    elif input2=="c":
        room2.enterroom()        


    

