import abc
from abc import ABC


class Dog(ABC):
    all_dog_count = 0
    per_breed_count = 0

    def __init__(self, name="unknown"):
        self.name = name
        self.__class__.per_breed_count += 1
        Dog.all_dog_count += 1

    @abc.abstractmethod
    def greet(self):
        pass

    def sleep(self):
        return "zzz"

    @classmethod
    def get_all_dog_count(cls):
        return cls.all_dog_count

    @classmethod
    def get_breed_count(cls):
        return cls.per_breed_count


class Puggle(Dog):

    def __str__(self):
        return f"Puggle named {self.name}"

    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"

    @staticmethod
    def get_characteristics():
        return "Like a mini boxer"


class Boxer(Dog):

    def __str__(self):
        return f"Boxer named {self.name}"

    def greet(self):
        return f"The name's {self.name}. Pleasure."

    @staticmethod
    def get_characteristics():
        return "Boxers are lovers, not fighters."
