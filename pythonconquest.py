import random

#you are going to want to set these values in classes...
player_health = 100
enemy_health = 100

#create rooms
#ok... put this in a function. This is really good, but... if you put it in a function you can call it over and over again.
#you can remove the room = and instead do return random.choice(room_types) and then call the function when you need it and it will return a room_type ranodmly.
room_types = ["Castle Dungeon ", "Castle Treasury", "Castle Library "]
room = random.choice(room_types)

#spawn enemy 
#again... create a function to do this. I gave you an example in the player class example of returning a class in a function.
# you want to be able to create a troll at random with "Enemey abilities."
enemy_types = [" Ogre  ", " Troll ", "Goblin"]
enemy = random.choice(enemy_types)

#player class
class Player:
    def __init__(self, name, health): #you dont need the health as an input unless you want to define this for every player... you are better off
        # just hard coding the health by doing self.health = 100
        #that being said, if you plan on healing... i would create a max health value.. you will change the self.health but the max health is a good check value.
        self.name = name
        self.health = health
p1 = Player("BRANDON", 100) # you dont need this... if there is only going to be 1 player you will generate the player at the start of the game.
#the very first thing you will do in the game is the function you have here....you could even have fun with it.
# you can create an input...and have the player enter the name, save it as a variable.
#then you can do player =Player(playername)

#enemy class
#class Enemy:
#    def __init__(self, name, health):
#        self.name = name
#        self.health = health

 
 #this is great! but i would have the display_hud take in values... so it is reusable. So have it take in player_health, room, enemey and enemey_health.
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
# so just so you know. I added the r in front of the text. This is called "raw text" alot of times / and \ are used to overwrite string code.
# so if your doing stuff with them, you can use raw text and it ignores the overwrite commends. I was getting an error with this drawing.
# adding hte r stopped that. 
#do the same here for the one above... have it take in the players name,  and room so it can generate it dynanically.
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
#you want a player attack function in the player class... i gave you an example in the Playerclass Example.
# i think you have the right idea here... so im not going to mess with this any more.
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