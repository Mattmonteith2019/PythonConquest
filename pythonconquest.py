import random

#removing global vars in lieu of class vars
#player_health = 100
#enemy_health = 100

def room_list(sequence):
    return random.choice(sequence)
options = ["Dungeon", "Treasury", "Library"]
room = room_list(options)

def generate_room():
    room_type = ["Dungeon", "Treasury", "Library"]
    return random.choice(room_type)
 
narrator = '\033[3m'"NARRATOR: "'\033[0M'

#player class
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    #here is the player attack. It will eventually take in the enemy along with self, but for now its just doing the damage and printing. 
    def attack(self):
        damage = random.randint(10, 20)
        #we will put enemy damage here when its dime.
        print(f"{self.name} attacks -- for {damage} damage!")

# get rid of this p1 = Player... the init looks good.
p1 = Player("BRANDON", 100)

#enemy class
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def attack(self):
        damage = random.randint(1, 10)
        print(f"{self.name} attacks for {damage} damage!")
        return damage

def spawn_enemy():
    enemies = [("Ogre", 100), ("Troll", 100), ("Goblin", 100)]
    name, health = random.choice(enemies)
    print(name)
    return Enemy(name)
 
def display_hud():
        print(r"_______________________________________________________________________")
        print(r"|  PLAYER HEALTH  |         ROOM         |   ENEMY   |  ENEMY HEALTH   |")
        #print(r"|______",p1.health,"______|___",room,"__|__",Enemy.name,"_|______",Enemy.health,"______|") removed this for now to stop the error
        print()
        print("Select from the following options: ")
        print(" 1. Attack")
        print(" 2. Flee")
        print(" 3. Exit game")
        print()


def story_intro():
        print(r"______      _   _                 _____                                   _   ")
        print(r"| ___ \    | | | |               /  __ \                                 | |  ")
        print(r"| |_/ /   _| |_| |__   ___  _ __ | /  \/ ___  _ __   __ _ _   _  ___  ___| |_ ")
        print(r"|  __/ | | | __| '_ \ / _ \| '_ \| |    / _ \| '_ \ / _` | | | |/ _ \/ __| __|")
        print(r"| |  | |_| | |_| | | | (_) | | | | \__/\ (_) | | | | (_| | |_| |  __/\__ \ |_ ")
        print(r"\_|   \__, |\__|_| |_|\___/|_| |_|\____/\___/|_| |_|\__, |\__,_|\___||___/\__|")
        print(r"       __/ |                                           | |                    ")
        print(r"      |___/                                            |_|                    ")
        print()
        print(f"{narrator}...wake up...")
        print(f"{narrator}...wake up...")
        print(f"{narrator}Wake up",p1.name,"!")
        print(f"{p1.name}: Where am I?? Who are you??")
        print(f"{narrator}You have awaken inside the",room,"...")
        print(f"{p1.name}: Why am I here? How did I get here? ...and WHO ARE YOU?!")
        print(f"{narrator}My name is Master Scrum.  The Coding Village is under seige by the sinister Lord Python and his evil horde of creatures...")
        print(f"{narrator}There's no time to waste! Stand up and draw your sword and prepare to defend Coding Village!")
        #print(f"{narrator}Watch out! There's a {Enemy.name} nearby!") Removed this for now to stop the error
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