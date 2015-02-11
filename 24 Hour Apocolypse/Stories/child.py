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
        operations = ["+", "-", "*"]
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
    print("\nPhew, that was easy.  I scored " + str(score) + "/5.  Not bad!")
    print("\"Alright folks, sweet lesson today.  You can go\" Everyone ran to get out of the room.")


def english():
    print("\"Alright folks, settle down now, just got to wait for the computer to log on,\" is the usual greeting.")
    print("We grab our books and a sheet with a question on it and sit. Another question based sheet. Great.")
    print ("\"Explane deeply wat is wrang wit this sentnce...\" Wow.")
    
    marks = 0
    ans = input("1. ")
    
    if ans.lower().find("explain") != -1:
        marks += 1
    if ans.lower().find("what") != -1:
        marks += 1
    if ans.lower().find("wrong") != -1:
        marks += 1
    if ans.lower().find("with") != -1:
        marks += 1
    if ans.lower().find("sentence") != -1:
        marks += 1
    print ("\"Alright folks, next on the list is " + Player.fore + ", so, " + Player.fore + ", you ended up with " + str(marks) + "/5. Well done " + Player.fore + "!\" Thanks sir. Thanks.")
        
def history():
    #name dates
    pass

def pe():
    #Hmmmm
    pass

def science():
    print("\nTime for Science!  You walk into the chemistry classroom, hoping for a practical lesson. However, you never do practicals in chemistry, what are you talking about! even so, anything is better than physics.")
    elements = {"Hydrogen":"h","Helium":"he","Lithium":"li","Beryllium":"be","Boron":"b","Carbon":"c","Nitrogen":"n","Oxygen":"o","Fluorine":"f","Neon":"ne","Sodium":"na","Magnesium":"mg","Aluminium":"al","Silicon":"si","Phosphorus":"p","Sulphur":"s","Chlorine":"cl","Argon":"ar","Potassium":"k","Calcium":"ca"}
    score = 0
    count = 0
    while count <= 9:
        count += 1
        rand_element = random.choice(list(elements.keys()))
        rand_symbol = elements[rand_element]
        #print(rand_element)
        #print(rand_symbol)
        print(str(count) + ". " + rand_element + ": ", end="")
        ans = input()
        if(ans.lower() == rand_symbol):
            print(" - Correct.")
            score += 1
        else:
            print(" - Wrong.")

    else:
        print("\nYou sigh and put down your pencil. %s/10.  Not bad")

def music():
    #notes or name that tune with snacksound
    pass

def geography():
    print ("A geography quiz! Sarcasm! We're given a sheet as we walk in and are told to sit and do it as soon as we start. First to finish and get all marks wins a prize!")
    print ("I should try and win that prize!")

    correct = 0
    questionNum = 1
    countries = ["England", "France", "Spain", "Portugal", "Germany", "Sweden", "Denmark", "Netherlands"]
    
    for i in range(0,5):
        countriesDone = []
        country = random.choice(countries)
        countries.remove(country)
        capital = ""
        if country == "England":
            capital = "london"
        elif country == "France":
            capital = "paris"
        elif country == "Spain":
            capital = "madrid"
        elif country == "Portugal":
            capital = "lisbon"
        elif country == "Germany":
            capital = "berlin"
        elif country == "Sweden":
            capital = "stockholm"
        elif country == "Denmark":
            capital = "copenhagen"
        elif country == "Netherlands":
            capital = "amsterdam"
        print ("What is the capital of " + country + "?")
        answer = input (str(questionNum) + ". ")
        if answer.lower() == capital:
            correct += 1
            questionNum += 1
            print ("Correct!")
        else:
            questionNum += 1
            print ("Wrong!")

    if correct == 5:
        print ("YES! I WON A packet of rubber bands. Fantastic.")  #To develop story in the future, this prize can "Come in handy" :D
    else:
        print ("Well, at least I got " + correct + "/5. Not too bad I suppose")
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
