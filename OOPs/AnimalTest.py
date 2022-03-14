from pythonClasses.Animal import Animal


class AnimalTest:
#creating dog object for the Animal class
    dog = Animal("scooby")
 #type returns the class name of the object dog
    print(type(dog))
    dog.set_animal_color("Brown")
    print(dog.name, "color is ", dog.get_animal_color())
