import random
import time

# Variables for player and boss stats
player_health = 100
player_attack_power = 15
boss_health = 150
boss_attack_power = 20
special_ability = "Shadow Blast"

# Function for player's turn with a story description
def player_turn():
    global player_health, boss_health
    print("\nYou gather your courage and prepare for action.")
    print("What will you do?")
    print("a. Strike with all your might!")
    print("b. Try to heal your wounds.")
    input81 = input("Choose your action (a or b): ")

    if input81 == "a":
        damage = random.randint(10, 20)  # Player attack damage
        boss_health -= damage
        print(f"\nWith a powerful swing of your weapon, you land a hit on FinalBoss, dealing {damage} damage!")
    elif input81 == "b":
        heal_amount = random.randint(10, 20)
        player_health += heal_amount
        if player_health > 100:  # Max health cap
            player_health = 100
        print(f"\nYou quickly drink a potion, feeling a rush of healing energy, restoring {heal_amount} health.")
    else:
        print("You hesitate for a moment, unsure of what to do. Your opponent waits for your next move.")

# Function for boss's turn with a story description
def boss_turn():
    global player_health, boss_health
    print("\nFinalBoss steps forward, looming over you with a terrifying presence.")
    # Boss decides whether to attack or use special ability
    input82 = random.choice(["attack", "special"])  # Randomly choose attack or special ability
    if input82 == "special":
        print(f"With a sinister smile, FinalBoss raises their hand and unleashes {special_ability}!")
        damage = random.randint(15, 25)  # Special ability causes higher damage
        player_health -= damage
        print(f"Shadowy tendrils lash out, dealing {damage} damage to you!")
    else:
        damage = random.randint(5, 15)  # Boss attack damage
        player_health -= damage
        print(f"FinalBoss strikes you with a fierce blow, causing {damage} damage to your body!")

# Function to check if someone is alive
def is_alive(health):
    return health > 0

# Main game loop
def game_loop():
    global player_health, boss_health
    print("A battle to the death begins in the dark, eerie dungeon...")

    while is_alive(player_health) and is_alive(boss_health):
        # Show the current health of both the player and the boss
        print(f"\nYour health: {player_health}")
        print(f"FinalBoss's health: {boss_health}")

        # Player's turn
        player_turn()

        if not is_alive(boss_health):
            print(f"\nWith a final blow, you defeat FinalBoss! Victory is yours!")
            break

        # Boss's turn
        boss_turn()

        if not is_alive(player_health):
            print("\nYou fall to the ground, your vision fading. FinalBoss has claimed victory.")
            break

        # Adding a little pause for dramatic effect
        time.sleep(2)

# Start the game loop
game_loop()
