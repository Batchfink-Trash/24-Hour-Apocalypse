import Player
import SetUp
from Utils import *
import TitleAnimation
import os
import SaveLoad
import Weapons
import story_child

player = SetUp.createCharacter()

SaveLoad.saveGame(player)

#Check out mah sweet inventorah system! Works too!


# VVVV Sorts out the timetable
for i in player.timetable:
    # I would really like a switch here...
    if(i == "maths"):
        story_child.maths(player)
    elif(i == "english"):
        story_child.english(player)
    elif(i == "history"):
        story_child.history(player)
    elif(i == "pe"):
        story_child.pe(player)
    elif(i == "science"):
        story_child.science(player)
    elif(i == "music"):
        story_child.music(player)
    elif(i == "geography"):
        story_child.geography(player)
    elif(i == "break"):
        story_child.breakTime(player)
    elif(i == "lunch"):
        story_child.lunch(player)


'''
if player.bracket == "adult":
    randomm = randint(1,10)
    if randomm == 4:
        #weekend adult story    <--- Too much work -.-
        None
    else:
        #normal adult story
        None
        '''