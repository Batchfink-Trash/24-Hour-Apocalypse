import Player
import Utils
import time
import os
import pickle

"""This class contains a method to set the game up -.- didn't need a whole module..."""

def createCharacter():
    """ This method provides an interface for creating the player character."""
    """ It uses this info to make a new instance of the player class"""

    os.system("cls")
    print("\n --- Create your character! --- ")
    time.sleep(0.5)
    firstname = input("\nForename: ")
    #character limiter, remove hashtags if it is a good idea :D
    #this sorts the UI out, as the UI will mess up if the name is too long :/
    #unless you can force the name to cut off the last few letters, like this:
    #firstname = firstname[:10]   (uses the first 10/9 letters of the str)

    #if len(firstname) > (10, 15, 20 etc.)
        #tell them it's bad or somethin'
    #else:
    surname = input("Surname: ")
    age = input("Age: ")
    gender = input("Gender (m/f): ")

    player = Player.Player(firstname, surname, age, gender, 20)

    Utils.loading()

    print("Is this you?")
    player.describe()
    ans = input("y/n ")
    if(ans.lower() == "y"):
       #Start game here

       #Dumping for use in other modules
       pickle.dump(player, open("player.p", "wb"))

       print("woop")
    elif(ans.lower() == "n"):
        print("\nAre you sure you want to remake your character?")
        ans = input("y/n ")
        if(ans.lower() == "y"):
            createCharacter()
        elif(ans.lower() == "n"):
            #Start game here
            #game.start or something
            pass
    else:
        print("nope")