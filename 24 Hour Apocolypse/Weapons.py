import random
import Player

""" This module contains classes for all of the weapons useable in the game"""

""" List of all attack types for future reference:
    - Smack
    - Stab
    - Punch
    - Shoot
    
"""

##This may not be worth it, but is good for randomizing your choice in a story!:

"""
def randomWeapon():
    rw = random.randint(1, 10)
    if rw == 1:
        return 
"""

##Will fix later ^

#SWING

class Rake(object):
    def swing():
        pass

class Broom(object):
    def swing():
        pass
    
class Shovel(object):
    def swing():
        pass
    
class Cane(object):
    def swing():
        pass

class Bat(object):
    def swing():
        pass

class Hammer(object):
    def swing():
        pass

class Sledgehammer(object):
    def swing():
        pass

class Pickaxe(object):
    def swing():
        pass

class Mattock(object):
    def swing():
        pass

class Hoe(object):
    def swing():
        pass

class TurfKnife():
    def swing():
        pass

    def stab():
        pass

class Retriever(object):
    def swing():
        pass

class ClawRake(object):
    def swing():
        pass

class NailPuller(object):
    def swing():
        pass

class BrickHammer(object):
    def swing():
        pass

class BrickLayingTrowel(object):
    def swing():
        pass

    def stab():
        pass

class GaugingTrowel(object):
    def swing():
        pass

class PlasteringTrowel(object):
    def swing():
        pass

class TilingTrowel(object):
    def swing():
        pass

class SplittingMaul(object):
    def swing():
        pass

class BrickHammer(object):
    def swing():
        pass

class DrywallHammer(object):
    def swing():
        pass

class DemolitionHammer(object):
    def swing():
        pass

class CarpentersHatchet(object):
    def swing():
        pass

class MilledFaceHammer(object):
    def swing():
        pass

class RoofingHammer(object):
    def swing():
        pass

#STAB

class Pitchfork(object):
    def stab():
        pass

class Crowbar(object):
    def stab():
        pass

class Knife(object):
    def stab():
        pass

class Screwdriver(object):
    def stab():
        pass

class StanleyKnife(object):
    def stab():
        pass

class CompostFork(object):
    def stab():
        pass

class PointingTrowel(object):
    def stab():
        pass

#PUNCH

class Box(object):
    def punch():
        pass

class Fist(object):
    def punch():
        pass

#CUT

class GardenShears(object):
    def cut():
        pass

#---------------
#GUNS AND RANGED
#---------------


##----------GUNS

#PISTOLS

class Pistol(object):
    MAXAMMO = 0
    def __init__(self, ammo):
        if(ammo <= self.MAXAMMO):
            self.ammo = ammo
    def attack(self):
        self.shoot()        # <--- Use weapon.attack in the story to cater for non gun based weapons
    def shoot(self):
        if(ammo > 0):
            accuracy = random.randint(0, 3)
            return 3 * accuracy
            ammo -= 1
        else:
            print("No ammo")

class ColtM1911(Pistol):
    MAXAMMO = 7
    def __init__(self, ammo):
        self.ammo = ammo

class BerettaM9(Pistol):
    MAXAMMO = 15
    def __init__(self, ammo):
        self.ammo = ammo

class Beretta70(Pistol):
    MAXAMMO = 10
    def __init__(self, ammo):
        self.ammo = ammo

class DesertEagle(Pistol):
    MAXAMMO = 7
    def __init__(self, ammo):
        self.ammo = ammo

class Fort12(Pistol):
    MAXAMMO = 12
    def __init__(self, ammo):
        self.ammo = ammo

class Glock19(Pistol):                                      #YES THESE ARE ACTUAL MAX MAGAZINE CAPACITIES
    MAXAMMO = 15
    def __init__(self, ammo):
        self.ammo = ammo

class Glock35(Pistol):
    MAXAMMO = 17
    def __init__(self, ammo):
        self.ammo = ammo

class P30(Pistol):
    MAXAMMO = 15
    def __init__(self, ammo):
        self.ammo = ammo

class Horhe(Pistol):
    MAXAMMO = 10
    def __init__(self, ammo):
        self.ammo = ammo

class SIGP220(Pistol):
    MAXAMMO = 6
    def __init__(self, ammo):
        self.ammo = ammo

class SIGP229(Pistol):
    MAXAMMO = 8
    def __init__(self, ammo):
        self.ammo = ammo

class TanfoglioForce(Pistol):
    MAXAMMO = 9
    def __init__(self, ammo):
        self.ammo = ammo

#MACHINE GUNS











##----------MISC RANGED

class Crossbow(object):
    ammo = 0
    def shoot():
        accuracy = random.randint(0, 5)
        return 5 * accuracy

class NailGun(object):
    nails = 0
    def shoot():
        accuracy = random.randint(0,7)
        return 7 * accuracy

class BlowTorch(object):
    gas = 132 #out of 2000 to 10000
    def torch():
        pass

#|--------------------------------------|
#|ENTIRE NEW SET OF WEAPONS, POWER BASED|
#|--------------------------------------|

class CircularSaw(object):
    power = 0
    def cut():
        pass

class AngleGrinder(object):
    power = 0
    def cut():
        pass

class ReciprocatingSaw(object):
    power = 0
    def stab():
        pass

    def cut():
        pass

class ChainSaw(object):
    power = 0
    def cut():
        pass

class Drill(object):
    power = 0
    def stab():
        pass

class Jackhammer(object):
    power = 0
    def stab():
        pass

class JigSaw(object):
    power = 0
    def cut():
        pass

""" 

This is a list of weapons to eventually do

These will be integrated with a location system which allows us to pick a random location within the story

For example, a locations.py file with def ArmyBase():  with a story following. This means that in the story / game.py we can pick a location for the player to arrive at and
allow them to find a weapon there. May want to consider renaming this to 24 Year apocalypse lol We ain't gonna fit all this story based stuff like these weapons into 24
hours, so I may have wasted my time. Either way, it doesn't really matter :D I HAD LOTS OF FUN FINDING THIS

Blow torch - Gas (fuel) - Ranged / very close to the face of the thing yeah :D


   _____                 
  / ____|                
 | |  __ _   _ _ __  ___ 
 | | |_ | | | | '_ \/ __|                  
 | |__| | |_| | | | \__ \
  \_____|\__,_|_| |_|___/


  PISTOLS


  Beretta M9
  Beretta 70
  Colt M1911
  Desert Eagle
  Fort 12
  Glock 19
  Glock 35
  Heckler & Koch P30     
  Horhe                  
  SIG P220
  SIG P229
  Tanfoglio Force


  MACHINE GUNS


  MG 30
  Daewoo K3
  Heckler & Koch MG4
  Mark 48 machine gun
  UKM-2000
  QGF 20-D4 MG (made up, 1 of 3 "super guns")


  SUBMACHINE GUNS


  Kel-Tec PLR-16
  Zastava Master FLG
  UMP
  Lusa submachine gun
  Daewoo Precision Industries K1
  MP5
  Uzi
  Sterling submachine gun


  SHOTGUNS


  KSG
  Vepr-12
  Armsel Striker
  USAS-12
  Model 1200
  Model 1100
  Model 1912
  Model 11
  Model 11-48
  Mossberg 500
  Double-barreled shotgun
  SpaZ-141 (made up)


  SNIPER RIFLES


  PDSHP
  Barrett M82
  Barrett M99
  OSV-96
  JNG-90
  MSSR rifle
  PlasmaR (made up)





"""

# F*** me.  Do you want to kill us? YES
# Welp, I appoint you head kill-y weapon man.
