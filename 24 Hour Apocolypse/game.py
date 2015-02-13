import Player
import SetUp
from Utils import *
import pickle
import TitleAnimation
from Stories import child

#TitleAnimation.animation()

with open("james.p", "rb") as f:
    player = pickle.load(f)

child.lunch(player)


#player = pickle.load(open("player.p", "rb"))

#print(player.age)