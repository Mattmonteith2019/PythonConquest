import random

#My original function for generating room
#def room_list(sequence):
#    return random.choice(sequence)
#options = ["Dungeon", "Treasury", "Library"]
#room = room_list(options)

#Brandon's function for generate room...doesn't allow me to use the return value in HUD 
### Brandons Comment to that you need to add an input in the return to do that... but im gonna remove the hud for now...
def generate_room():
    room_type = ["Dungeon", "Treasury", "Library"]
    return random.choice(room_type)

narrator = "NARRATOR: "

#player class
#so what i changed here is removed the health variable and hardcoded a value of 100... that way when you create the player he has 100 health.
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    #here is the player attack. It will eventually take in the enemy along with self, but for now its just doing the damage and printing. 
    def attack(self):
        damage = random.randint(10, 20)
        #we will put enemy damage here when its dime.
        print(f"{self.name} attacks -- for {damage} damage!")

# get rid of this p1 = Player... the init looks good.
#p1 = Player("BRANDON", 100)

#enemy class
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def attack(self):
        damage = random.randint(1, 10)
        print(f"{self.name} attacks for {damage} damage!")
        return damage

#This function doesn't work.  there is no way to pass this value into HUD or anywhere else for that matter.
def spawn_enemy():
    enemies = [("Ogre", 100), ("Troll", 100), ("Goblin", 100)]
    name, health = random.choice(enemies)
    print(name, health)
    return Enemy(name, health)
 
 # I added inputs into your  hud and then fixed the inputs in the 
def display_hud(player, room):
        print(r"_______________________________________________________________________")
        print(r"|  PLAYER HEALTH  |         ROOM         |   ENEMY   |  ENEMY HEALTH   |")
        print(r"|______",player.health,"______|___",room,"__|__")#name,"_|______")#Enemy.health,"______|")im leaving this commented out.. because we dont have this input yet.
        print()
        print("Select from the following options: ")
        print(" 1. Attack")
        print(" 2. Flee")
        print(" 3. Exit game")
        print()

# I added the inputs into the function, then i fixed the inputs in the statements.
def story_intro(player, room):
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
        print(f"{narrator}Wake up",player.name,"!")
        print(f"{player.name}: Where am I?? Who are you??")
        print(f"{narrator}You have awaken inside the",room,"...")
        print(f"{player.name}: Why am I here? How did I get here? ...and WHO ARE YOU?!")
        print(f"{narrator}My name is Master Scrum.  The Coding Village is under seige by the sinister Lord Python and his evil horde of creatures...")
        print(f"{narrator}There's no time to waste! Stand up and draw your sword and prepare to defend Coding Village!")
        #print(f"{narrator}Watch out! There's a",enemy,"nearby!")
        print()

#I removed Flee for now....

#ok... so i have no more run function, but i want to show you how this would work.

#first we create a player....
player_name = input("Enter your player's name: ")
player = Player(player_name)

#now we can pass this into the story intro and display hud functions
story_intro(player, generate_room())



""" # Function to run program
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
    run() """