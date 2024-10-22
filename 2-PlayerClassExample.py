import random
# so when you think about building a game, and your going to build objects, you want to do it with a class.
# classes DEFINE objects.

#so.. at a basic example, lets build a player class, then we will build a small tiny game to show you how you can use this in a game.

#what do we care about with a player? lets start with just a name and some health.

class Player: #remember we capitolize a class.
    #so.. this is the blueprint. The only input i need is the name... because every player will have the same stats, the only thing i need to know
    #is the name. Technically i could remove name and just have self then everyone will have the same name and the same health.
    def __init__(self, name): 
        self.name = name 
        self.health = 100 
        #so above is the basic class constructor  so if i did nothing else to this the only thing tha twould happen is you would
        #set a variable to player and th eonly thing is that player would have a name and health.
        #but we want a player to attack... and to to be attacked, and we need to know if he is alive... so a function to keep track of his health.
        #so we build functions INSIDE the class that controls these things
        #indentions are important to classes if the function is inside the player it needs to be indendtioned to be inside the class.
    
    def attack(self):
        damage = random.randint(1, 10)
        print(f"{self.name} attacks for {damage} damage!")
        return damage
        #so what we did above is create a function, that is taking in the player... which has a name and health and setting a variable to damage.
        # that variable will get randomly generated and set to damage. We COULD return damage. Or just print it out.. either way works, but generally
        # you want the function to handle all the logic. So if you were attacking a monster you would do monster.health -= damage. then jusst print i tout.
        # so thats all i am doing here, minus the actual health loss to anything.
        # for the purposes of this.... since i dont have  a 2nd class..... im going ot just return the value....so we can use it in the while loop

    def healPlayer(self):
        healAmount = random.randint(1, 10)
        self.health += healAmount
        print(f"{self.name} heals for {healAmount} health!")
        #so this is the same as the attack function, but instead is taking the self.health from teh init and increatsing it by the random generateed
        #number. Generally speaking your going to want logic here to hit a health cap so you dont go over 100... but you
        # can figure out how to do that in the actual game.

    def isAlive(self):
        return self.health > 0
        # so this function is going to return a true false. It is passing in teh player self.. which remember contains a name and health
        # and IF the healht is greater than 0 it will return true. 

# so now this is an example of an entire player class that we can do a lot of stuff wuth...
# im not going to build a monster class and instead ill just do it inline with hard coded magic number

# soooo Something the game was messing you up with, is the difference between a class and a funciotn. 
# You only need a class for things you are going to reuse. 
# keep a basic function (ouside of the class) if you just wanted  
# 
# example you can generate a random player... since thats all the functiuon is doing, then you dont need to make it a class.
def generatePlayer():
    playerNames = ["Bob", "Joe", "Steve", "Tom", "Jerry"] #so all im doing here is paying in what we asked for in the constructor... which was just a name.
    name = random.choice(playerNames) # so same thing here, im doing a random.choice to select a random player name.. from the list....
    return Player(name) # so now that i have the name, i can return the player class with the name.

#now that we have a function.... that we created a list of names.... randomly selecting one of those names... then RETURNING a player...
# we can call that function to randomly generate a player class....
#  and whats neat, is we can set it to a variable...
player1 = generatePlayer()
player2 = generatePlayer()
player3 = generatePlayer()

#if i coded no more ... this basically is just randomly selecting a name and creating a player... so you can target this many differnet ways..
#and since its randmoly generated everyt time, if you ran this function over and over and over agan, each would be different
print(player1.name)
print(player2.name)
print(player3.name)

#you can see if they are alive......
print("--------")
print(player1.isAlive())
print(player2.isAlive())
print(player3.isAlive())

#you can see thier health...
print("--------")
print(player1.health)
print(player2.health)
print(player3.health)

#Since you already crated the palyer.... you can now mess with their health.
player1.health -= 10
player2.health -= 20
player3.health -= 30

#then print it again and see something different...
print("--------")
print(player1.health)
print(player2.health)
print(player3.health)

#now we heal them for a random number.....
player1.healPlayer()
player2.healPlayer()
player3.healPlayer()

#now we check on it.
print("--------")
print(player1.health)
print(player2.health)
print(player3.health)

#nowe we will set them back to full health so we can play with while loops....
player1.health = 100
player2.health = 100
player3.health = 100

#so... im not goiung to build an interactive game... but im going to have player1 and player 2 fight each other until one dies...
# basically im going to do a while loop, that is checking to see if either is alive and as long as both are alive... they will each take turns attacking.
#player1 will go first with the unfair advantage.

while player1.isAlive() and player2.isAlive():
    player2.health -= player1.attack() #since attack is returning a damage amount.... we can do this.... its bad practice... but for this demo its fine.
    if player2.isAlive():
        player1.health -= player2.attack() #same thing here... player 2 is attacking player 1

        #so this is just an example.... but classes can be pretty good.... you can do a lot with them.
        #i encourage you to play with this just to get an understanding.