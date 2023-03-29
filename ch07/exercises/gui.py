class Weapon_Of_Mass_Destruction:
    def __init__(self, target, pnum=1):
        """
        Initialize the Weapon of Mass Destruction
        args: pnum [int] the weapon's id number, target [tuple] coordinates of target
        """
        self.wmd_num = pnum
        self.target = target
        self.hit_target = False

class Country:
    def __init__(self, location, corrupt=True, pnum=1):
        """
        Initialize the Country
        args: pnum [int] the country's id number, loaction [tuple] coordinates of location, corrupt [boolean] whether or not the country is corrupt
        """
        self.wmd_num = pnum
        self.target = location
        self.corrupt = corrupt
        self.hit_target = False

class Dog:
    def __init__(self, breed, age=0, happiness=100, domesticated=True, pnum=1,):
        """
        Initialize the Dog
        args: pnum [int] the dog's id number, breed [string] the breed of the dog, age [int] how old the dog is, happiness [int] how happy the dog is, domesticated [boolean] whether or not the dog is domesticated
        """
        self.wmd_num = pnum
        self.breed = breed
        self.age = age
        self.happiness = happiness
        self.domesticated = domesticated