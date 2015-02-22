import Utils
import Player
import random

class Enemy(object):
    """ Where the zombies live """

    def __init__(self, health, strength, defence):
        self.health = health        # Up to 20
        self.strength = strength    # Up to 6
        self.defence = defence      # Up to 5
    
    def attack(self, player):
        damage = self.strength - player.defence
        event = random.randint(1, 4)
        if(event == 1):
            Utils.q("The Zombie swipes at you, knocking you back for %i health."%(damage), 0.2, player)
        elif(event == 2):
            Utils.q("The Zombie grabs you, taking %i health."%(damage), 0.2, player)
        elif(event == 3):
            Utils.q("The Zombie rips through your clothes and tears at your skin for %i damage"%(damage), 0.2, player)
        elif(event == 4):
            Utils.q("Biting down on your arm, a zombie takes %i health"%(damage), 0.2, player)
        return(damage)


