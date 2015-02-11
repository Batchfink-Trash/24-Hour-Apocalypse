from Utils import *
import SetUp
import sys
import random
import os

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
    os.system("cls")
    print("\n\"Damn\", you thought.  \"It's maths.  I hate maths.\"  Quite rightly too, as you have a horrible teacher.  He makes no effort to explain the lesson and uses irritating colloquial terms, such as \"sweet\" and \"awesome!\".  This really grinds your gears")
    input()
    os.system("cls")
    print("\nYou walk in.  Sir makes everyone stand behind their chairs as some sort of pointless punishment.  \"Good morning class\", he says.  You sit.")
    input()
    os.system("cls")
    print("\nOn the table in front of you is a sheet of questions.  Thankfully, these are easier than usual.  No confusing algebra or \"Fastest finger first\", whatever that is.\n")
    input()
    
    score = 0
    questionsDone = 1
    
    for i in range(0, 5):
        os.system("cls")
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
    os.system("cls")
    print("\nPhew, that was easy.  I scored " + str(score) + "/5.  Not bad!")
    input()
    os.system("cls")
    print("\"Alright guys, sweet lesson today.  You can go\" Everyone ran to get out of the room.")
    input()


def english():
    os.system("cls")
    print("\"Okay folks, settle down now, just got to wait for the computer to log on,\" is the usual greeting.")
    input()
    os.system("cls")
    print("We grab our books and a sheet with a question on it and sit. Another question based sheet. Great.")#
    input()
    os.system("cls")
    print ("\"Explane deeply wat is wrang wit this sentnce...\" Wow.")
    input()
    os.system("cls")
    
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
    input()
        
def history():
    #name dates
    pass

def pe():
    os.system("cls")
    print("You step into the dank, moist changing rooms to the beautiful smell of drugs and adolescence. Charming.")
    input()
    os.system("cls")
    print("\"Alright maggots, you've got football this lesson, so get changed. Now!\" What a guy.")
    input()
    os.system("cls")
    
    t1goals = 0
    t2goals = 0
    miscMsg = ""
    
    input()
    
    for i in range(0,41):
        time.sleep(0.7)
        chance = random.randint(0,40)
        os.system("cls")
        
        #chances for things to happen, feel free to change at will for balanced gameplay

        if i == 20:
            miscMsg = "And it's half-time"
        if chance == 1:
            miscMsg = "Team 1 has scored."
            t1goals += 1
        elif chance == 27:
            miscMsg = "Team 2 has scored."
            t2goals += 1
        elif chance == 25:
            miscMsg = "And it's hit the bar!"
        elif chance == 24:
            miscMsg = "Oh my, what a save!"

        #end of chances

        print("[" + str(i) + "]") 
        print(str(t1goals) + " - " + str(t2goals))
        print(miscMsg)
    time.sleep(1)
    if t1goals > t2goals:
        print("Yeah! You won")
    elif t1goals == t2goals:
        print("It was a draw.")
    else:
        print ("Boo, you suck!")
    input()

def science():
    #you must've been knackered xD
    #just tidied it up a lil'
    os.system("cls")
    print("\nChemistry, the one lesson which is based on speech. You can go to lectures for the same result. You suppose that it's better than physics.")
    input()
    os.system("cls")
    elements = {"Hydrogen":"h","Helium":"he","Lithium":"li","Beryllium":"be","Boron":"b","Carbon":"c","Nitrogen":"n","Oxygen":"o","Fluorine":"f","Neon":"ne","Sodium":"na","Magnesium":"mg","Aluminium":"al","Silicon":"si","Phosphorus":"p","Sulphur":"s","Chlorine":"cl","Argon":"ar","Potassium":"k","Calcium":"ca"}
    score = 0
    for i in range(1,11):
        rand_element = random.choice(list(elements.keys()))
        rand_symbol = elements[rand_element]
        elements.pop(rand_element, None)
        elements.pop(rand_symbol, None)       #removes from the list after, so that two of the same don't appear. Did the same with geography :D
        #print(rand_element)
        #print(rand_symbol)
        print(str(i) + ". " + rand_element + ": ", end="")
        ans = input()
        if(ans.lower() == rand_symbol):
            print(" - Correct.")
            score += 1
        else:
            print(" - Wrong.")

    if score >= 5:
        print("\nYou sigh and put down your pencil. " + str(score) + "/10.  Not bad.")
        input()
    else:
        print("\nYou sigh and put down your pencil angrily. " + str(score) + "/10.  Not pleased.")
        input()

def music():
    #notes or name that tune with snacksound -This could be difficult, especially installing it to a Library on Git, not sure how we'd achieve this {josh}
    pass

def geography():
    os.system("cls")
    print ("A geography quiz! Sarcasm! We're given a sheet as we walk in and are told to sit and do it as soon as we start. First to finish and get all marks wins a prize!")
    input()
    os.system("cls")
    print ("I should try and win that prize!")
    input()
    os.system("cls")

    correct = 0
    questionNum = 1
    countries = {"England":"london", "France":"paris", "Spain":"madrid", "Portugal":"lisbon", "Germany":"berlin", "Sweden":"stockholm", "Denmark":"copenhagen", "Netherlands":"amsterdam"}
    
    for i in range(0,5):
        os.system("cls")
        country = random.choice(list(countries))
        capital = countries[country]
        countries.pop(country, None)
        countries.pop(capital, None)
        
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
        os.system("cls")
        print ("YES! I WON A packet of rubber bands. Fantastic.")  #To develop story in the future, this prize can "Come in handy" :D
        input()
    else:
        os.system("cls")
        print ("Well, at least I got " + str(correct) + "/5. Not too bad I suppose")
        input()
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
    #Survive with friends! -So is this bit important? Or is this random per game? Do you HAVE to? How do you instigate this? {josh}
    pass

def aftee():
    #haha, didn't do your homework -DAFUQ? {josh}
    #Afterschool detention {James}
    pass
