# This is a simple example of a class in Python

# Define a class called Animal
# Classes normally starts with a capitol letter, while a function starts with a lower case letter
class Animal:
    # The __init__ method is the constructor, which is called when an object is created.
    def __init__(self, name, species):
        # Attributes of the class: name and species
        self.name = name
        self.species = species
        # so basically what the constructor is doing, is it is saying. ok here is an Animal, it will have a name, and it will be a species. 
        # so think of this init method as a blueprint for the class.

        # then, each class has functions that are specific to that class. So for example... if you wanted to make a Dog speak.
        # you would create a speak function. This function would also work for a cat, or a bird, or a fish.
        # then function below that is used to introduce the animal. This function is specific to the Animal class.
        # you could create endless functions for this class.

    # Method to make the animal speak
    def speak(self):
        print(f"{self.name} makes a sound.")

    # Method to introduce the animal
    def introduce(self):
        print(f"This is {self.name}. It is a {self.species}.")

        # so the cool thing now, is you have a constructor at the top that you BUILD your class with.
        # then you create functions that take in that class and do something with it.
        # so now you can create an instance of the class and do something with it.

# So... this is where you can take the variable and create the class and it STORES the class in the variable. So everything
# reelated to the class is availble to that variablle. 
# the constructor only cared about the name and species. So all your have to do is set those. Because the functions only take in self.
# which is everything in the constructor.
dog = Animal("Buddy", "Dog")

# so now that you have created dog. You can run the functions of "dog" by doing dog.function.
# so to do the introdocue function, you just do dog.introduce(). it will take the input variables you set, and then print them out.
dog.introduce()  # Output: This is Buddy. It is a Dog.
dog.speak()      # Output: Buddy makes a sound.

#so this is where classes get powerful.
cat = Animal("Whiskers", "Cat")
#i just created a cat. I can do the same  thing with cat as i can with the dog..
cat.introduce()  # Output: This is Whiskers. It is a Cat.

# OR i can have the cat and the dog do things together by simply calling the same thing
# you can target any variable in the init by just doing dog.name or cat.name  because you set the name.....
print(f"Both {dog.name} and {cat.name} are animals.")

#you can do all sorts of things once you set up the class.
# and you can reuse them over and over again.
cat.introduce()
dog.introduce()
print(f"{dog.name} is a {dog.species} and {cat.name} is a {cat.species}.")

#this is a basic example of a clas in python.

# so to review. 
# 1. The init is the "blueprint" what you wnat to build.
# 2. The functions are the "tools" you use to do something with the blueprint.
# 3. then you CREATE the class by setting the variables from the constructor.
# 4. Nove to the 2nd example for more details of how classes can work together.