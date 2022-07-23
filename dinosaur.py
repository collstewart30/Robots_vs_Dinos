
# This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.
# (BONUS 5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        self.health -= robot.active_weapon.attack_power