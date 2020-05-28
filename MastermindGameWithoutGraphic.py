# Mastermind
# HsinYu Chi(Katie)

# This program will run mastermind game with GUI.

from random import*

def getSecretCode():

    scList = ['g', 'o', 'r', 'y', 'p', 'b','m','s']
    sc = []

    sc = sample(scList,4)
    
    return(sc)

def getGuess():

    guess = []
    guess = input("Enter four colors with lower case: ")

    return(guess)

def testGuess(ocode,sc):

    tempguess = []
    tempscode = []
    for i in range(4):
        tempguess.append(ocode[i])
        tempscode.append(sc[i])

    # Find black.
    for i in range(4):
        if tempguess[i] == tempscode[i]:
            tempguess[i] = "BK"
            tempscode[i] = "BK"
            
    # Find white.        
    for i in range(4):
        if tempguess[i] != "BK":
            for j in range(4):
                if tempguess[i] == tempscode[j]:
                    tempguess[i] = "WT"
                    tempscode[j] = "WT"

    # Count black and white.
    black = tempguess.count("BK")
    white = tempguess.count("WT")
            
    return(black,white)

def main():

    Secretcode = getSecretCode()
    turn = 0
    Black = 0
    while Black < 4 and turn <= 10:
        Guess = getGuess()
        Black, White = testGuess(Guess,Secretcode)
        print("Black has:{0}. White has:{1}.".format(Black, White))
        turn = turn + 1
    print(Secretcode)


main()
