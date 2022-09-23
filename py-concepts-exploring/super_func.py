"""
Create a class that will inherit all the methods and properties from another class
"""


class Parent:

    def __init__(self, text):
        self.message = text

    def printMessage(self):
        print(self.message)


class Child(Parent):

    def __init__(self, txt):
        super().__init__(txt)


obj = Child("Johaar and Welcome!")

obj.printMessage()  # Leo: Since Child class inherits from Parent class, it has access to printMessage method

"""
Definition and Usage:
1) The super() function is used to give access to methods and properties of a parent or sibling class.
2) The super() function returns an OBJECT that represents the parent class.
"""