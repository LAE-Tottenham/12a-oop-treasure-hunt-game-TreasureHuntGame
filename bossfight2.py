import random

input7=" "
while input7!="a":
    input7=input("press a to continue ")
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
    input7=input("press a to continue ")
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
    input7=input("press a to continue ")
print()    
print("You realize this is who you have been hearing the whole time.")
print("You have been playing their games....")
print("A sense of unease grows in your stomach...")
print()

input7=" "
while input7!="a":
    input7=input("press a to continue ")
print()    
print("A faint red glow begins to emanate from the shadows. You feel the ground tremble beneath you.")
print("Suddenly, the shadows form a menacing figure: the Demon of Terror, its eyes glowing with malice.")
print("A tall menacing shadow looms over you, its face concealed with a large, dark hood, its bony long fingers point at you mockingly.")
print("It steps forward, its voice echoing in your mind, 'Prepare yourself.'")
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

############################################################################################################################
playerhealth = 100
player_attack_power = 15
bosshealth = 150
boss_attack_power = 20
special_ability = "Shadow Blast"

backpack = ["shield", "golden sword", "healing potion", "armor", "magical staff"]

print()
print(f"Your health: {playerhealth}")
print(f"FinalBoss's health: {bosshealth}")
print()

while input7!="a":
    input7=input("press a to continue ")

print("The evil monster cackles, 'You'll never get out alive!'")
print("Before you can react, it extends its long arm in front of it, and effortlessly causes a giant boulder to explode, sending small bits of rocks flying at you.")
print()
print("You don't dodge it in time!")
print("You take 5 damage")
playerhealth -= 5
print()
print(f"Your health: {playerhealth}")
print(f"FinalBoss's health: {bosshealth}")
print()
input7=" "
while input7!="a":
    input7=input("press a to continue ")

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
        print(f"The sword glows as it strikes, dealing {damage} damage to FinalBoss. The ground shakes beneath you.")
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
        print("You hesitate, torn between your options. The FinalBoss grows impatient...")

def bossturn():
    global playerhealth, bosshealth
    print()
    print("FinalBoss stands tall, its eyes gleaming with malevolent intent. The room feels colder with every passing second.")

    input82 = random.choice(["attack", "special"])  
    if input82 == "special":
        print()
        print(f"With a terrifying roar, FinalBoss conjures dark energy, its form warping with the power of {special_ability}!")
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
        print(f"FinalBoss raises its fist and smashes it down with terrifying force. You feel the impact as {damage} damage shakes your body!")
        list4=["The demon mocks you, grinning as you stagger back.",
            "It seems the demon is enjoying your suffering.",
            "The shadowy figure of the demon looms over you, relentless."]
        print(random.choice(list4))

        
    print(f"FinalBoss attacks, you take {damage} damage.")
    
def isalive(health):
    return health > 0

def gameloop():
    global playerhealth, bosshealth

    while isalive(playerhealth) and isalive(bosshealth):
        print()
        print(f"Your health: {playerhealth}")
        print(f"FinalBoss's health: {bosshealth}")

        if playerhealth < 20 and "healing potion" not in backpack:
            print()
            print("Your vision begins to blur, and every breath feels like a struggle.")
            print("The FinalBoss takes notice, its grin widening as it prepares to finish you off.")
            print("The battle is almost over... You need to win this to get out!")

        playerturn(backpack)

        if not isalive(bosshealth):
            print()
            print(f"With a final, devastating blow, you defeat FinalBoss! Victory is yours!")
            print("You fall to your knees, exhausted. The darkness around you seems to fade, but you're too weary to celebrate.")
            break

        if not isalive(playerhealth):
            print()
            print("You fall to the ground, your body numb with fatigue. The FinalBoss stands victorious over you.")
            print("You feel the cold grip of darkness closing in. It's over.")
            break

        bossturn()

gameloop()

print()
input7=" "
while input7!="a":
    input7=input("press a to continue ")

print()
print("Suddenly, you hear a loud, guttural growl. The ground shakes violently.")
print("You look up to see the FinalBoss's body rising from the ground, a dark aura surrounding it.")
print("It is not dead... not yet. The monster’s eyes glow with a malevolent light as it laughs maniacally.")
print("'You thought you had defeated me? Foolish mortal. I am eternal! I will crush you!'")

print()
print("The FinalBoss lurches forward, its claws ready to rip you apart.")

print()
print("You're barely hanging on. The monster is relentless, and you can feel your strength fading.")
print("But you know you can't give up. This is the final battle. You must end it.")
print()
print("With a burst of desperation and strength, you throw your sword at the FinalBoss!")

print(f"The sword flies through the air and lands with a mighty strike")

print()
print("With a final, dramatic roar, the FinalBoss is pierced through the heart by your sword!")
print("It collapses to the ground, defeated for good.")
print("You’ve won. You’ve survived the Lair of Death.")