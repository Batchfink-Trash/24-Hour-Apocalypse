import Player
import pickle
import os
import time

""" A module for saving and loading games.  Currently there are only 3 save files, but this could be expended upon """
#USAGE
#To Save:
#player = SetUp.createCharacter()
#SaveLoad.saveGame(player)

#To Load:
#player = SaveLoad.loadGame() 


def saveGame(player):
    os.system("cls")
    print("Which game do you want to save to?")
    files = []
    filepaths = []
    root = os.getcwd()
    for(dirpath, dirnames, filenames) in os.walk(root):
        for filename in filenames:
            if(filename[-4:] == ".dat"):
                files.append(filename)
                filepaths.append(os.sep.join([dirpath, filename]))
    
    count = 1
    for f in files:
        print(str(count) + ". " + f)
        count += 1
    saveno = input()
    if(saveno == "1"):
        saveFile = filepaths[0]
    elif(saveno == "2"):
         saveFile = filepaths[1]
    elif(saveno == "3"):
        saveFile = filepaths[2]
    
    with open(saveFile, "wb") as f:
        pickle.dump(player, f)
    time.sleep(0.5)
    input("\nDone!  Press any key to continue...")


def loadGame():
    os.system("cls")
    print("Which game do you want to load?")
    files = []
    filepaths = []
    root = os.getcwd()
    for(dirpath, dirnames, filenames) in os.walk(root):
        for filename in filenames:
            if(filename[-4:] == ".dat"):
                files.append(filename)
                filepaths.append(os.sep.join([dirpath, filename]))
    
    count = 1
    for f in files:
        print(str(count) + ". " + f)
        count += 1
    saveno = input()
    if(saveno == "1"):
        saveFile = filepaths[0]
    elif(saveno == "2"):
         saveFile = filepaths[1]
    elif(saveno == "3"):
        saveFile = filepaths[2]
    
    with open(saveFile, "rb") as f:
        # Use player = loadGame()
        return pickle.load(f)
    time.sleep(0.5)
    input("\nDone!  Press any key to continue...")


    # I freaking salute you Sir Mizen, you certainly are a special child.