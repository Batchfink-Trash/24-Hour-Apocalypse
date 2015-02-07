import Player
import SetUp
from Utils import *
import pickle

SetUp.createCharacter()

player = pickle.load(open("player.p", "rb"))

print(player.age)