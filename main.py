from animal_registry import AnimalRegistry
from animal import Cat, Dog, Hamster, Horse, Camel, Donkey


def main():
    with AnimalRegistry() as registry:
        while True:
            print("1. Add a new animal")
            print("2. Get animal's class and commands")
            print("3. Teach new commands")
            print("4. List all animals")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter the name of the animal: ")
                animal_type = input("Enter the type of the animal (Dog/Cat/Hamster/Horse/Camel/Donkey): ")
                if animal_type == "Dog":
                    animal = Dog(name)
                elif animal_type == "Cat":
                    animal = Cat(name)
                elif animal_type == "Hamster":
                    animal = Hamster(name)
                elif animal_type == "Horse":
                    animal = Horse(name)
                elif animal_type == "Camel":
                    animal = Camel(name)
                elif animal_type == "Donkey":
                    animal = Donkey(name)
                else:
                    print("Invalid animal type.")
                    continue

                registry.add_animal(animal)

            elif choice == "2":
                registry.print_animals()
                index = int(input("Enter the index of the animal: ")) - 1
                if 0 <= index < len(registry.animals):
                    animal = registry.animals[index]
                    print(f"Animal class: {registry.get_animal_class(animal)}")
                    registry.show_commands(animal)
                else:
                    print("Invalid index.")

            elif choice == "3":
                registry.print_animals()
                index = int(input("Enter the index of the animal: ")) - 1
                if 0 <= index < len(registry.animals):
                    animal = registry.animals[index]
                    new_commands = input("Enter new commands (comma-separated): ").split(',')
                    registry.teach_commands(animal, new_commands)
                else:
                    print("Invalid index.")

            elif choice == "4":
                registry.print_animals()

            elif choice == "5":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
