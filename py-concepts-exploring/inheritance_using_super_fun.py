"""
An example to show how super() function is used to implement multiple inheritance
Leo's naming convention:
i) class name starts with Caps, and can be camel case if there are more than one words
"""


class Animal:

    def __init__(self, animal_name):
        print(animal_name, "is an animal.")


# Mammal inherits Animal
class Mammal(Animal):

    def __init__(self, mammal_name):
        print(mammal_name, "is a mammal.")
        super().__init__(mammal_name)  # Leo: no 'self' in __init__ while using with super()


# CannotFly inherits Mammal
class CannotFly(Mammal):

    def __init__(self, mammal_that_cant_fly):
        print(mammal_that_cant_fly, "can't fly.")
        super().__init__(mammal_that_cant_fly)


# CannotSwim inherits Mammal
class CannotSwim(Mammal):

    def __init__(self, mammal_that_cant_swim):
        print(mammal_that_cant_swim, "can't swim")
        super().__init__(mammal_that_cant_swim)


# Cat inherits CannotSwim and CannotFly
class Cat(CannotSwim, CannotFly):

    def __init__(self):
        print("I'm a cat.")
        super().__init__("Cat")


# Driver Code
cat_obj = Cat()
print(" ")

bat_obj = CannotSwim("Bat")
