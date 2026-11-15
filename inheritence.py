class Animal:                     # parent class
    def display(self):
        print("I am an animal.")

class Dog(Animal):                # child class — inherits from Animal
    pass

d = Dog()
d.display()   # Output: I am an animal.
# Dog defined nothing — it inherited display() from Animal

class Animal:                          # parent
    def __init__(self, name, habitat):
        self.name    = name
        self.habitat = habitat

    def display(self):
        print(f"Name: {self.name}  |  Habitat: {self.habitat}")

class Dog(Animal):                     # child
    def __init__(self, name, habitat, breed):
        self.breed = breed             # Dog-specific attribute
        # name and habitat still need to be set — see Topic 3

class Animal:
    def __init__(self, name, habitat):
        self.name    = name
        self.habitat = habitat

class Dog(Animal):
    def __init__(self, name, habitat, breed):
        Animal.__init__(self, name, habitat)  # call parent constructor
        self.breed = breed

d = Dog("Bruno", "Home", "Labrador")
print(d.name)    # Bruno   — set by Animal's __init__
print(d.breed)   # Labrador — set by Dog's __init__


class Animal:
    def __init__(self, name, habitat):
        self.name    = name
        self.habitat = habitat

class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)   # cleaner — no class name needed
        self.breed = breed

class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

from abc import ABC, abstractmethod

class Animal(ABC):             # Animal is now abstract
    def __init__(self, name, habitat):
        self.name    = name
        self.habitat = habitat

# a = Animal("x", "y")       # ERROR — cannot instantiate abstract class

class Dog(Animal):             # Dog is concrete — can be instantiated
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed


        
                