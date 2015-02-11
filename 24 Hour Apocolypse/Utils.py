import time
import os
import sys
"""Misc methods"""



""" time variables to be edited within the game """

minute = 01
hour = 7
wtime = hour + ":" + minute + ":"   #wtime = world time          access using Utils.wtime :D

""" end of time variables """



def printUI(text, health, time, name):
     #TODO     maybe print name[:10] instead
     print("\n               Name: " + name + "  |  " + "Health: " + str(health) + "  |  " + "Time: " + wtime)
     print("--------------------------------------------------------------------------------")
     print(text)


def loading():
    os.system("cls")
    print("     |    ")
    print("Loading...")
    time.sleep(0.25)
    os.system("cls")
    print("     /    ")
    print("Loading ..")
    time.sleep(0.25)
    os.system("cls")
    print("     -    ")
    print("Loading. .")
    time.sleep(0.25)
    os.system("cls")
    print("     \    ")
    print("Loading.. ")
    time.sleep(0.25)
    os.system("cls")
    print("     |    ")
    print("Loading...")
    time.sleep(0.25)
    os.system("cls")

def animateTitle(text):
    titleSpace = "|- - - " + text + " - - -|"
    for c in titleSpace:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.25)

