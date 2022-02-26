from pythonClasses.Animal import Animal


class AnimalTest:
    dog = Animal("scooby")
    print(type(dog))
    dog.set_animal_color("Brown")
    print(dog.name, "color is ", dog.get_animal_color())
