from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon


# video example: robot attacks dino with weapon for x damage, dino has x health remaining
# then dino attacks robot for x damage, robot has x health remaining

class Battlefield:
    
    def __init__(self):
        self.robot = Robot('T-Rex')
        self.dinosaur = Dinosaur('Buzz', 35)

    def run_game(self):
        self.display_welcome
        self.battle_phase
        self.display_winner
                       

# (10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# (10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield.

    def display_welcome(self):
        print("")
        print("The battle we've all been waiting for: Robots vs Dinosaurs! Who will claim victory?")    #this is the video example - change
        print("")

    def battle_phase(self):
       
        while self.robot.health or self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            print(f"{self.dinosaur.name}'s current health: {self.dinosaur.health}")
            self.dinosaur.attack(self.robot)
            print(f"{self.robot.name}'s current health: {self.robot.health}")
        else:
            self.display_winner
        

    def display_winner(self):
        if self.robot.health == 0:
            print(f'{self.dinosaur.name} wins!')
        if self.dinosaurinosaur.health == 0:
            print(f'{self.robot.name} wins!')
# (10 points): As a developer, I want the battle to conclude once either the robot or the dinosaur has its health points reduced to zero.

