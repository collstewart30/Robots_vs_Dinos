from robot import Robot

# (10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.
# (5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

class Dinosaur:

    def __init__(self, name, attack_power_int):
        self.name = name
        self.attack_power = attack_power_int
        self.health = 0

    def attack(self, robot):
        self.attack_robot -= Robot.health