import random

#TITLE FUNCTION
def title():
    print(
        r"______      _   _                 _____                                   _   "
    )
    print(
        r"| ___ \    | | | |               /  __ \                                 | |  "
    )
    print(
        r"| |_/ /   _| |_| |__   ___  _ __ | /  \/ ___  _ __   __ _ _   _  ___  ___| |_ "
    )
    print(
        r"|  __/ | | | __| '_ \ / _ \| '_ \| |    / _ \| '_ \ / _` | | | |/ _ \/ __| __|"
    )
    print(
        r"| |  | |_| | |_| | | | (_) | | | | \__/\ (_) | | | | (_| | |_| |  __/\__ \ |_ "
    )
    print(
        r"\_|   \__, |\__|_| |_|\___/|_| |_|\____/\___/|_| |_|\__, |\__,_|\___||___/\__|"
    )
    print(
        r"       __/ |                                           | |                    "
    )
    print(
        r"      |___/                                            |_|                    "
    )
print()

# PLAYER CLASS
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.damage = 0
        
    def attack(self, enemy):
        damage = random.randint(10, 20)
        enemy1.health -= damage
        # we will put enemy damage here when its time.
        print(f"{self.name} attacks -- for {damage} damage!")

player_name = input("Enter your Player name: ")
player = Player(player_name, 0)
player.health = 100



# ENEMY CLASS
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, player):
        damage = random.randint(1, 20)
        player.health -= damage
        print(f"{self.name} attacks {player_name} with {weapon} for {damage} damage!")



# RANDOM ENEMY SPAWN
def spawn_enemy():
    enemies = [("Ogre", 100), 
               ("Troll", 60), 
               ("Goblin", 50), 
               ("Dragon", 200), 
               ("Witch", 75)
               ]
    name, health = random.choice(enemies) #it takes both values. the name and health.
    return Enemy(name, health) # it returns the enemy object with the name and health.
enemy1 = spawn_enemy() 


#RANDOM ROOM SPAWN
def generate_room():
    room_type = ["Dungeon", 
                 "Treasury", 
                 "Library"
                 ]
    return random.choice(room_type)
room = generate_room()

#RANDOM ENEMY WEAPON
def enemy_weapon():
    weapons = ["sword",
               "club",
               "dagger"
               ]
    return random.choice(weapons)
weapon = enemy_weapon()


#PRINT STATEMENTS TO CHECK THINGS ARE WORKING PROPERLY
title()
print()
print()
print(f"{player.name} is your player name!")
print()
print(f"You are in {room}.")
print()
print(f"Your current health = {player.health}")
print()
print(f"A {enemy1.name} with {enemy1.health} health has spawned randomly! They're wielding a {weapon}.")
print()
player.attack(enemy1)
print()
print(f"{enemy1.name} health has diminished to {enemy1.health}")
print()
enemy1.attack(player)
print()
print(f"{player.name}'s health has diminished to {player.health}!")
print()
player.attack(enemy1)
print()
print(f"{enemy1.name} health has diminished to {enemy1.health}")
print()
enemy1.attack(player)
print()
print(f"{player.name}'s health has diminished to {player.health}!")
print()

#NEXT STEP IS TO CREATE A MENU FOR THE PLAYER TO DECIDE WHETHER TO ATTACK, HEAL, EXIT. 
#SIMILAR TO VURTUAL PRINTER..WON'T BE ABLE TO HEAL BEYOND 100.
#AFTER EACH CHOICE TO EITHER ATTACK OR HEAL, PLAYER MUST ENTER A CHOICE TO KEEP ATTACKING OR HEAL OR EXIT
#STILL NEED TO INTRODUCE THE WHILE PLAYER IS ALIVE
#ADD YOUR COMMENTS


# FUNCTION TO RUN PROGRAM
#def run():


# This runs program
#if __name__ == "__main__":
    #run()
