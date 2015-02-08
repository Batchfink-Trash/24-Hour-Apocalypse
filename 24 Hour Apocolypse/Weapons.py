import random

""" This module contains classes for all of the weapons useable in the game"""

""" List of all attack types for future reference:
    - Smack
    - Stab
    - Push
    - Shoot
    
"""
    
class Rake(object):
    def smack():
        pass

class Broom(object):
    def smack():
        pass
    
class GardenFork(object):
    def stab():
        pass
    
class Shovel(object):
    def smack():
        pass
    
class Box(object):
    def push():
        pass

class Handgun(object):
    ammo = 0
    def shoot():
        accuracy = random.randint(0, 3)
        return 3 * accuracy

class Cane(object):
    def smack():
        pass

class Crowbar(object):
    def stab():
        pass

class Bat(object):
    def smack():
        pass

class Knife(object):
    def stab():
        pass

class Crossbow(object):
    ammo = 0
    def shoot():
        accuracy = random.randint(0, 5)
        return 5 * accuracy
