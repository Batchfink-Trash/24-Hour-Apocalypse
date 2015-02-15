import Player
import SetUp
from Utils import *
import pickle
import TitleAnimation
from Stories import child
from Stories import adult

#TitleAnimation.animation()

with open("james.p", "rb") as f:
    player = pickle.load(f)

if player.bracket == "adult":
    randomm = randint(1,10)
    if randomm == 4:
        #weekend adult story
        None
    else:
        #normal adult story
        None


#player = pickle.load(open("player.p", "rb"))

#print(player.age)