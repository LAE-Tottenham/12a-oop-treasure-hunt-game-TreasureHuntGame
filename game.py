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
styled_text=pyfiglet.figlet_format('welcome to the treasure hunt game',font='doom')
print(styled_text)

s=" "
while s!="s":
    s=input("enter s to start ")

print("You wake up in a dark and ominous cave.Through the shadows you can make out the ouline of a folded parchment on the ground and mysterious figure standing in the distance")

    

