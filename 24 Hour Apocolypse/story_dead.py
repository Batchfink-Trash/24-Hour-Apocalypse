import os
import sys
import random
from Utils import *

#This module contains everything for the "play-as-a-zombie" secret story :D
#Note, this is an easter egg, so it is rather story based. No minigames to play, and if there are, they ain't too fancy :P

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

def game():
    os.system("cls")
    ans = input("You stumble upon a group of people. Do you want to attack them or lay low? (a/ll): ")
    if ans.lower() == "ll":
        os.system("cls")
        print ("You lay low, which was a good choice. These are veterans, they ain't gonna mess.")
        input()
        os.system("cls")
        ans = input("Attack now or move closer slowly? (a/m): ")
        if ans.lower() == "a":
            os.system("cls")
            print("Good choice. The unsuspecting leader now has no ring finger. Priceless.")
            input()
            os.system("cls")
            ans = input("Okay, now's your chance, attack or stand still and moan for no reason? (a/m): ")
            if ans.lower() == "a":
                os.system("cls")
                print ("Good! However, your journey has come to an end, as you are shot straight in the face.")
                input()
                #GAME OVER
            elif ans.lower() == "m":
                os.system("cls")
                print ("I er... don't know. You wander out mindlessly an are instantly shot in the leg, chest and face.")
                input()
                #GAME OVER
            else:
                os.system("cls")
                print ("Due to your incapability to type a usable answer, you wander aimlessly into a wall and are shot. At least you tried?")
                input()
                #GAME OVER
        elif ans.lower() == "m":
            os.system("cls")
            print ("You slowly move closer, but are noticed. Should've just went for it.")
            input()
            #GAME OVER
        else:
            os.system("cls")
            print ("Due to your incapability to type a usable answer, you wander aimlessly into a wall and are shot. At least you tried?")
            input()
            #GAME OVER
    elif ans.lower() == "a":
        os.system("cls")
        print("Good choice. The unsuspecting leader has lost his forearm flesh. Fantastic!")
        input()
        os.system("cls")
        ans = input("Okay, now's your chance, attack or stand still and moan for no reason? (a/m): ")
        if ans.lower() == "a":
            os.system("cls")
            print ("Good choice. However, your journey has come to an end, as you are shot straight in the face and chest.")
            input()
            #GAME OVER
        elif ans.lower() == "m":
            os.system("cls")
            print ("I err... can't explain that. You wander out mindlessly an are instantly shot in the face.")
            input()
            #GAME OVER
        else:
            os.system("cls")
            print ("Due to your incapability to type a usable answer, you wander aimlessly into a wall and are shot. At least you tried?")
            input()
            #GAME OVER
    else:
        os.system("cls")
        print ("Due to your incapability to type a usable answer, you wander aimlessly into a wall and are shot. At least you tried?")
        input()
        #GAME OVER
