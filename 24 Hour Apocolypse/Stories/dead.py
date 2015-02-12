import os
import sys
import random
from Utils import *


#This module contains everything for the "play-as-a-zombie" secret story :D

def grave():
    os.system("cls")
    print("You slowly rise out of the ground. You are a zombie.")
    input()
    os.system("cls")
    print("You really fancy eating some brain...")
    input()
    os.system("cls")

def singleSurvivor():
    name = generateName()
    os.system("cls")
    print("You stumble upon a young unsuspecting human, cowering in the corner of an alleyway.")
    input()
    os.system("cls")
    print("You slowly wander over to them, seeking their succulent human flesh and brains.")
    input()
    os.system("cls")
    print("You wouldn't even know who they are, that their name is " + name + " and that they lost their mother in a car accident. You wouldn't know that.")
    input()
    os.system("cls")
    print("Yet you continue to walk towards them. No morals, just one goal. Death.")
    input()
    os.system("cls")
    print("As you bite into their flesh, they scream a ear-piercing scream. You fulfil your taste.")
    input()
    os.system("cls")




def