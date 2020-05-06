import random

countrys = ["Germany", "France", "United Kingdom", "China", "Japan", "Australia", "Italy","Russia", "Brazil", "Canada"]
capitals = ["Berlin", "Paris", "London", "Bejing", "Tokyo", "Canberra", "Rome", "Moscow", "Brasilia", "Ottawa"]

correct = 0
incorrect = 0
usedMatches = []

def checkMatch (matchName):
    inp = input().lower()
    if(str(inp) == matchName.lower()):
        print("Correct")
        return(True)
    else:
        print("Incorrect")
        return(False)

def getRandInt(x):
    number = random.randint(0, x)
    return number

for rounds in range(0, 10, 1):
    uniqueNum = True
    matchNumber = getRandInt(9)

    #this ensures no used countrys/capitals
    if matchNumber in usedMatches:
        uniqueNum = False
        while uniqueNum == False:
            matchNumber = getRandInt(9)
            if not(matchNumber in usedMatches):
                uniqueNum = True

    usedMatches.append(matchNumber)

    if getRandInt(1) == 0:
        print("Enter the capital of " + countrys[matchNumber])
        x = checkMatch(capitals[matchNumber])
        if x is True:
            correct +=1
        else:
            incorrect +=1
    else:
        print("Enter the country that " + capitals[matchNumber] + " is the capital of ")
        x = checkMatch(countrys[matchNumber])
        if x is True:
            correct +=1
        else:
            incorrect +=1

print("Amount Correct: " + str(correct) + " Amount Incorrect: " + str(incorrect))
#print("Zeros: " + str(zeros) + "    Ones: " + str(ones))
