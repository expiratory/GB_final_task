from counter import Counter
from animal import Cat, Dog, Hamster, Horse, Camel, Donkey


class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.counter = Counter()

    def add_animal(self, animal):
        self.counter.add()
        self.animals.append(animal)

    def get_animal_class(self, animal):
        if isinstance(animal, Dog):
            return "Dog"
        elif isinstance(animal, Cat):
            return "Cat"
        elif isinstance(animal, Hamster):
            return "Hamster"
        elif isinstance(animal, Horse):
            return "Horse"
        elif isinstance(animal, Camel):
            return "Camel"
        elif isinstance(animal, Donkey):
            return "Donkey"
        else:
            return "Неизветсный класс животного"

    def show_commands(self, animal):
        animal_class = self.get_animal_class(animal)
        print(animal.get_commands())

    def teach_commands(self, animal, new_commands):
        animal_class = self.get_animal_class(animal)
        if animal_class != "Unknown":
            animal.add_commands(new_commands)

    def print_animals(self):
        for index, animal in enumerate(self.animals, 1):
            print(f"{index}. {animal.name} - {self.get_animal_class(animal)}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            raise Exception("Exception occurred or the resource was not properly closed.")