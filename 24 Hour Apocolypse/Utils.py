import time
import os
import sys
import random
"""Misc methods"""

def generateName(gender):                 
    names = ["Josh", "James", "Callum", "Edward", "Kyle", "Tom", "Joe", "Chris", "Isaac", "Sam", "Aaron", "Adam", "Clive", "Richard", "Robin", "Greg", "Harold", "Andre", "Daniel", "Lloyd", "Hugh", "Jake", "Jason", "Oscar", "Bradley", "Jack", "Matthew", "Jacob", "Austin", "Derek", "Sasha", "Sophie", "Samantha", "Maddy", "Sal", "Charlotte", "Paula", "Erin", "Josey", "Mila", "Kelly", "Jennifer", "Michelle", "Sydney", "Emily", "Nadia", "Daniella", "Carly", "Lydia", "Elizabeth", "Helen", "Lily", "Rebecca", "Abigail", "Beth", "Holly", "Grace"]
    guyNames = ["Josh", "James", "Callum", "Edward", "Kyle", "Tom", "Joe", "Chris", "Isaac", "Sam", "Aaron", "Adam", "Clive", "Richard", "Robin", "Greg", "Harold", "Andre", "Daniel", "Lloyd", "Hugh", "Jake", "Jason", "Oscar", "Bradley", "Jack", "Matthew", "Jacob", "Austin", "Derek"]
    girlNames = ["Sasha", "Sophie", "Samantha", "Maddy", "Sal", "Charlotte", "Paula", "Erin", "Josey", "Mila", "Kelly", "Jennifer", "Michelle", "Sydney", "Emily", "Nadia", "Daniella", "Carly", "Lydia", "Elizabeth", "Helen", "Lily", "Rebecca", "Abigail", "Beth", "Holly", "Grace"]
    if(gender == "m"):
        return random.choice(guyNames)
    elif(gender == "f"):
        return random.choice(girlNames)
    else:
        return random.choice(names)

def printUI(health, time, name):
     #TODO     maybe print name[:10] instead
     print("\n               Name: " + name + "  |  " + "Health: " + str(health) + "  |  " + "Time: " + time)
     print("--------------------------------------------------------------------------------")

def loading():
    os.system("cls")
    print("     |    ")
    print("Loading.")
    time.sleep(0.25)
    os.system("cls")
    print("     /    ")
    print("Loading..")
    time.sleep(0.25)
    os.system("cls")
    print("     -    ")
    print("Loading...")
    time.sleep(0.25)
    os.system("cls")
    print("     \    ")
    print("Loading.. ")
    time.sleep(0.25)
    os.system("cls")
    print("     |    ")
    print("Loading.")
    time.sleep(0.25)
    os.system("cls")

def animateTitle(text):
    titleSpace = "|- - - " + text + " - - -|"
    for c in titleSpace:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.05)

def credits():
    os.system("cls")
    line1 = "---------------------------------[GAME CREDITS]---------------------------------"
    for c in line1:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.02)
    print ("\n")
    line2 = "Programmers: James Mizen | Josh Johnson"
    for c in line2:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.02)
    print ("\n")
    line3 = "99% of the work: Josh Johnson - jk of course - 100% of the work: Josh Johnson"     # Piss off, you've just got too much spare time :P
    for c in line3:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.02)
    print ("\n")
    line4 = "etc. etc. cba finish later"
    for c in line4:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.02)
    input()