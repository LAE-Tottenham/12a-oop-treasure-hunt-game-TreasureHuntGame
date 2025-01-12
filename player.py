import curses

items=['rock','apple']

stdscr=curses.initscr()

class Player():
    def __init__(self, name):
        self.name=name
        self.health=50
        self.rucksack=[]
        self.bagcap=5
    

    def countitems(self):
        num= len(self.rucksack)
        return num
    def attacked(self,damage):
        self.health-=damage
        if self.health<0:
            return True
        else:
            return False

        

        
        
