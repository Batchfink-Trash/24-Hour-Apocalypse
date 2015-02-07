import random

""" This module contains classes for all of the weapons useable in the game"""

class Crowbar(object):
    def stab():
        pass
    def swipe():
        pass

class bat(object):
    def smack():
        pass
    def jab():
        pass

class sword(object):
    def swipe():
        pass
    def stab():
        pass

class crossbow(object):
    ammo = 0
    def shoot():
        accuracy = random.randint(0, 5)
        return 5 * accuracy