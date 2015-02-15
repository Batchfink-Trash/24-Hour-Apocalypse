import Utils
import SetUp
import random
import Weapons

class Player(object):
    """The Player class. This holds all variables and methods ascociated with the player character"""

    #TODO Add time for loading and saving games

    def __init__(self, fore, sur, age, gender, health):       #The weapon thing ballsed me up. I fixed it
        self.fore = fore
        self.sur = sur
        self.name = self.fore + " " + self.sur
        self.age = int(age)
        self.gender = gender
        self.health = health
        self.weapon = Weapons.Fist()
        if(self.age <= 2):
            self.bracket = "Baby"
        elif(self.age >= 3 and self.age <= 6):
            self.bracket = "Infant"
        elif(self.age >= 7 and self.age <= 18):
             self.bracket = "Child"
             self.timetable = []
             self.timetable = self.generateDay(self.timetable)
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
    
    def generateDay(self, timetable):
        lessons = ["maths", "english", "history", "pe", "science", "music", "geography"]
        lesson1 = lessons.pop(random.randint(0, 6))
        lesson2 = lessons.pop(random.randint(0, 5))
        lesson3 = lessons.pop(random.randint(0, 4))
        lesson4 = lessons.pop(random.randint(0, 3))
        lesson5 = lessons.pop(random.randint(0, 2))
        timetable.append(lesson1)
        timetable.append(lesson2)
        timetable.append("break")
        timetable.append(lesson3)
        timetable.append("lunch")
        timetable.append(lesson4)
        timetable.append(lesson5)
        return timetable