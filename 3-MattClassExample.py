import random
#just to have some fun.... i am going to show you another class with more complext functions insteaed of it.

class Matt: #since im not going to be doing alot with modification of this class... im not allowing anything to be modified.
    def __init__(self): 
        self.name = "Matt"
    
class Friend:
    def __init__(self, name):
        self.name = name

def funnySaying():
    funnySaying =["But Matt Said", "They call me Meldown Matt!", "Woman is for Bed and Breakfast!", "I am the Mattinator!"]
    return random.choice(funnySaying)

def genereate_friend():
    friendNames = ["Brandon", "Freddy", "Kimmy", "Brittany", "Joyce"]
    name = random.choice(friendNames)
    return Friend(name)

friend1 = genereate_friend()
matt = Matt() #i never set an input, so im just createing a new Matt...and assigning it to matt.

print(f"{matt.name} tells {friend1.name} '{funnySaying()}'")

# just a fun example... its kinda dumb but give syou an idea... techncially... i could generate 2 Matts....
matt2 = Matt()
#them have them tell each other....
print(f"{matt.name} tells {matt2.name} '{funnySaying()}'")

#hopefully this helps...