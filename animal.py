class Animal:
    def __init__(self, name):
        self.name = name
        self.commands = []

    def add_commands(self, commands):
        self.commands.extend(commands)

    def get_commands(self):
        return self.commands

class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Hamster(Animal):
    pass


class Horse(Animal):
    pass


class Camel(Animal):
    pass


class Donkey(Animal):
    pass
