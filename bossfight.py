input7=" "
while input7!="a":
    input7=input("press a to continue ")
print()    
print("You slowly open your eyes. The world around you is shrouded in darkness. You can barely make out your surroundings.")
print()
print("The cold, damp air clings to your skin ")
print("The walls around you are broken and dilapidated, with large cracks running through them.")
print("Ancient, crumbling statues loom in the corners of the room, their features worn and distorted, it is as though this place holds long-forgotten memories of death and despair")
print()
print("Suddenly, a strange presence fills the air, sending an icy chill down your spine. Something... or someone... is watching you.")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue ")
print()    
print("'you are here at last... Welcome to the Lair of Death.'")
print("'I have been watching you... all this time. You are but a pawn in my game.'")
print("'I am the Demon of Terror, the final boss you could never defeat.'")
print()
print("'I have waited patiently for your arrival. Now, the time has come.'")
print("'No one has ever escaped the Lair of Death... and neither shall you.'")
print("the demon laughs manically")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue ")
print()    
print("you realise this is who you have been hearing the whole time")
print("you have been playing their games....")
print("a sense of unease grows in your stomach...")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue ")
print()    
print("A faint red glow begins to emanate from the shadows. You feel the ground tremble beneath you.")
print("Suddenly, the shadows form a menacing figure: the Demon of Terror, its eyes glowing with malice.")
print("a tall menacing shadow looms over you, its face concealed with a large, dark hood, its bony long fingers point at you mockingly")
print("It steps forward, its voice echoing in your mind, 'Prepare yourself'")
print("You feel your heart racing. There's no turning back.")
print()
input7=" "
while input7!="a":
    input7=input("press a to continue ")


print("The anticipation grows as you ready yourself for the fight. The room is still... for now.")
print("You can feel the Demon of Terror preparing for the final showdown...")

print("A heavy silence fills the room....")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue ")


import random
############################################################################################################################
playerhealth = 100
player_attack_power = 15
bosshealth = 150
boss_attack_power = 20
special_ability = "Shadow Blast"

backpack=["shield","golden sword","healing potion","armor","magical staff"]

print()
print(f"Your health: {playerhealth}")
print(f"FinalBoss's health: {bosshealth}")
print()

print("the evil monster cackles 'youll never get out alive'")
print("before you can react, it extends it long arm infront of it, and effortlessly causes one of the giant boulders to explodes, flinging small bit of rocks flying at you")
print()
print("you dont dodge it in time!")
print("you take 5 damage")
playerhealth -= 5
print()
print(f"Your health: {playerhealth}")
print(f"FinalBoss's health: {bosshealth}")
print()
input7=" "
while input7!="a":
    input7=input("press a to continue ")

print("the monster laughs at its victory, but you know this is far from over, you sieze tis oppurtnity to:")
print("a.attack by throwing a brick towards the monster")    
print("b.prepare to dodge the next attack")
print("panic and do nothing")
option=input()
if option=="a":
    print("the demon is distracted so it doesnt anticipate this attack! however the effects are only weak.")
    bosshealth -= 3
    print("the boss takes 3 damage")
    print()
    print(f"Your health: {playerhealth}")
    print(f"FinalBoss's health: {bosshealth}")
    print()
elif option=="b":
    print("the monster quietly laughs to itself untill it causes another boulder to accelerate towards you")
    print("luckily you manage to dodge it right on time!")
else:
    print("unfortulately your lack of appropriate resonse causes you to fall vinctim to the next attack!!")
    print("luckily you manage to dodge it right on time!")



def playerturn(backpack):
    global playerhealth, bosshealth
    print()
    print("You take a deep breath, trying to steady your racing heart. The air is thick with tension.")
    print("What will you do?")
    print("a. Strike with all your might!")
    print("b. Try to heal your wounds")
    input81 = input()

    if input81 == "a":
        if "golden sword" in backpack:
            damage = random.randint(15, 30)  
            print()
            print("With a roar, you raise your Golden Sword high and slash downward with all your strength!")
            print(f"The sword glows as it strikes, dealing {damage} damage to FinalBoss. The ground shakes beneath you.")
        else:
            damage = random.randint(10, 20)  
            print()
            print("You grit your teeth and swing your weapon with every ounce of your strength.")
            print(f"The strike lands, dealing {damage} damage to FinalBoss.")
        
        bosshealth -= damage
        print(f"You dealt {damage} damage to FinalBoss.")
        
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
        print("You hesitate, torn between your options. The FinalBoss grows impatient...")

def bossturn():
    global playerhealth, bosshealth
    print()
    print("FinalBoss stands tall, its eyes gleaming with malevolent intent. The room feels colder with every passing second.")

    input82 = random.choice(["attack", "special"])  
    if input82 == "special":
        print()
        print(f"With a terrifying roar, FinalBoss conjures dark energy, its form warping with the power of {special_ability}!")
        damage = random.randint(15, 25) 
        playerhealth -= damage
        print(f"Shadowy tendrils surge toward you, wrapping around you with crushing force! {damage} damage!")
    else:
        damage = random.randint(5, 15) 
        playerhealth -= damage
        print()
        print(f"FinalBoss raises its fist and smashes it down with terrifying force. You feel the impact as {damage} damage shakes your body!")
        
    print(f"FinalBoss attacks, you take {damage} damage.")
    
    if playerhealth < 20:
        print()
        print("You stagger back, your vision starting to blur. Your heart pounds in your chest. You can barely stand...")
        print("The FinalBoss senses your weakness and laughs menacingly, its voice echoing through the dark room.")

def isalive(health):
    if health > 0:
        return(True)
    else:
        return(False)


def gameloop():
    global playerhealth, bosshealth
    print("The battle begins, your heart races as the FinalBoss emerges from the shadows, its figure menacing and imposing.")

    while isalive(playerhealth) and isalive(bosshealth):
        print()
        print(f"Your health: {playerhealth}")
        print(f"FinalBoss's health: {bosshealth}")

        if playerhealth < 20 and "healing potion" not in backpack:
            print()
            print("Your vision begins to blur, and every breath feels like a struggle.")
            print("The FinalBoss takes notice, its grin widening as it prepares to finish you off.")

        playerturn(backpack)

        if not isalive(bosshealth):
            print()
            print(f"With a final, devastating blow, you defeat FinalBoss! Victory is yours!")
            print("You fall to your knees, exhausted. The darkness around you seems to fade, but you're too weary to celebrate.")
            break

        bossturn()

        if not isalive(playerhealth):
            print()
            print(" fall to the ground, your body numb with fatigue. FinalBoss stands victorious over you.")
            print("You feel the cold grip of darkness closing in. It's over.")
            break



    if isalive(playerhealth):
        print()
        print("You breathe a sigh of relief, the battle finally over. You slump against the wall, your energy completely drained.")
        print("But wait... you hear something moving in the shadows. The ground trembles beneath your feet.")
        print("A voice echoes through the darkness. \"You may have defeated him... but you have not seen the true horror yet.\"")
        print()
        print("To be continued...")

gameloop()
