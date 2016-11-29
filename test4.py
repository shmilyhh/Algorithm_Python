import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSprial(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSprial(myTurtle, lineLen-5)

#drawSprial(myTurtle, 100)
#myWin.exitonclick()


def drawSprial(myTurtle, lineLen):
    if lineLen < 0:
        return

    drawSprial(myTurtle, lineLen-5)
    myTurtle.forward(lineLen)
    myTurtle.right(90)

drawSprial(myTurtle, 100)
myWin.exitonclick()
