import curses

from item import Food,Weapon,Item
import random
import place
from player import Player
import time
from item import NPC
stdscr=curses.initscr()
curses.start_color()
curses.beep()
monsterdef=False
apple=Food('apple',20,28,3,'🍎','world')
apple2=Food('apple',20,13,6,'🍎','world')
chest=Item("Chest",19,7,False,'▩','world')
House1=Item('House1',17,5,False,'⌂','world')
House2=Item('House2',9,7,False,'⌂','world')
Key1=Item('silver key',chest.xpos,chest.ypos,True,'🗝','world')
Key2=Item('copper key',17,5,True,'⚷','world')
key1disc=False
key2disc=False
wizard=NPC('mage',11,8,'𐀪')
sword=Weapon('Enchanted Sword',House1.xpos,House1.ypos,'⚚',30,'world')
skull1=Item('skull',3,3,False,'☠','world')



class Monster():
    def __init__ (self,name,char,world,attackstat,x,y,hp):
        self.name=name
        self.char=char
        self.world=world
        self.attackstat=attackstat
        self.x=x
        self.y=y
        self.hp=hp




enchanted=False
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

world=[]
world2=[]
world3=[]
stage=0

maxy=10
maxx=30
playerx=0
playery=0
enemychar='ꆜ'
randmonster=Monster('Teus','〠',world3,True,15,3,100)  
monsterhp=randmonster.hp 
monsterx=randmonster.x
monstery=randmonster.y
monsterchar=randmonster.char
treasurex=15
treasurey=2
treasurechar='⧆'
playerchar='𖠋'



def randomgen(worldnum):
    x=random.randint(2,maxx-1)
    y=random.randint(2,maxy-1)


    
    return x,y



def checkenemy():
    global playing,ex,ey,playerx,playery
    if playerx==ex and playery==ey:
        stdscr.clear()
        stdscr.addstr(maxy//2,0,"YOU DIED...")
        stdscr.refresh()
        stdscr.clear()
        if 'magical sword' not in rucksack:
            stdscr.addstr(5,0,"You weren't prepared enough...")
            stdscr.refresh()
        time.sleep(3)
        stdscr.clear()
        playing=False
    else:
        if 'magical sword' in rucksack:
            diff=0.9
        else :
            diff=0.9

        stdscr.nodelay(False) 
        if ex>playerx and random.random()> diff:
            ex-=1
        elif ex<playerx and random.random()> diff:
            ex+=1
        elif ey>playery and random.random() > diff :
            ey-=1
        elif ey<playery and random.random() > diff:
            ey+=1

        
        ex=makevalid(ex,0,maxx)
        ey=makevalid(ey,0,maxy)



def makevalid(v,min,max):
    if v>max:
        return max
    elif v< min:
        return min
    else:
        return v


def move(c,worldnum):
        global playerx,playery
        if c == "a" :
                playerx -= 1
        elif c =="w" :
                playery -= 1
        elif c == "s" :
                playery +=1
        elif c == "d" :
                playerx+=1

        if worldnum=='world2':
            playerx=makevalid(playerx,0,maxx-1)
            playery=makevalid(playery,0,maxy-1)
        elif worldnum==world:
            playerx=makevalid(playerx,0,maxx-1)
            playery=makevalid(playery,1,maxy-1)
        elif worldnum=='world3':
            playerx=makevalid(playerx,0,maxx-1)
            playery=makevalid(playery,1,maxy-2)
            
        

def moveinforest(c):
        global playerx,playery
        if c == "a":
            playerx -= 1
        elif c =="w":
            playery -= 1
        elif c == "s":
            playery +=1
        elif c == "d":
            playerx+=1
        playerx=makevalid(playerx,0,maxx-1)
        playery=makevalid(playery,0,maxy-1)
appleeaten=False
applex=apple.xpos
appley=apple.ypos
applechar=apple.character
def init():
    global playerx,playery,applex,appley,applechar,apple2,appleeaten,chestchar,chesty,chestx,key1x,key2x,key1y,key2y,wizardx,wizardy,house1x,house2x,house1y,house2y,house2char,house1char,key1char,key2char,wizardy,wizardx,wizardchar,swordx,swordy,swordchar,skullx,skully,skullchar,ex,ey
    for i in range(maxy):
        world.append([])            
        for j in range(maxx):
                world[i].append('.')
    playerx=15
    playery=9       
    applex=apple.xpos
    appley=apple.ypos
    applechar=apple.character
    chestchar=chest.character
    chesty=chest.ypos
    chestx=chest.xpos
    house1x=House1.xpos
    house1y=House1.ypos
    house1char=House1.character
    house2x=House2.xpos
    house2y=House2.ypos
    house2char=House2.character
    key1x=Key1.xpos
    key1y=Key1.ypos
    key1char=Key1.character
    key2x=Key2.xpos
    key2y=Key2.ypos
    key2char=Key2.character
    wizardx=wizard.xpos
    wizardy=wizard.ypos
    wizardchar=wizard.character
    swordx=sword.xpos
    swordy=sword.ypos
    swordchar=sword.character
    skullx=skull1.xpos
    skully=skull1.ypos
    skullchar=skull1.character


def introwoods():
    count=0
    if playerx==15 and playery==8 and stage!=3 and count>1:
        introstring='Sickly trees are all over this forest, their branches smothered in white leaves...'
        charslow2(introstring)
        clearline()
        introstring2="Something weird is in the middle... It doesn't look like a force to be reckoned with..."
        charslow2(introstring2)
        time.sleep(2)
        clearline()
        ostring='OBJECTIVE: Find the end of the woods'
        charslow2(ostring)
        count+=1

def monstertime():
    global health,playing,monstery,monsterx,monsterdef,treasurex,treasurey,treasurechar
    global monsterhp
    count=0
    if playerx== monsterx and playery== monstery+1:
            while count<1:
                monstring="A dark and foreboding grin lies on the creature's face..."
                charslow2(monstring)
                monstring2="Yet you don't feel afraid at all...                       "
                charslow2(monstring2)
                monstring3="You stand upright sword in hand, and prepare yourself for battle..."
                charslow2(monstring3)
                clearline()
                count+=1
                curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLUE)
                stdscr.addstr(12,10,f"Opponent HP:{monsterhp}",curses.color_pair(1))
                monstring4="Click f to FIGHT!"
                charslow2(monstring4)
                time.sleep(2)
                clearline()
                count+=1
            
    while monsterhp>0:
        fight=stdscr.getkey()
        if fight=='f' and health>50:
            monsterhp-=20
            stdscr.addstr(12,10,f"Opponent HP:{monsterhp}",curses.color_pair(1))
            stdscr.refresh()
        elif fight=='f' and health <= 50 and health >30 and 'apple' in rucksack:
            curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
            stdscr.addstr(12,0,f'HP:{health}',curses.color_pair(2))
            fightstring="Your body isn't able to fight.. your health is too low..."
            charslow2(fightstring)
            fightstring2='There is an apple in your rucksack. Eat it? Y/N           '
            charslow2(fightstring2)
            time.sleep(2)
            eat=stdscr.getkey()
            if eat=='Y':
                health+=20
                curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_GREEN)
                stdscr.addstr(12,0,f'HP:{health}',curses.color_pair(3))
                fightstringw='You have eaten the apple and regained your health!'
                charslow2(fightstringw)
                fightstringw1='Now.. Press f to FIGHT!'
                charslow(fightstringw1)

        elif fight=='f' and health<=50 and health>30 :
            curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
            stdscr.addstr(12,0,f'HP:{health}',curses.color_pair(2))
            fightstring3='Your health is too low for battle... You should have never tried to find this place...'
            charslow2(fightstring3)
            fightstring4='You utter your last words as you are struck by this surge of magic...                    '
            charslow2(fightstring4)
            fightstring5='You remember the words of the wizard amidst your last breaths            '
            charslow2(fightstring5)
            clearline()
            fightstring6='You died.... :('
            charslow2(fightstring6)
            time.sleep(2)
            stdscr.clear()
            stdscr.refresh()
            playing=False
        
    if monsterhp==0:
        monsterdef=True
        stdscr.addstr(monstery,monsterx,'##')
        fightstringa='You have slain the monster! His remains lie on the ground, the magical powers still emanating...'
        charslow2(fightstringa)
        fightstringb="But that's besides the point! The treasure is right there! Go and pick it up !"
        charslow2(fightstringb)
        if world3[playery][playerx]== treasurechar:
            fightstringc='What are you waiting for ?! Interact to Open it !'
            charslow(fightstringc)
            inter=stdscr.getkey()
            if inter== 'i':
                pass
                   
                    


def interactworld3():
    global treasurex,treasurey
    if playery==treasurey and playerx==treasurex :
        fightstringh='You have found artefacts that look thousands of years old... Gold and valuables overflow'
        charslow2(fightstringh)
        stdscr.addch(treasurex-1,treasurey,'👑')
        stdscr.refresh()
        stdscr.addch(treasurex+1,treasurey,'🪙')
        stdscr.refresh()
        stdscr.addch(treasurex,treasurey+1,'🧭')
        stdscr.refresh()
    else:
        fightstringh1='Nothing to see here'
        charslow2(fightstringh1)
    pass





def initinforest():
    global playerx,playery,ex,ey
    for i in range(maxy):
        world2.append([])
        for j in range(maxx):
            world2[i].append('♧' if random.random()>0.8 else ' ')
    playerx=15
    playery=9
    ex=15
    ey=4
    
def inittreasure():
    global monstery,monsterx,monsterchar,treasurex,treasurey,treasurechar,playerx,playery,randmonster,monsterhp
    for i in range(maxy):
        world3.append([])
        for j in range(maxx+1):
            world3[i].append('.')
    

    randmonster=Monster('o','〠',world3,True,15,3,100)        
    monsterx=randmonster.x
    monstery=randmonster.y
    monsterhp=randmonster.hp
    monsterchar=randmonster.char
    treasurex=15
    treasurey=2
    treasurechar='⧆'
    playerx=14
    playery=8

def drawtreasure():
    for i in range(0,maxy):
        for j in range(maxx):
            stdscr.addch(i,j,world3[i][j])
    stdscr.refresh()

    for j in range(0,6):
        stdscr.addch(9,j,'🌳')
    for j in range(11,18):
        stdscr.addch(9,j,'🌳')
    for j in range(0,monsterx-1):
        stdscr.addch(monstery,j,'🔥')
    for j in range(monsterx+1,17):
        stdscr.addch(monstery,j,'🔥')
    stdscr.refresh()
    if monsterhp>0:
        stdscr.addch(monstery,monsterx,monsterchar)
    else:
        stdscr.addstr(monstery,monsterx,'##')
    stdscr.refresh()
    stdscr.addch(treasurey,treasurex,treasurechar)
    stdscr.refresh()
    stdscr.addch(playery,playerx,playerchar)
    stdscr.addstr(9,14,'𖦹')
    stdscr.refresh()

def checkintreasure():
    global playing,monsterchar,monsterx,monstery
    if playery==3 and playerx!=15 or playery==monstery and playerx==monsterx and monsterdef==False:
        stdscr.addstr(maxy//2,maxx//2,'YOU DIED...')
        stdscr.refresh()
        stdscr.clear()
        time.sleep(3)
        playing=False
    

def draw():
    global applex,appley, applechar,playery,playerx,playerchar
    for i in range(1,maxy):
        for j in range(maxx):
            stdscr.addch(i,j,'.')
    stdscr.refresh()              
    for i in range(15):
        stdscr.addch(0,i,'🌳')
    for i in range(15):
            stdscr.addch(1,i,'.')
    for i in range(1,maxy):
        stdscr.addch(i,15,'⚀')
    
    stdscr.addch(playery,playerx,playerchar)            
    stdscr.refresh()            
    stdscr.addch(7,0,'🐈')
    stdscr.refresh()             
    stdscr.addch(8,13,'🔮')
    stdscr.addstr(appley,applex,applechar)
    stdscr.refresh()
    stdscr.addch(key1y,key1x,key1char)
    stdscr.addch(key2y,key2x,key2char)
    stdscr.addch(house1y,house1x,house1char)
    stdscr.addch(house2y,house2x,house2char)
    stdscr.addch(chesty,chestx,chestchar)
    stdscr.addch(wizardy,wizardx,wizardchar)
    stdscr.addch(skully,skullx,skullchar)
    stdscr.addch(1,15,'𖦹')
    stdscr.refresh()
    if key1disc==True:
        stdscr.addstr(chesty,chestx,key1char)
        stdscr.refresh()
        stdscr.adstr(chestx,chesty,'..')
    if key2disc==True:
        stdscr.addstr(key2y,key2x,key2char)
    if appleeaten==True:
        applechar='..'
        stdscr.addstr(appley,applex,applechar)
        stdscr.refresh()
        stdscr.refresh()

def drawoods():
    global playerx,playery
    for i in range(maxy):
        for j in range(maxx):
                stdscr.addch(i,j,world2[i][j])
    stdscr.refresh()
    playerx=makevalid(playerx,0,maxx-1)
    playery=makevalid(playery,0,maxy-1)
    stdscr.addch(playery,playerx,playerchar)  
    stdscr.refresh()   
    stdscr.addch(ey,ex,enemychar)       
    stdscr.refresh()
    stdscr.addch(0,15,'𖦹')
    stdscr.addch(9,15,'𖦹')

               
    



#mainc='sirine'
#m=Player(mainc,100,15,9,[])
#playerx=m.x
#playery=m.y
def charslow(string):
        for char in string:
            curses.delay_output(60)
            stdscr.addstr(char)
            stdscr.refresh()
def charslow2(string):
        x=-1
        for char in string:
            x+=1
            curses.delay_output(20)
            stdscr.addstr(11,x,char)
            stdscr.refresh()


playing=True
cba=False
while cba:
    curses.echo()
    stdscr.clear()
    the_string = """Welcome to Sirine's treasure hunt game! Let's start by setting the scene! 
    You are from an ancient lineage of treasure hunters,and have come across
    the foreign lands of Telarium.
    An ancient treasure is hidden here, waiting for you to discover it...
    What is your name?"""
    charslow(the_string)
    playername=stdscr.getstr()
    main=Player(playername)
    second_string=f"""Greetings {playername}! What would you like to be presented as? 
    1)𖠋   2)☺ Choice 1 will be selected as default"""
    charslow(second_string)
    characternum=stdscr.getkey()
    if characternum=='2':
        playerchar='☺'
    else:
        playerchar='𖠋' 
    time.sleep(3)
    stdscr.clear()
    third_string=f"{playerchar} has been selected! Great choice. Now let the hunt begin!"
    charslow(third_string)
    time.sleep(3)

    stdscr.clear()
    curses.noecho()
    fourth_string="""Here is a simple guide to the controls.This will stay displayed on
    your screen!
    w=move upwards
    a=move to the left
    s=move downwards
    d=move to the right
    i=interact
    And finally, click q to quit the game!
    """
    charslow(fourth_string)
    time.sleep(5)
    stdscr.clear()
    cba=False

main=Player('player')
rucksack=main.rucksack
health=main.health

bagcap=main.bagcap
def clearline():
    stdscr.addstr(11,0,'                                                                                                                       ')

bagcap=5
def additem(item):
    global items,rucksack,bagcap
    stdscr.addstr(11,0,'Would you like to add this'+' '+item+' '+ 'to your rucksack?Y/N :')
    reply=stdscr.getkey()
    stdscr.refresh()
    if reply=='Y':
        if len(rucksack) == bagcap:
            stdscr.addstr(11,0,"Your rucksack is full. Would you like to remove something?")
            stdscr.refresh()
            p=stdscr.getkey()
            stdscr.refresh()
            if p in rucksack:
                (main.rucksack).remove(p)
                stdscr.addstr(11,0,'Item has been removed!')
                stdscr.refresh()
            else:
                stdscr.addstr(11,0,"That item isn't in your rucksack")
                stdscr.refresh()
        else:
            rucksack.append(item)
            stdscr.addstr(11,0,item+ "is now in your rucksack!")
            stdscr.refresh()
    else:   
        clearline()
        
    return reply


def interactworld2():
    global stage,playing,enchanted
    if playerx==15 and playery==0:
        foreststring='You have reached the end of the whistling woods. Do you wish to move forward?Y/N '
        charslow2(foreststring)
        forest=stdscr.getkey()
        if forest == 'Y':
            stage=3
            inittreasure()

            
    
        





times=0
h1open=0
h2opent=0


def interactworld():
    global appley,applex,appleeaten,key1disc,key2disc,key1x,key1char,key1y,key2x,key2y,key2char,house1y,house1x,house2y,house2x,chesty,chestx,rucksack,times,h1open,h2opent,enchanted,skully,skullx,skullchar,eat,health
    if playery==appley and playerx==applex:
        eat=' '
        reply2=additem('apple')
        stdscr.refresh()
        if reply2=='Y':
            appleeaten=True
            stdscr.addstr(appley,applex,applechar)
            stdscr.refresh()
            stdscr.refresh()

        if health < 80 :
            stdscr.addstr(11,0,f'Would you like to eat this apple? It will give you {apple.hp} health.Y/N :')
            eat=stdscr.getkey()
            stdscr.refresh()

            if eat=='Y':
                clearline()
                health+= apple.hp
                stdscr.addstr(11,0,'You have eaten an apple!                                                   ')
                stdscr.addstr(12,0,'              ')
                stdscr.refresh()
                stdscr.addstr(12,0,f'HP:{health}')
                stdscr.refresh()
                appleeaten=True
                stdscr.addstr(appley,applex,applechar)
                stdscr.refresh()
                
            else:
                clearline()
        if reply2=='Y' and eat=='Y':
                rucksack.remove('apple')
        elif health>80:
            stdscr.addstr(11,0,'Would you like to eat this apple? It will restore your hp to full health.')
            eat=stdscr.getkey()
            stdscr.refresh()
            time.sleep(2)
            if eat=='Y':
                clearline()
                health=100
                stdscr.addstr(11,0,'You have eaten an apple!                                                   ')
                stdscr.addstr(12,0,'              ')
                stdscr.refresh()
                stdscr.addstr(12,0,f'HP:{health}')
                stdscr.refresh()
                appleeaten=True
                stdscr.addstr(appley,applex,applechar)
                stdscr.refresh()
                if reply2=='yes' and eat=='Y':
                    main.rucksack.remove('apple')
        else:
            clearline()
    if playery==chesty and playerx==chestx :
        stdscr.addstr(11,0,"This seems to be a box with no lock. Press i again to see what's inside")
        stdscr.refresh()
        chestopen=stdscr.getkey()
        time.sleep(1)
        clearline()
        
        if chestopen=='i' and times<1:
            key1disc==True
            stdscr.addstr(chesty,chestx,key1char)
            stdscr.addstr(11,0,'You have found a silver key! This item has been added to your rucksack!')
            stdscr.refresh()
            stdscr.addstr(chesty,chestx,'...')
            rucksack.append('silver key')
            time.sleep(2)
            clearline()
            times+=1
        elif chestopen=='i' and times >= 1:
            stdscr.addstr(11,0,"You've already opened this box. It is empty now!")
            
    
    if playerx==house1x and playery==house1y:
        stdscr.addstr(11,0,'This is a small shed locked with a large silver lock. Would you like to open the door?Y/N:')
        openh1=stdscr.getkey()
        if openh1=='Y':
            if 'silver key' in rucksack and h1open<1:
                stdscr.addstr(11,0,'Your silver key is a match for this lock!                                                          ')
                rucksack.remove('silver key')
                stdscr.refresh()
                time.sleep(3)
                stdscr.addstr(11,0,'You unlock the door which reveals a dark empty room...')
                stdscr.refresh()
                time.sleep(3)
                stdscr.addstr(11,0,'In the middle, there seems to be a key.                  ')
                stdscr.addstr(house1y,house1x,key2char)
                stdscr.refresh()
                time.sleep(3)
                stdscr.addstr(11,0,'Copper key added to rucksack!             ')
                rucksack.append('Copper key')
                h1open+= 1

            elif h1open>=1:
                stdscr.addstr(11,0,'This is a small shed with its door opened. It is empty and dark inside.')
            else:
                stdscr.addstr(11,0,"Sorry, you don't have the key to unlock the door...                                     ")
        else:
            clearline()
    
    if playerx==house2x and playery==house2y:
        stdscr.addstr(11,0,'This is another shed, but this time it has a large copper lock on the door. Want to try and open the door?Y/N ')
        h2open=stdscr.getkey()
        curses.echo()
        if h2open=='Y':
            if 'Copper key' in rucksack and h2opent<1:
                stdscr.addstr(11,0,'You turn the lock with your copper key and...                                                                       ')
                stdscr.refresh()
                time.sleep(2)
                stdscr.addstr(11,0,"The door unlocks, revealing yet another empty shed.")
                stdscr.refresh()
                time.sleep(2)
                stdscr.addstr(11,0,'But there seems to be something glinting in the darkness....')
                stdscr.refresh()
                time.sleep(2)
                stdscr.addstr(11,0,"You step forward, and.. it's a sword!                           ")
                stdscr.refresh()
                time.sleep(2)
                stdscr.addstr(11,0,"It has an unusual glint and feels almost magical...       ")
                stdscr.refresh()
                time.sleep(2)
                stdscr.addstr(11,0,"Could this be what the old wizard was talking about...?")
                stdscr.refresh()
                time.sleep(2)
                stdscr.addstr(11,0,"Enchanted Sword added to Rucksack!                           ")
                stdscr.refresh()
                rucksack.append('Enchanted Sword')
                rucksack.remove('Copper key')
                h2opent+=1
            elif h2opent>=1:
                stdscr.addch(11,0,'This is an unlocked shed revealing nothing inside')
        else:
            stdscr.addch(11,0,'                                                                                                                  ')
    if playerx==15 and playery==2:
        stdscr.addch(11,0,'Do you wish to enter the whistling woods?Y/N                     ')
        woods=stdscr.getkey()
        if woods=="Y":
            stdscr.clear()
            enchanted==True
    if playerx==skullx and playery==skully:
        stdscr.addstr(11,0,'An eerie pile of bones lie on the ground...')
    if playerx==15 and playery==1:
        ranstring='An eerie sound comes from within the forest...'
        charslow2(ranstring)
        ranstring2='But this is what you must face to find the treasure right?'
        charslow2(ranstring2)
    
        clearline()
        ranstring3='Do you wish to enter the whistling woods? Y/N : '
        charslow2(ranstring3)
        h=stdscr.getkey()
        if h=='Y':
            enchanted=True
            stdscr.refresh()
            stdscr.clear()
            stdscr.refresh()
            initinforest()
            

            


    



def printrucksack():
        rucksackx=0
        rucksacky=11
        clearline()
        stdscr.addstr(rucksacky,rucksackx,'Your rucksack contains:'+str(rucksack))
        stdscr.refresh()
        time.sleep(2)
        
def poo():
    global playing,count
    try:
        c=stdscr.getkey()
    except:
        c=' '
    if c =='i':
        interactworld3()
    elif c in 'asdw':
        stdscr.addstr(playery,playerx,playerchar)
        time.sleep(1)         
    elif c=='i':
        interactworld3()
    elif c == 'q':
        playing=False
    drawtreasure()
    checkintreasure()
    monstertime()
    stdscr.refresh()
enchanted=True
stage=3
playing=True
if enchanted==False:
    init()
elif enchanted== True and stage!=3:
    stdscr.clear()
    con='on'
    initinforest()
    playing=True
elif stage==3:
    stdscr.clear()
    con='on'
    playing=False
    inittreasure()
    playing=True

while playing:
    try:
        c=stdscr.getkey()
    except:
        c=' '
    
    if enchanted==False and stage!=3:
        if c in 'asdw':
            move(c,world)
        elif c== 'q':
            playing=False
        elif c =='i':
            interactworld()
        elif c=='p':
            printrucksack()
        draw()
                
    if enchanted==True and stage != 3:
        
        if c in 'asdw':
            clearline()
            move(c,world2)
        elif c== 'q':
            playing=False
        elif c=='i':
            interactworld2()
        elif c=='p':
            printrucksack()
        drawoods()
        introwoods()
        checkenemy()

    while stage==3 and enchanted==True:
        inittreasure()
        count=0
        if c =='i':
            interactworld3()
        elif c in 'asdw':
            stdscr.addstr(playery,playerx,playerchar)
            time.sleep(1)         
        elif c=='i':
            interactworld3()
        elif c == 'q':
            playing=False
        drawtreasure()
        checkintreasure()
        monstertime()
        stdscr.refresh()
        
            
           
        
        
if playing==False and con !='on':
    stdscr.clear()
    stdscr.addstr(5,15,'Thanks for playing!')
    time.sleep(2)
    stdscr.clear()
if playing==False and con=='on':
    pass
stdscr.getkey()
curses.nocbreak()
stdscr.keypad(False)
stdscr.clear()
curses.echo()

