import random

#Global vars marked out, trying to use classes instead
#player_health = 100
#enemy_health = 100

#create rooms
room_types = ["Castle Dungeon ", "Castle Treasury", "Castle Library "]
room = random.choice(room_types)

#spawn enemy 
#enemy_types = [" Ogre  ", " Troll ", "Goblin"]
#enemy = random.choice(enemy_types)

#player class
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        print("Walking...")
    
    def run(self):
        print("Running...")
    
    def attack(self):
        damage = random.randint(1, 10)
        print(f"{self.name} attacks for {damage} damage!")
        return damage
    
    def healPlayer(self):
        healAmount = random.randint(1, 10)
        self.health += healAmount
        print(f"{self.name} heals for {healAmount} health!")
        return healAmount
    
    def isAlive(self):
        return self.health > 0
    
narrator = '\033[3m' + "NARRATOR: " + '\033[0m'

p1 = Player("BRANDON", 100)
p1.walk()

p1.run()

#enemy class
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def attack(self):
        damage = random.randint(1, 10)
        print(f"{Enemy.name} attacks for {damage} damage!")
        return damage
    
    def spawn_enemy(self):
        enemyNames = ["OGRE", "TROLL", "GOBLIN"]
        name = random.choice(enemyNames)
        return Enemy(name)
enemy1 = spawn_enemy()

def display_hud():
        print("_______________________________________________________________________")
        print("|  PLAYER HEALTH  |         ROOM         |   ENEMY   |  ENEMY HEALTH   |")
        print("|______",p1.health,"______|___",room,"__|__",enemy1,"_|______",Enemy.health,"______|")
        print()
        print("Select from the following options: ")
        print(" 1. Attack")
        print(" 2. Flee")
        print(" 3. Exit game")
        print()

# initial story intro
def story_intro():
        print("______      _   _                 _____                                   _   ")
        print("| ___ \    | | | |               /  __ \                                 | |  ")
        print("| |_/ /   _| |_| |__   ___  _ __ | /  \/ ___  _ __   __ _ _   _  ___  ___| |_ ")
        print("|  __/ | | | __| '_ \ / _ \| '_ \| |    / _ \| '_ \ / _` | | | |/ _ \/ __| __|")
        print("| |  | |_| | |_| | | | (_) | | | | \__/\ (_) | | | | (_| | |_| |  __/\__ \ |_ ")
        print("\_|   \__, |\__|_| |_|\___/|_| |_|\____/\___/|_| |_|\__, |\__,_|\___||___/\__|")
        print("       __/ |                                           | |                    ")
        print("      |___/                                            |_|                    ")
        print()
        print(f"{narrator}...wake up...")
        print(f"{narrator}...wake up...")
        print(f"{narrator}Wake up",p1.name,"!")
        print(f"{p1.name}: Where am I?? Who are you??")
        print(f"{narrator}You have awaken inside the",room,"...")
        print(f"{p1.name}: Why am I here? How did I get here? ...and WHO ARE YOU?!")
        print(f"{narrator}My name is Master Scrum.  The Coding Village is under seige by the sinister Lord Python and his evil horde of creatures...")
        print(f"{narrator}There's no time to waste! Stand up and draw your sword and prepare to defend Coding Village!")
        print(f"{narrator}Watch out! There's a",enemy1,"nearby!")
        print()

#player attack function
def player_attack():
    p1.health
    Enemy.health
    player_attack_value = [5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100]
    p_attack_value = random.choice(player_attack_value)
    enemy_attack_value = [5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100]
    e_attack_value = random.choice(enemy_attack_value)
    try:
        if p_attack_value == e_attack_value:
            p1.health -= p_attack_value
            Enemy.health -= e_attack_value
            print(f"{narrator}You both lost {p_attack_value} health!")
            return
        if p_attack_value >= e_attack_value:
            Enemy.health -= p_attack_value
            print(f"SLICE! {enemy1} has lost {p_attack_value} health!")
            if Enemy.health <= 0:
                Enemy.health = 0
                print(f"{narrator}WELL DONE",p1.name,"! You killed the",enemy1,"!")
            return
        else:
             p1.health -= e_attack_value
             print(f"OUCH! {enemy1} struck you and you lost {e_attack_value} health!")
             if p1.health <= 0:
                 p1.health = 0
                 print(f"{narrator}YOU'RE DEAD!")
             return
    except ValueError:
        print()   


#player flee function and divide player health in half
def player_flee ():
    p1.health
    p1.health /= int(2)
    print(f"{narrator}Regain your composure {p1.name}! Don't give up so easily!")
    return

# Function to run program
def run():
    story_intro()
    while p1.health > 0:
        display_hud()
        choice = input("Choose wisely (1-3): ")
        print()
        if choice == "1":
            player_attack()
        elif choice == "2":
            player_flee()
        elif choice == "3":
            print(f"{narrator}YOU COWARD! You miserable worm! The Coding Village was counting on you to fight!")
            break
        else:
            print("Invalid entry, please try again.")

# This runs program
if __name__ == "__main__":
    run()