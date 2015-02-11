import Player
import SetUp
from Utils import *
import pickle
import TitleAnimation
from Stories import child

TitleAnimation.animation()

SetUp.createCharacter()

"""
Possibly how the system would work?


if Player.bracket == "Child":
    child.getUp()
    child.goToSchool()
    lessons = ["Pe","Geography","History","English","Maths","Music","Science"]
    #choose lessons
    #for sake of player, only three lessons
    child.lessonchose
    #break whatevs
    #after school
    #zombie pocalypse
    
"""





#player = pickle.load(open("player.p", "rb"))

#print(player.age)