import Player
import Utils
import time
import os
import pickle

"""This module contains a method to set the game up -.- didn't need a whole module..."""

def createCharacter():
    """ This method provides an interface for creating the player character."""
    """ It uses this info to make a new instance of the player class"""

    os.system("cls")
    Utils.animateTitle("Create your character!")
    time.sleep(0.5)
    firstname = input("\nForename: ")
    firstname = firstname[:8]
    surname = input("Surname: ")
    surname = surname[:12]
    age = input("Age: ")
    gender = input("Gender (m/f): ")

    player = Player.Player(firstname, surname, age, gender, 20)

    Utils.loading()

    print("Is this you?")
    player.describe()
    ans = input("Y/N: ")
    if(ans.lower() == "y"):
        return(player)
        #don't need a game.start, cos you just returned player, see game.py
    elif(ans.lower() == "n"):
        print("\nAre you sure you want to remake your character?")
        ans = input("Y/N: ")
        if(ans.lower() == "y"):
            createCharacter()
        elif(ans.lower() == "n"):
            return (player)
            #see game.py
            pass
    else:
        print ("Assuming you are ready...")
        time.sleep(1)
        return(player)
        #buggers have to learn!!!!!