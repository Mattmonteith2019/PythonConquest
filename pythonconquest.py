import random

#removing global vars in lieu of class vars
#player_health = 100
#enemy_health = 100

#create rooms
#You need to add this into a function... so you can call it Like you did with the generate enemey. But it returns the "room"
room = ["Castle Dungeon", "Castle Treasury", "Castle Library"]
print(random.choice(room))


narrator = '\033[3m]'"NARRATOR: "'\033[0M'

#player class
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
# get rid of this p1 = Player... the init looks good.
p1 = Player("BRANDON", 100)

#enemy class
class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
        #ok this funciton is 90% there.. remove the return, just do the print now... and =remove the Enemy.name and make it self.name
        # anything IN the function only takes in self, your alreayd in the enemey class
        #the function wont WORK until we have it remove player health, but dont worry about that for now.
    def attack(self):
        damage = random.randint(1, 10)
        print(f"{Enemy.name} attacks for {damage} damage!")
        return damage

#ok remember your enemey takes in 2 things, a name and health, so dont what you ened to do is do ("Ogre", 100),(Troll, 100) etc inside the array
def spawn_enemy():
    enemies = ["Ogre", "Troll", "Goblin"]
    #ok this is CLOSE but what 2 things does your enemy take in? name and health right? so insteady of enemy = its name, health =
    enemy = random.choice(enemies)
    print(enemy)
    #PERFECT
    return Enemy(enemy)
 
def display_hud():
        print("_______________________________________________________________________")
        print("|  PLAYER HEALTH  |         ROOM         |   ENEMY   |  ENEMY HEALTH   |")
        #print("|______",p1.health,"______|___",room,"__|__",Enemy.name,"_|______",Enemy.health,"______|") removed this for now to stop the error
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

#work on player attack next...
# the function should be in the player class, and be only about 4 lines long
# the def with the input of self and the enemy.
# then the damage like your did in the enemey class.
# then your print statement.
# we will worry about the actual damage after you clean this up.....
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
            print(f"SLICE! {Enemy.name} has lost {p_attack_value} health!")
            if Enemy.health <= 0:
                Enemy.health = 0
                print(f"{narrator}WELL DONE",p1.name,"! You killed the",Enemy.name,"!")
            return
        else:
             p1.health -= e_attack_value
             print(f"OUCH! {Enemy.name} struck you and you lost {e_attack_value} health!")
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