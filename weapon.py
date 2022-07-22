
# (5 points): As a developer, I want to choose from a List of 3 possible weapons before a robot makes an attack.

class Weapon:

    def __init__(self, name, attack_power_int):
        self.name = name
        self.attack_power = attack_power_int