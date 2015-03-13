# Another important aspect of Python classes is scope. The scope of a variable is the context in which it's visible to the program.

# It may surprise you to learn that not all variables are accessible to all parts of a Python program at all times. When dealing with classes, you can have variables that are available everywhere (global variables), variables that are only available to members of a certain class (member variables), and variables that are only available to particular instances of a class (instance variables).

# The same goes for functions: some are available everywhere, some are only available to members of a certain class, and still others are only available to particular instance objects.

# Instructions
# Check out the code in the editor. Note that each individual animal gets its own name and age (since they're all initialized individually), but they all have access to the member variable is_alive, since they're all members of the Animal class. Click Save & Submit Code to see the output!

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Hippo",3)
hippo.description()

sloth = Animal("Sloth", 4)
ocelot = Animal("Ocelot", 3)

print hippo.health
print sloth.health
print ocelot.health

