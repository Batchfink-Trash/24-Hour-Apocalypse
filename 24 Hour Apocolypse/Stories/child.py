from Utils import *
import SetUp
import sys
import random

""" This module contains all of the necessary methods for the child story """

def getUp():
    #START STORY
    pass

def goToSchool():
    # random transport
    pass

"""

def genSum():
        operations = ["+", "-", "*", "/"]
        operation = random.choice(operations)
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)
        return(str(num1) + " " + operation + " " + str(num2), operation)

"""

def maths():
    #FIXED IT. DON'T OVER COMPLICATE THINGS YOU SILLY MARE.
    print("\n\"Damn\", you thought.  \"It's maths.  I hate maths.\"  Quite rightly too, as you have a horrible teacher.  He makes no effort to explain the lesson and uses irritating colloquial terms, such as \"sweet\" and \"awesome!\".  This really grinds your gears")
    print("\nYou walk in.  Sir makes everyone stand behind their chairs as some sort of pointless punishment.  \"Good morning class\", he says.  You sit.")
    print("\nOn the table in front of you is a sheet of questions.  Thankfully, these are easier than usual.  No confusing algebra or \"Fastest finger first\", whatever that is.\n")
    
    score = 0
    questionsDone = 1
    
    for i in range(0, 5):
        operations = ["+", "-", "*", "/"]
        operation = random.choice(operations)
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)
        question = str(num1) + " " + operation + " " + str(num2)
        if operation == "+":
            print(str(questionsDone) + ". " + question, end="")                  
            ans = input(" = ")
            if(int(ans) == num1 + num2):
                print("\nCorrect!\n")
                score += 1
                questionsDone += 1
            else:
                print("\nWrong!\n")
                questionsDone += 1

        elif operation == "-":
            print(str(questionsDone) + ". " + question, end="")
            ans = input(" = ")
            if(int(ans) == num1 - num2):
                print("\nCorrect!\n")
                score += 1
                questionsDone += 1
            else:
                print("\nWrong!\n")
                questionsDone += 1

        elif operation == "*":
            print(str(questionsDone) + ". " + question, end="")
            ans = input(" = ")
            if(int(ans) == num1 * num2):
                print("\nCorrect!\n")
                score += 1
                questionsDone += 1
            else:
                print("\nWrong!\n")
                questionsDone += 1

        elif operation == "/":
            print(float(questionsDone) + ". " + question, end="")
            ans = input(" = ")
            if(ans == num1 / num2):
                print("\nCorrect!\n")
                score += 1
                questionsDone += 1
            else:
                print("\nWrong!\n")
                questionsDone += 1
    print("\nPhew, that was easy.  I scored " + str(score) + "/5.  Not bad!")
    print("\"Alright folks, sweet lesson today.  You can go\" Everyone ran to get out of the room.")


def english():
    #write essay, check if it contains certain words to pass
    pass

def history():
    #name dates?
    pass

def pe():
    #Hmmmm
    pass

def science():
    #symbol equations >.<
    pass

def music():
    #notes or name that tune with snacksound
    pass

def geography():
    #country quiz eg. capitals
    pass

def breakTime():
    #go to library or something.  "develop" story
    pass

def lunch():
    #eat food
    pass

def lastLesson():
    # "you walk out of <lesson name>" etc"
    #choose random mode of transport
    pass

def paperRound():
    #deliver papers to houses.  delivering when apocalypse starts
    pass

def sports():
    #Go to club or park
    pass

def friends():
    #Survive with friends!
    pass

def aftee():
    #haha, didn't do your homework
    pass