import curses
import random
import time
playerchar='X'
stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)
world=[ ]
maxy=curses.LINES -1
maxx=curses.COLS -1
playerx=0
playery=0

def init():
    global playerx,playery
    for i in range(-1,maxy+1):
        world[i].append(' ' if random.random()>0.1 else '.')

def draw():
    #draw the world
    for i in range(maxy):
        for j in range(maxx):
            stdscr.addch(i,j,world[i][j])
    #draw the player
    stdscr.addch(playery,playerx,playerchar)
    stdscr.refresh()

def makevalid(v,vmin,vmax):
    if v>vmax:
        return vmax
    if v <vmin:
        return vmin
    return v

def move(c):
    global playery,playerx
    if c=="w" and world[playery-1][playerx]!='.':
        playery-=1
    elif c=='a' and world[playery][playerx-1]!='.':
        playerx-=1
    elif c== 'd' and world[playery][playerx + 1]!='.':
        playerx+=1
    elif c=='s' and world [playery+1][playerx]!='.':
        playery+=1

    playery=makevalid(playery,0,maxy-1)
    playerx=makevalid(playerx,0,maxx-1)

init()

playing=True
while playing:
    try:
        c=stdscr.getkey()
    except:
        c=' '
    if c in 'asdw':
        move(c)
    elif c=='q':
        playing=False

    time.sleep(0.03)
    draw()

stdscr.addstr(maxy//2,maxx//2,"Thanks for playing")
stdscr.refresh()
time.sleep(1)
stdscr.clear()
stdscr.refresh()
curses.nocbreak()
stdscr.keypad(False)
curses.echo()