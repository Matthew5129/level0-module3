import random
import turtle
from tkinter import simpledialog

# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them
    bob = turtle.Turtle()
    bob.shape('turtle')
    bob.shapesize(10)
    for i in range(4):
        bob.forward(100)
        bob.left(90)
    bob.width(10)
    user = simpledialog.askstring(title="user", prompt="what color turtle would you like?")
    if user == 'red':
        bob.color('red')
        for i in range(4):
            bob.forward(100)
            bob.left(90)
    if user == 'blue':
        bob.color('blue')
        for i in range(4):
            bob.forward(100)
            bob.left(90)













    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
