#!/usr/bin/python3
"""
Defines classes for Fish, Bird, and FlyingFish with their behaviors
"""


class Fish:
    """
    Represents a fish with swimming behavior and habitat
    """
    def swim(self):
        """
        Behavior for fish
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Habitat for fish"""
        print("The fish lives in water")


class Bird:
    """
    Represents a bird with flying behavior and habitat
    """
    def fly(self):
        """
        Behavior for bird
        """
        print("The bird is flying")

    def habitat(self):
        """
        Habitat for bird
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish that can both swim and fly, with its habitat
    """
    def swim(self):
        """
        Behavior for flying fish
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Behavior for flying fish
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Habitat for flying fish
        """
        print("The flying fish lives both in water and the sky!")
