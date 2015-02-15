""" The story line for an adult. """

import os
import random
from Utils import *
import time
import datetime
import Player
import Weapons

def weekend(player):
    os.system("cls")
    print ("As your eyes slowly open, you drift in and out of consciousness, wishing for yourself to fall back asleep.")
    input()
    os.system("cls")
    print ("You look towards your clock, it reads 8:30. 8:30 is not your usual awakening time.")
    input()
    os.system("cls")
    print ("Upon further inspection, you notice that it's the weekend. You slept all through Friday. Wierd.")
    input()
    os.system("cls")
    print ("You vaguely remember the smashing party you had, and how drunk you'd gotten.")
    input()
    os.system("cls")
    print ("After sliding out of bed, you put on a shirt and walk into the kitchen.")
    input()
    os.system("cls")
    print ("Here, it comes to your attention that somebody is knocking on the door. And has been for the last 4 minutes.")
    input()
    os.system("cls")
    print ("You decide to answer them, but at 8:30 in the morning, they could just be someone drunk.")
    input()
    os.system("cls")
    print ("You peer through your peep hole. You see a tall male, with a... deformed face.")
    input()
    os.system("cls")
    print ("\"Nice makeup!\" You shout through the door. No response.")
    input()
    os.system("cls")
    print ("You turn around after locking the door. The banging resumes.")
    input()
    os.system("cls")
    if player.gender == "f":
        print ("You decide to get changed, so you take off your shirt and put on a bra, a jacket and a skirt.")
    elif player.gender == "m":
        print ("You decide to get changed, so you take off your shirt and put on some underwear, a jumper and a pair of jeans.")
    else:
        print ("You decide to get changed, so you take off your shirt and put on a bra, some underwear, a skirt and a pair of jeans.")  # xD   if this is possible I s'pose
    input()
    os.system("cls")
    print ("*CRASH*")
    input()
    os.system("cls")
    print("You sprint towards your door, and see a mass of \'people\' barging into your apartment.")
    input()
    os.system("cls")
    print("Being on the 15th floor means windows aren't an option, so you sprint to the closet to grab a weapon")
    input()
    os.system("cls")
    print ("You see a bunch of possible weapons.")
    input()
    print ("1. A broom")
    input()
    print ("2. A crowbar")
    input()
    print ("3. A plastic box")
    input()
    print ("4. A hammer")
    input()
    weaponPicked = str(input("Choose (number): "))
    if weaponPicked == "1":
        player.weapon = Weapons.Broom()
    elif weaponPicked == "2":
        player.weapon = Weapons.Crowbar()
    elif weaponPicked == "3":
        player.weapon = Weapons.Box()
    elif weaponPicked == "4":
        player.weapon = Weapons.Hammer()

