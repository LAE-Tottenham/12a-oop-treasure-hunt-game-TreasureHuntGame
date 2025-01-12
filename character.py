class Character:
    def __init__(self,name, description, health,  char_type, dialogue):
        self.name = name
        self.description = description
        self.health = health
        self.type = char_type
        self.dialogue = dialogue
        self.defeated = False
    
    
    def interact(self):
        if self.role == 'hero':
            return f"You meet the hero {self.name}. {self.description}"
        elif self.role == 'villain':
            return f"You encounter the villain {self.name}. {self.description}"
        
    def fight(self,villain_name):
        villain_found = None
        for villain in self.current_place.villains:
            if villain.name.lower()==villain_name.lower():
                villain_found = villain
                break
            if villain_found:
                print(f"You are fighting {villain_found.name}")
            else:
                print(f"No villain named {villain_name}")

    def defeat(self):
        self.defeated = True
                
      