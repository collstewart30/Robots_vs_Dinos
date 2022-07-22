from robot import Robot
from dinosaur import Dinosaur


# (10 points): As a developer, I want the battle to conclude once either the robot or the dinosaur has its health points reduced to zero.

# video example: robot attachs dino with weapon for x damage, dino has x health remaining
# then dino attacks robot for x damage, robot has x health remaining

class Battlefield:

    def __init__(self):
        self.Robot = ''
        self.Dinosaur = ''

    def run_game(self):
        pass

    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages!\nOnly one side can win!\n')    #this is the video example - change

    def battle_phase(self):
        pass

    def display_winner(self):
        if Robot(health) == 0:
            print('Dino wins!')
        if Dinosaur(health) == 0:
            print('Robot wins!')

