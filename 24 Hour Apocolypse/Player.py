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
        if(self.age >= 3 and self.age <= 10):
            self.bracket = "Infant"
        if(self.age >= 11 and self.age <= 18):
             self.bracket = "Child"
        elif(self.age >= 19 and self.age <= 60):
            self.bracket = "Adult"
        elif(self.age >= 61):
            self.bracket = "OAP"

    def describe(self):
        print("Name:      " + self.name)
        print("Age:       " + str(self.age))
        print("Gender:    " + self.gender)
        print("Age Group: " + self.bracket)
