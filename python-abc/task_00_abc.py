#!/usr/bin/python3
"""
Defines and abstract class Animal and 2 subclasses Dog and Cat
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that returns the sound of the animal
        """
        pass


class Dog(Animal):
    """
    Class Dog inheriting Animal
    """
    def sound(self):
        """
        Returns dog sound
        """
        return "Bark"


class Cat(Animal):
    """
    Class Cat inheriting Animal
    """
    def sound(self):
        """
        Returns cat sound
        """
        return "Meow"
