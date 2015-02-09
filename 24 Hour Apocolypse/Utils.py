import time
import os
"""Misc methods"""

def printUI(text, health, time, name):
     #TODO     maybe print name[:10] instead
     print("\n               Name: " + name + "  |  " + "Health: " + str(health) + "  |  " + "Time: " + time)
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
    print("\n")
    blankStr = ""
    for c in text:
        blankStr += " "
    titleSpace = "|- - - " + blankStr + " - - -|"
    for c in titleSpace:
        print(c, end="")
        time.sleep(0.25)
    time.sleep(0.5)
    os.system("cls")
    print("|- - - " + text + " - - -|")
