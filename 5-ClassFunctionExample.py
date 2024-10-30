import random

# so lets talk about funcitons of a class...
# that is all they are, they are functions that are part of a class
# its really no different than a function outside, its just more organized and can use the class variables
# its generally a functions specific to the class, but it can be used outside of the class if you want... its just not good practice.


# for the health loss in the game, the the player is just taking in a object.. in this case the monster object
# then its targeting the health part of that object and subtracting the damage from it.
# just like a lot of other examples I gave. Its mostly just what your put INTO the function.

# so im going to build 2 classes here, and try to give an example that fully works.

# read these classses then look below for the example and explination.


class Student:
    def __init__(self, name):
        self.name = name

    def answer_question(self):
        return f"{self.name} says: 'The answer is 42!'"


class Teacher:
    def __init__(self, name):
        self.name = name

    def ask_question(self, student):
        print(f"{self.name} asks {student.name} a question.")
        response = student.answer_question()
        print(response)


# so we have 2 really small classes here.
# lets first look at the student. Its pretty simple, we take in a name in the init.

# remember, whatever is in the init,  when we CREATE the student that is everything the student has. and everything that the project has access to.

# but the student has a function too... that we can trigger.
# yes you can do it with something simple as..
# student.answer_question()
# but we are going to do it with the teacher class to show you HOW.

# so now lets look at the teacher.
# it has the name init... but in the ask question it is looking for a student object..... without a student object it wont know what to do.
# no just like my examples for functions, you CAN hard code that. right?
# teacherTest = Teacher("Mr. Johnson")
# teacherTest.ask_question("Bob")
# wrong. this gives you an error you can uncomment it and try it if you want.

# the reason is here...  print(f"{self.name} asks {student.name} a question.")
# this print statement is looking for a student.name. so it KNOWS the student is an object. (remember you can name this whatever you want)
# but because it has a .name or event if it had .health. it knows that it is an object.
# you can replace the input to say blorp and it would says blorp.name, and as long as you pass in the student object it will work.

# the naming structure is just to make it helpful as you build out your code.

# So if we changed that print statement to this....
# print(f"{self.name} asks {student} a question.")
# then doing
# teacherTest = Teacher("Mr. Johnson")
# teacherTest.ask_question("Bob")
# would work just fine.Because now it is just looking for a string. and any string with no object would work.

# so lets put it to prace and see how it works.
# lets createa  student and a teach object.
student = Student("Matt")
teacher = Teacher("Mr. DeVore")

# so here we have created 2 objects, a student and a teacher. set them to variables.
# so looking at this...
# student now contains a name of "Matt" and it can be asked a question.
# teacher now contains a name of "Mr. DeVore" and can ask a question.
teacher.ask_question(student)

# so when the teacher is asking the question, its passing in the ENTIRE student object(class).
# so spefically, the function inside teacher... which is what we say when we do teacher.askquestion.
# so looking at that function back in the class.. it is taking that object in... and  then using it.
# so this is an example of a string.... so lets create 2 new classes..... and see how we can use it with numbers.


class Bully:
    def __init__(self, name):
        self.name = name
        self.spankings = 0


class Principal:
    def __init__(self, name):
        self.name = name

    def spank(self, cat):
        cat.spankings += 1
        print(
            f"{self.name} spanks {cat.name} for being a bully. {cat.name} has now been spanked {cat.spankings} times."
        )


# so lets look at these classes...
# Bully is simple.  he has a name, and spankings.
# but he is only taking in the name, so when we create the bully. We only need to tell the class his name and he wil be created with 0 spankings.
# however...the spanking count is going to stay with the class forever after the is created... unless you hard code it. which I will show you later.

# so looking at the principal class.
# it is basically the same on the init. To create the class, all we need is the name.
# however, he has a function to take in an object. I called it cat. but it could be anything.
# i called it cat on purpose to show you that it can be anything.
# i think when you see these functions taking in obecects you arre thinking they are actually talking to the other class.. but they are not.
# the statements INSIDE the function are only whatever you call the input.

# so lets talk about about something confusing.
# how do we know its not an object?? (remember an object is basically another way of saying class)
# an obecjt is jsut anything that is more than 1 thing... so if your pasing in a string or a number its not an object.
# so the way you can tell is look at what the input for cat is...
# if it was a string, then it would not be cat.name, or cat.spanings. it would just be cat.
# same as if it were a number, if itwas cat.lives it would be an object, but if it was 1 + cat it woudl be an int.
# so the naming structure gives it away.
# i hate how python does this. in other languages you have to imply it in the input.
# like c# you would do something like functionName(string cat) or functionName(int cat) to tell it what it is.
# but python is more free form and you can do whatever you want, witch in a way can be confusing.

# so... lets go ahead and create the objects.
bully = Bully("Biily")
bully2 = Bully("Bobby")
principal = Principal("Mr. Monteith")

# so here, we created 3 objects (classes...objects = things with more than 1 thing in it.).2 bullys and principal.
# so before we write any logic... lets think about what is happening right here in our code.
# both of our bullies have 0 spankins... and lets print that to confirm it..
print(f"{bully.name} has been spanked {bully.spankings} times.")
print(f"{bully2.name} has been spanked {bully2.spankings} times.")

# so we are able to look at the object... directly....

# so... let the spankings begin.
principal.spank(bully)
# so here we call teh principal function that is for spank and pass in the object.... remeber we know its an object because it has a .name and .spanking
# therfor we need an object that has a .spanking and a .name... even though the function in principal is called cat, look atr this.. bully has a .spanking and a .name
# so we can pass in the bully object and it will work.
# so now lets print out the spankings to see what happened.
print(f"{bully.name} has been spanked {bully.spankings} times.")
print(f"{bully2.name} has been spanked {bully2.spankings} times.")
# so look at that... remember bully 1 and 2 are created above and re changed it with this function, so the spanking count.. even though it started a 0 is now 1.
# but bully 2 is still 0.
# lets change that a few times....
principal.spank(bully)
principal.spank(bully)
principal.spank(bully)
principal.spank(bully2)
principal.spank(bully2)
principal.spank(bully)
principal.spank(bully2)
# so looking at this... what do you think is happening?
# before you uncomment the print statements below... think about it.
# what is happening to the spankings for each bully?
# dont forget bully 1 already has 1 spanking before that slew of spankings.
# print(f"{bully.name} has been spanked {bully.spankings} times.")
# print(f"{bully2.name} has been spanked {bully2.spankings} times.")

# somethinf else to think about.... the spanking are hard coded to increase by 1 each time... but what if you wanted to change that?
# like.. a random number???
# so lets created it and see..


class Mean_Bully:
    def __init__(self, name):
        self.name = name
        self.spankings = 0


class Strong_Principal:
    def __init__(self, name):
        self.name = name

    def spank(self, bully):
        spankings = random.randint(1, 10)
        bully.spankings += spankings
        print(
            f"{self.name} spanks {bully.name} {spankings} times for being a bully. {bully.name} has now been spanked {bully.spankings} times."
        )


# so the only difference that i did here, was that I createda  spanking variable, assigned it to get a random number, then when we add to the spankings
# we add the variable to it....
# so lets create the objects and see how it works.
mean_bully = Mean_Bully("Matt")
mean_bully2 = Mean_Bully("Freddy")
strong_principal = Strong_Principal("Mr. DeVore")

# so the objects are created... now lets pring and show that they are indeed 0.
print(f"Inital: {mean_bully.name} has been spanked {mean_bully.spankings} times.")
print(f"Inital: {mean_bully2.name} has been spanked {mean_bully2.spankings} times.")

# so lets look really quick at the spank function in the principal class.
# see how there is a spankings variabke? and then there is a bully.spankings?
# the spanking variable in the function is just a number that getrs randomly genereated..
# so in the print statement, tere is that {spakings} and then there is a bully.spankings.
# the {spankingks} is going to show how many he gto spanked that time.
# but bully.spankings is going ot show that object total.

# so lets spank them a few times.
strong_principal.spank(mean_bully)
strong_principal.spank(mean_bully)
strong_principal.spank(mean_bully)
strong_principal.spank(mean_bully)
# so are you see ing how this is going to be helful if you want to do damange to a mosnster?
# once you create the monster, you have access to everything in the init....
# you just pass that into the funciton of the player....
#

# hopeflly this helps you understand how to use functions in a class.
