import time
import os
import sys
import random
"""Misc methods"""


def generateName(gender):                 
    names = ["Josh", "James", "Callum", "Edward", "Kyle", "Tom", "Joe", "Chris", "Isaac", "Sam", "Aaron", "Adam", "Clive", "Richard", "Robin", "Greg", "Harold", "Andre", "Daniel", "Lloyd", "Hugh", "Jake", "Jason", "Oscar", "Bradley", "Jack", "Matthew", "Jacob" , "Austin", "Derek", "Sasha", "Sophie", "Samantha", "Maddy", "Sal", "Charlotte", "Paula", "Erin", "Josey", "Mila", "Kelly", "Jennifer", "Michelle", "Sydney", "Emily", "Nadia", "Daniella", "Carly", "Lydia", "Elizabeth", "Helen", "Lily", "Rebecca", "Abigail", "Beth", "Holly", "Grace"]
    guyNames = ["Josh", "James", "Callum", "Edward", "Kyle", "Tom", "Joe", "Chris", "Isaac", "Sam", "Aaron", "Adam", "Clive", "Richard", "Robin", "Greg", "Harold", "Andre", "Daniel", "Lloyd", "Hugh", "Jake", "Jason", "Oscar", "Bradley", "Jack", "Matthew", "Jacob", "Austin", "Derek"]
    girlNames = ["Sasha", "Sophie", "Samantha", "Maddy", "Sal", "Charlotte", "Paula", "Erin", "Josey", "Mila", "Kelly", "Jennifer", "Michelle", "Sydney", "Emily", "Nadia", "Daniella", "Carly", "Lydia", "Elizabeth", "Helen", "Lily", "Rebecca", "Abigail", "Beth", "Holly", "Grace"]
    if(gender == "m"):
        return random.choice(guyNames)
    elif(gender == "f"):
        return random.choice(girlNames)
    else:
        return random.choice(names)

def printUI(health, time, name, player):
     #TODO     maybe print name[:10] instead
     
     print ("NAME: " + name + "  |  " + "HEALTH: " + str(health) + "  |  " + "TIME: " + time)
     print ("--------------------------------------------------------------------------------")
     print ("\n\nINVENTORY:")
     inv = player.inventory
     pocket = str(inv["Pocket"])
     bag = str(inv["Bag"])
     if pocket == "[]":
         pocket = "Empty"
     if bag == "[]":
         bag = "Empty"
     for c in ["{", ":", "[", "]", "}", "'"]: 
         if c in pocket:            #removing unnecessary stuff like {'s and :'s
             pocket = pocket.replace(c, "")
     for c in ["{", ":", "[", "]", "}", "'"]: 
         if c in bag:           
             bag = bag.replace(c, "")
     print ("Bag: " + str(bag) + "\nPocket: " + str(pocket))   #Note, does keep python format, but looks good either way, so I kept it. Try it out!
     print ("--------------------------------------------------------------------------------")

     #Bag: Empty
     #Pocket: Rubber bands, String  etc.


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
        time.sleep(0.03)

def credits():
    os.system("cls")
    line1 = "---------------------------------[GAME CREDITS]---------------------------------"
    for c in line1:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    print ("\n")
    line2 = "[Lead Programmer]\n"
    for c in line2:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    line3 = "James Mizen"
    for c in line3:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    print ("\n")
    line4 = "[Programmers]\n"
    for c in line4:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    line5 = "Josh Johnson\n"
    for c in line5:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    line6 = "James Mizen"
    for c in line6:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")
    line7 = "[Lead Writer]\n"
    for c in line7:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    line8 = "Josh Johnson"
    for c in line8:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    print ("\n")
    line9 = "[Writers]\n"
    for c in line9:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    line10 = "James Mizen\n"
    for c in line10:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    line11 = "Josh Johnson"
    for c in line11:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    print ("\n\n")
    line8 = "--------------------------------[SEPCIAL THANKS]--------------------------------"
    for c in line8:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)
    print ("\n")
    #Whoever:
    line11 = "LIST ALL TESTERS HERE"
    for c in line11:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.04)

def q(text, speed, player):
    #if len(text) > 80:
        #make it split the line onto two
        #then do the below code for all of it :D
    printUI(player.health, "12:14", player.name, player)
    for c in text:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(speed)