class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am {}!".format(self.name))


name_input = Person(input())

name_input.greet()
