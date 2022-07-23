from weapon import Weapon

 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.
# (BONUS 5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

class Robot:

    def __init__(self, name, weapon_passed):         #UML doesn't include weapon parameter 
        self.name = name
        self.health = 100
        self.active_weapon = weapon_passed

    def attack(self, dinosaur):
        self.health -= dinosaur.attack_power


    