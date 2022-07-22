from dinosaur import Dinosaur
from weapon import Weapon

# (10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.
# (BONUS 5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

class Robot:

    def __init__(self, name):       
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()

    def attack(self, dinosaur):
        self.health -= dinosaur.health


    