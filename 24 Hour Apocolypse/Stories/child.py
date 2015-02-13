from Utils import *
import SetUp
import sys
import random
import os
from time import *
from datetime import date

""" This module contains all of the necessary methods for the child story """

def getUp():
    #START STORY
    pass

def goToSchool():
    # random transport
    pass

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

def english(player):
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
    print ("\"Alright folks, next on the list is " + player.fore + ", so, " + player.fore + ", you ended up with " + str(marks) + "/5. Well done " + player.fore + "!\" Thanks sir. Thanks.")
    input()
        
def history(player):
    os.system("cls")
    print ("\"Okay class, take out your books and turn to page 1534 in the text book.\" Says your brain-dead, monotonous hell of a history teacher.")
    input()
    os.system("cls")
    score = 0
    year = date.today().year
    print ("Question 1")
    sleep(0.6)
    print ("\nWhat year did World War 2 start in?")
    sleep(0.6)
    print ("a. 1942")
    sleep(0.6)
    print ("b. 1939")
    sleep(0.6)
    print ("c. 1914")
    sleep(0.6)
    print ("d. 1839")
    sleep(0.6)
    ans = input("\n1. ")
    if ans == "1939" or ans.lower() == "b":
        score += 1
        print ("\n/")
        input()
    else:
        print ("\nx")
        input()
    os.system("cls")
    print ("Question 2")
    sleep(0.6)
    print ("\nWhat year did the apocalypse start in?")
    sleep(0.6)
    print ("a. 1945")
    sleep(0.6)
    print ("b. 1989")
    sleep(0.6)
    print ("c. " + year)
    sleep(0.6)
    print ("d. 2003")
    sleep(0.6)
    ans = input("\n2. ")
    if ans == year or ans.lower() == "c":
        score += 1
        print ("\n/")
        input()
    else:
        print ("\nx")
        input()
    os.system("cls")
    print("\"Okay class, " + player.fore + " got " + score + "/2, so yeah.\" You seriously believe that you've lost brain cells")
    

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
        elements.pop(rand_symbol, None)     
        #removes from the list after, so that two of the same don't appear. Did the same with geography :D
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

def form(player):
    os.system("cls")
    randform = random.randint(1,3)
    if randform == 1:
        print ("You walk into form, and sit at your seat. You are greeted with, \"Ok guys, we're gonna do the register and then have a bit of soociaal tiime.\" His accent rings in your ears.")
        input()
        os.system("cls")
        print ("\"Hey " + player.fore + ".\" says your \"friend\". You can't be bothered to remember their name.")
        input()
        os.system("cls")        
        print ("\"Hey.\"")
        input()
        os.system("cls") 
        print ("\"Ok guys, we're gonna watch some Newsground.\"")
        input()
        os.system("cls") 
        print ("What a great form. Fun.")
        input()
        os.system("cls") 
        print ("\"Breaking News! An unidentified suspect has bitten and or eaten over 50 people in a shopping mall.\"")
        input()
        os.system("cls") 
        print("\"Wow, what a crazy.\" Yeah.")
    if randform == 2:
        #mizen, do your form here:
        print("You walk into form, and sit at your seat. You are greeted with the sound of shrieking children and grunting adolescents fill your ears as you sit down. Lovely.")
        input()
        os.system("cls")
        print("\"I'M TRYING TO DO THE REGISTER\"")
        input()
        os.system("cls")
        print("\"SNOWBALL FIGHT!\"")
        input()
        os.system("cls")
        print("\"PLEASE, FOR THE LOVE OF GOD, STOP THROWING GLUE AT THE WINDOWS!\"")
        input()
        os.system("cls")
        print("These are the noises that echo around the room, filling your head with pain and fury and...")
        input()
        os.system("cls")
        player.health -= 5      #Kinda for story later on
        print("*Smack*")
        input()
        os.system("cls")
        print("\"" + player.fore + ", are you OK..?\"")
        input()
        os.system("cls")
        print("You had knocked yourself out on the desk to escape the torment")
        input()
        os.system("cls")
        print("Only your friend had noticed. Speaking of noticing, you see your form tutor reading an article on the computer.")
        input()
        os.system("cls")
        print("MYSTERIOUS FIGURE SEEN WALKING AROUND A SHOPPING MALL, POLICE REPORTS CANNOT INDENTIFY THE SUSPECT.")
        input()
        os.system("cls")
        print("As you pick yourself up off the floor, the bell goes.")
        input()
        os.system("cls")
        print("\"Quickly, it's 12:30! RUN!\"")
        input()
        os.system("cls")
        print("You sprint from the classroom, leaving the hellish cesspit behind...")
        input()

        # So, I got carried away.  Most of the details mentioned above are true, but slightly exaggerated...
        # ...WHAT THE HELL IS GOIN ON IN HERE? XD Gramatically fixed it as well (not so many !'s !!!!!) , and added the zombie reference. Pls read :D

        pass
    if randform == 3:
        print ("You walk into form, and sit at your seat. You are greeted with, \"Alright children, you have lots of things to do this form time. Give me your phones!\" God I hate this woman.")
        input()
        os.system("cls")
        print ("\"Hey " + player.fore + ".\" says your \"friend\". You can't be bothered to remember their name.")
        input()
        os.system("cls")        
        print ("\"Hey.\"")
        input()
        os.system("cls") 
        print ("\"Alright children, get to it!\"")
        input()
        os.system("cls") 
        print ("What a great form. Fun.")
        input()
        os.system("cls") 
        print ("\"Did you hear about that wierd person at that Shopping Mall?\"")
        input()
        os.system("cls") 
        print("\"No.\"")
        input()
        os.system("cls") 
        print("\"Yeah, they started biting people and ripping flesh off and stuff!\"")
        input()
        os.system("cls") 
        print("\"Ewwwwwwww.\"")
        input()
        os.system("cls") 
        print("\"Huh. Probably a fake story.\"")
        input()
        os.system("cls") 
        print("\"Nah mate.\"")
        input()
        os.system("cls") 
        print("You know that it is a fake story. What a stupid story!")
        input()

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
