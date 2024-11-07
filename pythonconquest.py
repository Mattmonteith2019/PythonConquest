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

#GAME OVER TITLE
def game_over():
    print()
    print(r"   ____    _    __  __ _____    _____     _______ ____")  
    print(r"  / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ ") 
    print(r" | |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) |")
    print(r" | |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < ") 
    print(r"  \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\ ")
    print()

# PLAYER CLASS
class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.damage = 0
        self.alive = True
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            
    def is_alive(self):
        return self.health > 0
        
    def attack(self, enemy):
        damage = random.randint(10, 20)
        enemy.take_damage(damage)
        # we will put enemy damage here when its time.
        print(f"{self.name} attacks {enemy.name} with {pweapon} for {damage} damage!")
        print()
            
    def heal(self):
        self.health = 100
        print(f"{self.name} heals to full health {self.health}")
    

#player_name = input("Enter your Player name: ")
#player = Player(player_name, 0)


# ENEMY CLASS
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            #print(f"{self.name} has been slain!")
            
    def is_alive(self):
        return self.health > 0

    def attack(self, player):
        damage = random.randint(1, 20)
        player.take_damage(damage)
        print(f"{self.name} counter-attacks {player.name} with {weapon} for {damage} damage!")


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


#RANDOM ROOM SPAWN
def generate_room():
    room_type = ["Dungeon", 
                 "Treasury", 
                 "Library"
                 ]
    return random.choice(room_type)
room = generate_room()

#RANDOM PLAYER WEAPON
def player_weapon():
    pweapons = ["sword",
                "bow and arrow",
                "sling-shot",
                "javelin"
                ]
    return random.choice(pweapons)
pweapon = player_weapon()

#RANDOM ENEMY WEAPON
def enemy_weapon():
    weapons = ["sword",
               "club",
               "dagger"
               ]
    return random.choice(weapons)
weapon = enemy_weapon()

#DISPLAY HUD
def display_hud(player, enemy, weapon, room):
    print(f"ROOM: {room}")
    print(f"{player.name} HEALTH: {player.health}")
    print(f"{player.name} WEAPON: {pweapon}")
    print(f"ENEMY: {enemy.name}")
    print(f"ENEMY HEALTH: {enemy.health}")
    print(f"ENEMY WEAPON: {weapon}")
    print()

#DISPLAY HUD2
def ingame_hud(player, enemy, weapon):
    print(f"{player.name} HEALTH: {player.health}")
    print(f"{enemy.name} HEALTH: {enemy.health}")
    print()
    print("Player options: ")
    print(" 1. ATTACK!")
    print(" 2. Heal")
    print(" 3. Exit Game.")
    print(r"_____________")

# FUNCTION TO RUN PROGRAM
def run():
    title()
    print()
    player_name = input("Enter your Player name: ")
    player = Player(player_name)
    #player = Player(health=100)
    enemy1 = spawn_enemy()
    room = generate_room()
    weapon = enemy_weapon()
    pweapon = player_weapon()
    print()
    display_hud(player, enemy1, weapon, room)    
    while player.is_alive():
        ingame_hud(player, enemy1, weapon)
        choice = input("Make your choice (1-3): ")
        print()
        if choice == "1":
            player.attack(enemy1)
            if enemy1.is_alive():
                enemy1.attack(player)
                if player.health <= 0:
                    print(f"YOU'VE BEEN SLAIN! YOU'RE DEAD.")
                    game_over()
                    break
            elif not enemy1.is_alive():
                print(f"{enemy1.name} is slain!")
                enemy1 = spawn_enemy() # New enemy
                room = generate_room() # New room
                weapon = enemy_weapon() # New weapon
                print(f"Behold! You're now in {room} and a new enemy has spawned - - - a {enemy1.name} wielding a {weapon} with {enemy1.health} health!")
        elif choice == "2":
            player.heal()
        elif choice == "3":
            print("Goodbye! You are now exiting PythonConquest game.")
            print()
            break
        else:
            print("Invalid entry. Please try again.")
            print() 


# This runs program
if __name__ == "__main__":
    run()
