import turtle 
import random

def tree(t, branchLen):
    if branchLen > 5:
        t.forward(branchLen)
        r1 = random.randint(15, 45)
        t.right(r1)
        br = random.randint(5, 100)
        while br > branchLen:
            br = random.randint(0, 100)
        tree(t, br)
        r2 = random.randint(15, 60)
        t.left(r2)
        bl = random.randint(5, 100)
        while bl > branchLen:
            bl = random.randint(5, 100)
        tree(t, bl)
       # if r2 - r1 > 0:
        t.right(r2-r1)
       # else:
        t.backward(branchLen)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(5)
    myTurtle.down()
    myTurtle.color("green")
    tree(myTurtle, 100)
    myWin.exitonclick()

main()
