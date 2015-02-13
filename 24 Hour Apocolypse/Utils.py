import time
import os
import sys
"""Misc methods"""

def generateName():
    names = ["Josh", "James", "Callum", "Edward", "Kyle", "Tom", "Joe", "Chris", "Isaac", "Sam", "Aaron", "Adam", "Clive", "Richard", "Robin", "Greg", "Harold", "Andre", "Daniel", "Lloyd", "Hugh", "Jake", "Jason", "Oscar", "Bradley", "Jack", "Matthew", "Jacob", "Austin", "Derek", "Sasha", "Sophie", "Samantha", "Maddy", "Sal", "Charlotte", "Paula", "Erin", "Josey", "Mila", "Kelly", "Jennifer", "Michelle", "Sydney", "Emily", "Nadia", "Daniella", "Carly", "Lydia", "Elizabeth", "Helen", "Lily", "Rebecca", "Abigail", "Beth", "Holly", "Grace"]
    genName = random.choice(names)
    return genName      #feel free to add names in the future

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
        time.sleep(0.25)

