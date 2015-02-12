import Utils
import SetUp
import random

class Player(object):
    """The Player class. This holds all variables and methods ascociated with the player character"""

    def __init__(self, fore, sur, age, gender, health):
        self.fore = fore
        self.sur = sur
        self.name = self.fore + " " + self.sur
        self.age = int(age)
        self.gender = gender
        self.health = health
        if(self.age <= 2):
            self.bracket = "Baby"
        elif(self.age >= 3 and self.age <= 6):
            self.bracket = "Infant"
        elif(self.age >= 7 and self.age <= 18):
             self.bracket = "Child"
             self.timetable = []
        elif(self.age >= 19 and self.age <= 60):
            self.bracket = "Adult"
        elif(self.age >= 61 and self.age <= 120):
            self.bracket = "OAP"
        elif(self.age >= 121):
            self.bracket = "Dead"

    def describe(self):
        print("Name:      " + self.name)
        print("Age:       " + str(self.age))
        print("Gender:    " + self.gender)
        print("Age Group: " + self.bracket)
    
        def generateDay():
            lessons = ["maths", "english", "history", "pe", "science", "music", "geography"]
            lesson1 = lessons.pop(random.randint(0, 7))
            lesson2 = lessons.pop(random.randint(0, 7))
            lesson3 = lessons.pop(random.randint(0, 7))
            lesson4 = lessons.pop(random.randint(0, 7))
            lesson5 = lessons.pop(random.randint(0, 7))
            self.timetable += lesson1 + lesson2 + "break" + lesson3 + "lunch" + lesson4 + lesson5