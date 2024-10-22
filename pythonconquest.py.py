import random

player_health = 100
enemy_health = 100

#create rooms
room_types = ["Castle Dungeon ", "Castle Treasury", "Castle Library "]
room = random.choice(room_types)

#spawn enemy 
enemy_types = [" Ogre  ", " Troll ", "Goblin"]
enemy = random.choice(enemy_types)

#player class
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
p1 = Player("BRANDON", 100)

#enemy class
#class Enemy:
#    def __init__(self, name, health):
#        self.name = name
#        self.health = health

 
def display_hud():
        print("_______________________________________________________________________")
        print("|  PLAYER HEALTH  |         ROOM         |   ENEMY   |  ENEMY HEALTH   |")
        print("|______",player_health,"______|___",room,"__|__",enemy,"_|______",enemy_health,"______|")
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
        print("VOICE: '...wake up...'")
        print("VOICE: '...wake up...'")
        print(f"VOICE: 'Wake up",p1.name,"!'")
        print(f"", p1.name,": 'Where am I?? Who are you??'")
        print(f"VOICE: 'You have awaken inside the",room,"...'")
        print(f"",p1.name,"'Why am I here? How did I get here? ...and WHO ARE YOU?!'")
        print("VOICE: 'My name is Master Scrum.  The Coding Village is under seige by the sinister Lord Python and his evil horde of creatures...'")
        print("VOICE: 'There's no time to waste! Stand up and draw your sword and prepare to defend Coding Village!'")
        print(f"VOICE: 'Watch out! There's a ", enemy, "nearby!'")
        print()

#player attack function
def player_attack():
    global player_health
    global enemy_health
    player_attack_value = [5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100]
    p_attack_value = random.choice(player_attack_value)
    enemy_attack_value = [5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100]
    e_attack_value = random.choice(enemy_attack_value)
    try:
        if p_attack_value == e_attack_value:
            player_health -= p_attack_value
            enemy_health -= e_attack_value
            print(f"VOICE: 'You both lost {p_attack_value} health!'")
            return
        if p_attack_value >= e_attack_value:
            enemy_health -= p_attack_value
            print(f"SLICE! {enemy} has lost {p_attack_value} health!")
            if enemy_health <= 0:
                enemy_health = 0
                print(f"VOICE: 'WELL DONE",p1.name,"! You killed the",enemy,"!'")
            return
        else:
             player_health -= e_attack_value
             print(f"OUCH! {enemy} struck you and you lost {e_attack_value} health!")
             if player_health <= 0:
                 player_health = 0
                 print("YOU'RE DEAD!")
             return
    except ValueError:
        print()   


#player flee function and divide player health in half
def player_flee ():
    global player_health
    player_health /= int(2)
    print("VOICE: 'Regain your composure HERO! Don't give up so easily!'")
    return

# Function to run program
def run():
    story_intro()
    while player_health > 0:
        display_hud()
        choice = input("Choose wisely (1-3): ")
        print()
        if choice == "1":
            player_attack()
        elif choice == "2":
            player_flee()
        elif choice == "3":
            print("YOU COWARD! You miserable worm! The Coding Village Scrum Master was counting on you to fight!")
            break
        else:
            print("Invalid entry, please try again.")

# This runs program
if __name__ == "__main__":
    run()