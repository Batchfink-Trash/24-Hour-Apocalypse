import Utils
import SetUp

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
