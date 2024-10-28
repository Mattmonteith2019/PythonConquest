# So lets talk about a funciton. First im going ot make a simple Print function
def printFunction1():
    print("Print Function 1: The Cow Goes Moo")

#obviously if you call it, you just do
printFunction1()
#and if you ran this it would print out the statement... but lets say you cant to change the wording...

animal = "Cow"
#you did something something like this when you did p1= 
#then you put it in the funciton.
def printFunction2():
    print(f"Print Function 2: The {animal} goes moo")

#this works... but it does not make it reusable. if i call the function....
printFunction2()
#i get the same thing... 
#im gonna build a small class here for the next example..

class Animal:
    def __init__(self, name):
        self.name = name
#ok basic Animal class and it takes in a name as the contructor.
#lets create an animal...
animal2 = Animal("Dog")
# and lets build one more print function....
def printFunction3():
    print(f"Print Function 3: The {animal2.name} goes bark")
# this the type of function you made...
#looking at this. you are saying everytime i call printfunciton3 no matter what, it wil be animal2.name
printFunction3()
#this is fine... if you had the function inside of a class, but you want the function to be reusable. No matter what.... 
#so what you do, is you build inputs into the funciton.

#you can call these inputs whatever you want.
#so... lets build a new class....that does 2 things. We are going to hardcode the 2nd thing...
class Friend:
    def __init__(self, name):
        self.name = name
        self.statement = "Hello!"
#so this is a friend class, that in the init, has a name, and a statement, we hardcoded the statement, but it REQUIRES a name to input.
#so lets make a friend.....
friend1 = Friend("Brandon")
#so this variable says....create me a friend called Brandon...
#now lets build a friend 2.... a 2nd friend...
friend2 = Friend("Freddy")
#so now, i have created 2 friends... both friends have the same statement of "Hello..."
#now lets create a new print function...
def printFunction4():
    print(f"Print Function 4: {friend1.name} says {friend1.statement}")

#so the downside to this... you created printfunction that it only prints what friend1 no matter what...
printFunction4()
#if you WANT this... its fine.. but its really not good idea....
# this is orginally how you set up the HUD in your game and what was causing a ton of errros.
#it actually still has errors because of the enemy....
# your hardcoding things like the room, and the player and the enemey, so it wil error out.
#this is why you build your classes and then your functions, and then your actual run.
#so lets rebuild printfunciton4 as printfunction5 with a better approach.....
def printFunction5(friend):
    print(f"Print Function 5: {friend.name} says {friend.statement}")
#so now what i ahve done is say take in a friend, then no matter who that friend is, take the name and the statement and print it...
# so to run this... you have to PASS the function data...
#we arlready have our friends....
#you just pass the whole variable in...
printFunction5(friend1)
#but i can also passin anothe rone...
printFunction5(friend2)
#this measn the function is now reusable...
#Soooo lets explain the input a but more... im going ot create another one..
def printFunction6(bleblorp):
    print(f"Print Function 6: I have a friend named {bleblorp}.")
#what you CALL your input only matters at teh function level, so you can call the input whatever you want....
#however, when you PASS it. you have to match what your passing it.... if you loop at teh funciton above.. look at the statment.
#its looking for a string, and i did not add a .name after bleblorp... so i cant pass tehw whole friend in... because friend contains 
#both a name and a statment.. 
printFunction6(friend1) #you will see when you run this, its kinda erroring out, it does not know what you actually print..
#so instead.... we tell it what bleblorp is...
printFunction6(friend1.name)#so now im passing the name.... which is a string in...
#so thing if bleblorp as a placeholder..... BUt you generally want to call it what you want it to be.. so obviously "friend" names more sense...

#so lets talk about more complex uses and how to use nameing structures...
# lets build a class... that takes in a few inputs...maybe 4... just to get a point across...
class Wife:
    def __init__(self, name, statment, favorite_food, dislike):
        self.name = name
        self.statement = statment
        self.favorite_food = favorite_food
        self.dislike = dislike
        self.statement2 = "Blerg"
        self.number_of_eyes = 2
#so i just built a class.... it has 4 inputs and 2 hard coded datapoints because no matter who is it, i want statment2 to be "blerg"
# and for them to have 2 eyes. You only hard card things that you want to be consistent.
# so in a game, if every player will have 100 health, then you can hard code that
# for a monster, you might want it to be different... then you would NOT hard code it.
# so lets look at different ways we can use this class in a function..
wife1 = Wife("Joyce", "Oh Boy", "sushi", "working outside")
#so i just created wife 1. all of those things that we created are all string values
#lets create 2 more, so you can see reusability...
wife2 = Wife("Kimmy", "Bless his heart", "steak", "being inside")
wife3 = Wife("Brittany", "but Matt said...", "hibachi", "not being with friends")
# so lets build a reusable funciton that will print something more complex...
def printFunction7(wife):
    print(f"Print Function 7: Hi my name is {wife.name}.")
    print(f"Print Function 7: when i talk about my husband I say {wife.statement}.")
    print(f"Print Function 7: I like  {wife.favorite_food} to eat")
    print(f"Print Function 7: I dislike  {wife.dislike}")
    print(f"Print Function 7: Sometimes I say  {wife.statement2}")
    print(f"Print Function 7: I have {wife.number_of_eyes} eyes")

#so just a print statement with a ton of prints... but becaues its taking the WHOLE wife object in. we can divy it up just by passing
#in the wife class.
printFunction7(wife1)

#we can take that same print statement and make it so we require specific things to be passed in.....
#but you can see, the input now requires a bunch of stuff..
def printFunction8(name, statement, favorite_food, dislike, statement2, number_of_eyes):
    print(f"Print Function 8: Hi my name is {name}.")
    print(f"Print Function 8: when i talk about my husband I say {statement}.")
    print(f"Print Function 8: I like  {favorite_food} to eat")
    print(f"Print Function 8: I dislike  {dislike}")
    print(f"Print Function 8: Sometimes I say  {statement2}")
    print(f"Print Function 8: I have {number_of_eyes} eyes")
#now instead of just passing in the whole Wife class.... we have to pass in each required object...
printFunction8(wife2.name, wife2.statement, wife2.favorite_food, wife2.dislike, wife2.statement2, wife2.number_of_eyes)
#it still works the same.... but its a bit more complicated... it also means that the printfunction8 can take in any random string though...
#instead of an object.....
printFunction8("Blerg", "bloop", "bleep", "blop", "bing", 5)
#so it really just matters what you are trying to do.....

#now lets take a class with a function in it..
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, monster):
        damage = 5
        monster.health -= damage
        print(f"{self.name} attacks {monster.name} for {damage} damage!")

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 15

    def attack(self, player):
        damage = 5
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!") 

#ok we have 2 classes here... both are basically the same. One is a player, the other is a monster.  They are identical
#except for the player starts with 100 health and the monster has 15...  i also made it so both monster and player do 5 damage, every time.
# So lets create our player and monster...
player = Player("Matt") #the only thing we have in the player init is the name....
monster = Monster("Troll") #same with the onster... just the name.
# right now if we run the function, we have a player and a monster...
#if i wanted the monster to attack a player.. all i have to do is this.
print("First attack example:")
monster.attack(player)
#in this funciton.... i basically saying run the monster attack funtion, inside the monster class.
# because the monsterclass is taking in the player object... i just pass in the player object. 
#i do the same for the player...
print("First attack example:")
player.attack(monster)

#then you can print the health and see... that it DOES mess with the player...
print(f"Monster health is: {monster.health}")
print(f"Player health is: {player.health}")

#but this is generic... which is good... im going to get expressive. so you can SEE what i mean by passing data,
#im going to create a new monster.
ogre = Monster("Ogre")
#so instead of calling it a generic monster... i called it an ogre
#lets do the same thing.....
print("2nd attack example:")
ogre.attack(player)
print(f"Player health is: {player.health}")
#so... this time we created the ogre and i said, take in the player... and attack him.

#hopefuly these exsamples help with class and function use...
# i would highly recommend learning this in depth, because classes and functions are the fundemental root of complex applciations.