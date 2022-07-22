from dinosaur import Dinosaur
from battlefield import Battlefield
from weapon import Weapon
from robot import Robot


battlefield_one = Battlefield()
battlefield_one.run_game()

weapon_one = Weapon('Chainsaw Fingers', 15)

dino_one = Dinosaur('T-Rex', 35)
robot_one = Robot('Buzz')

robot_one.attack(dino_one)
print(dino_one.health)


