from operator import truediv
from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon


# video example: robot attacks dino with weapon for x damage, dino has x health remaining
# then dino attacks robot for x damage, robot has x health remaining

class Battlefield:
    
    def __init__(self):
        self.robot = Robot('Robob')
        self.dinosaur = Dinosaur('Rex', 35)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()


# (10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# (10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield.

    def display_welcome(self):
        print("")
        print("The battle we've all been waiting for: Robots vs Dinosaurs! Who will claim victory?")    #this is the video example - change
        print("")

    def battle_phase(self):
        print(f"{self.robot.name}'s starting health: {self.robot.health}")
        print(f"{self.dinosaur.name}'s starting health: {self.dinosaur.health}")
        print("")

        while self.robot.health >= 0 and self.dinosaur.health >= 0:
            self.robot.attack(self.dinosaur)
            print(f'{self.dinosaur.name} attacked {self.robot.name} with attack power of {self.dinosaur.attack_power}!')
            print("")

            self.dinosaur.attack(self.robot)
            print(f'{self.robot.name} attacked {self.dinosaur.name} with {self.robot.active_weapon.name} with attack power of {self.robot.active_weapon.attack_power}!')
            print("")

            if self.robot.health <0 or self.dinosaur.health <0:
                self.display_winner
            else:
                print(f"{self.robot.name}'s current health: {self.robot.health}")
                print(f"{self.dinosaur.name}'s current health: {self.dinosaur.health}")
            
        

    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} wins!')
        elif self.dinosaur.health <= 0:
            print(f'{self.robot.name} wins!')
            
# (10 points): As a developer, I want the battle to conclude once either the robot or the dinosaur has its health points reduced to zero.

