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

"""smack"""

class Rake(object):
    def smack():
        pass

class Broom(object):
    def smack():
        pass
    
class Shovel(object):
    def smack():
        pass
    
class Cane(object):
    def smack():
        pass

class Bat(object):
    def smack():
        pass

class Hammer(object):
    def smack():
        pass

class Sledgehammer(object):
    def smack():
        pass

"""stab"""

class pitchfork(object):
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

"""punch"""

class Box(object):
    def punch():
        pass

class Fist(object):
    def punch():
        pass

"""cut"""

class GardenShears(object):
    def cut():
        pass

"""ranged"""

class Handgun(object):
    ammo = 0
    def shoot():
        accuracy = random.randint(0, 3)
        return 3 * accuracy

class Crossbow(object):
    ammo = 0
    def shoot():
        accuracy = random.randint(0, 5)
        return 5 * accuracy

#ENTIRE NEW SET OF WEAPONS, POWER BASED

class CircularSaw(object):
    power = 0
    def cut():
        pass

""" 

This is a list of weapons to eventually do

These will be integrated with a location system which allows us to pick a random location within the story

For example, a locations.py file with def ArmyBase():  with a story following. This means that in the story / game.py we can pick a location for the player to arrive at and
allow them to find a weapon there. May want to consider renaming this to 24 Year apocalypse lol We ain't gonna fit all this story based stuff like these weapons into 24
hours, so I may have wasted my time. Either way, it doesn't really matter :D I HAD LOTS OF FUN FINDING THIS





AngleGrinder - Cut
ReciprocatingSaw - Stab / Cut
Chainsaw - Cut
Drill - Stab
Jackhammer (Small) - Stab
Jigsaw - Cut

Pickaxe - Swing
Mattock - Swing
Hoe - Swing
Turf Knife - Swing / Stab
Retriever - Swing
Claw rake - Swing
Nail Puller - Swing
Compost Fork - Stab
Brick-laying Trowel - smack / stab
Pointing trowel - stab
Gauging trowel - smack
Plastering Trowel - smack
Tiling Trowel - smack
Splitting Maul - Swing
brick hammer - Swing
drywall hammer - swing
Demolition Hammer - Swing
Carpenters Hatchet - Swing
Milled-face Hammer - swing
Roofing hammer - swing

Nail Gun - Ranged
Industrial stapler - Ranged

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


  SNIPER RIFLES


  PDSHP
  Barrett M82
  Barrett M99
  OSV-96
  JNG-90
  MSSR rifle





"""

# F*** me.  Do you want to kill us? YES