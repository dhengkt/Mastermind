# MastermindGamewithGUI
# HsinYu Chi(Katie)

# This program combine the mastermind game
# with the interface GUI.

from graphics import*
from random import*


def drawBoard():

    global win
    global colors
    global Guess

    win = GraphWin("Mastermind", 400, 800)
    win.setCoords(0,0,400,800)
    win.setBackground("Antiquewhite")

    
    colors = ["Red","Mediumpurple","Dodgerblue","Green",
                 "Saddlebrown","Orange","Yellow","Pink"]

    area = Rectangle(Point(10,790),Point(390,20))
    area.draw(win)
    area.setOutline("Black")
    area.setFill("Lightsalmon")

    block1 = Rectangle(Point(10,790),Point(390,130))
    block1.draw(win)
    block1.setOutline("Black")
    block1.setFill("Lightsalmon")

    line1 = Line(Point(250,790),Point(250,130))
    line1.draw(win)
    line1.setOutline("Black")
    line2 = line1.clone()
    line2.draw(win)
    line2.move(90,0)
    line3 = Line(Point(10,730),Point(390,730))
    line3.draw(win)
    line3.setOutline("Black")
    

    # Draw the guess balls.
    for y in range(160,760,60):
        for x in range(40,240,60):
            gb = Circle(Point(x,y),20)
            gb.draw(win)
            gb.setWidth(3)
            gb.setFill("Sandybrown")
    # Draw the secret balls.
    for x in range(40,240,60):
        sb = Circle(Point(x,760),20)
        sb.draw(win)
        sb.setWidth(3)
        sb.setFill("Sandybrown")

    # Draw the check balls.
    for j in range(160,760,60):
        for i in range(265,340,20):
            cb1 = Circle(Point(i,j),5)
            cb1.draw(win)
            cb1.setOutline("Black")

    # Draw the color balls.
    cb1 = Circle(Point(40,100),20)
    cb1.draw(win)
    cb1.setFill("Red")
    tcb1 = Text(Point(40,100),"r")
    tcb1.draw(win)
    tcb1.setSize(16)
    cb2 = cb1.clone()
    cb2.draw(win)
    cb2.move(60,0)
    cb2.setFill("Mediumpurple")
    tcb2 = Text(Point(100,100),"m")
    tcb2.draw(win)
    tcb2.setSize(16)
    cb3 = cb2.clone()
    cb3.draw(win)
    cb3.move(60,0)
    cb3.setFill("Dodgerblue")
    tcb3 = Text(Point(160,100),"d")
    tcb3.draw(win)
    tcb3.setSize(16)
    cb4 = cb3.clone()
    cb4.draw(win)
    cb4.move(60,0)
    cb4.setFill("Green")
    tcb4 = Text(Point(220,100),"g")
    tcb4.draw(win)
    tcb4.setSize(16)
    cb5 = cb1.clone()
    cb5.draw(win)
    cb5.move(0,-50)
    cb5.setFill("Saddlebrown")
    tcb5 = Text(Point(40,50),"s")
    tcb5.draw(win)
    tcb5.setSize(16)
    cb6 = cb5.clone()
    cb6.draw(win)
    cb6.move(60,0)
    cb6.setFill("Orange")
    tcb6 = Text(Point(100,50),"o")
    tcb6.draw(win)
    tcb6.setSize(16)
    cb7 = cb6.clone()
    cb7.draw(win)
    cb7.move(60,0)
    cb7.setFill("Yellow")
    tcb7 = Text(Point(160,50),"y")
    tcb7.draw(win)
    tcb7.setSize(16)
    cb8 = cb7.clone()
    cb8.draw(win)
    cb8.move(60,0)
    cb8.setFill("Pink")
    tcb8 = Text(Point(220,50),"p")
    tcb8.draw(win)
    tcb8.setSize(16)

def getSecretCode():

    scList = ['g', 'o', 'r', 'y', 'p', 'd','m','s']
    sc = []

    sc = sample(scList,4)
    
    return(sc)

def getGuess():

    # Create the entry box for guess.
    Guess = Entry(Point(320,75),10)
    Guess.draw(win)
    Guess.setFill("White")

    # Check botton.
    area1 = Rectangle(Point(350,170+60*turn),Point(380,150+60*turn))
    area1.draw(win)
    area1.setOutline("Black")
    area1.setFill("White")

    text1 = Text(Point(365,160+60*turn),"Check")
    text1.draw(win)
    text1.setSize(9)
    
    win.getMouse()
    
    g = Guess.getText()
    guess = []
    
    for i in range(len(g)):
        guess.append(g[i])

    for color in colors:
        for i in range(len(guess)):
            if guess[i] == color[0].lower():
                circle = Circle(Point(40+60*i,160+60*turn),20)
                circle.setWidth(3)
                circle.setFill(color)
                circle.draw(win)
    area1.undraw()
    text1.undraw()

    return(guess)

def testGuess(oguess,sc):

    tempguess = []
    tempscode = []
    
    for ch in oguess:
        tempguess.append(ch)
    for i in range(4):
        tempscode.append(sc[i])
    #print(tempguess)
    #print(tempscode)

    # Find black.
    for i in range(4):
        if tempguess[i] == tempscode[i]:
            tempguess[i] = "bl"
            tempscode[i] = "bl"
            
    # Find white.        
    for i in range(4):
        if tempguess[i] != "bl":
            for j in range(4):
                if tempguess[i] == tempscode[j]:
                    tempguess[i] = "wh"
                    tempscode[j] = "wh"

    # Count black and white.
    black = tempguess.count("bl")
    white = tempguess.count("wh")

    testc = []
    ccolors = ["Black","White"]

    for i in range(black):
        circle = Circle(Point(265+20*i,160+60*turn),5)
        circle.draw(win)
        circle.setFill("Black")

    for i in range(white):
        circle = Circle(Point(265+20*(i+black),160+60*turn),5)
        circle.draw(win)
        circle.setFill("White")
        
    return(black,white)


def main():

    global turn

    gameboard = drawBoard()
    Secretcode = getSecretCode()
    turn = 0
    Black = 0
    while Black < 4 and turn < 10:
        Guess = getGuess()
        Black, White = testGuess(Guess,Secretcode)
        turn = turn + 1

    if Black == 4:
        Win = Rectangle(Point(140,460),Point(260,400))
        Win.draw(win)
        Win.setFill("Sandybrown")
        textwin = Text(Point(200,430),"You win!")
        textwin.draw(win)
        textwin.setSize(16)
    elif turn == 10:
        Lose = Rectangle(Point(140,460),Point(260,400))
        Lose.draw(win)
        Lose.setFill("Sandybrown")
        textwin = Text(Point(200,430),"You lose TT")
        textwin.draw(win)
        textwin.setSize(16)

    closeb = Rectangle(Point(280,50),Point(360,30))
    closeb.draw(win)
    closeb.setFill("White")
    closetext = Text(Point(320,40),"Close")
    closetext.draw(win)
    closetext.setSize(16)

        
    for color in colors:
        for i in range(len(Secretcode)):
            if Secretcode[i] == color[0].lower():
                circle = Circle(Point(40+60*i,760),20)
                circle.setWidth(3)
                circle.setFill(color)
                circle.draw(win)

    win.getMouse()
    win.close()
    
main()

#===== End file =====