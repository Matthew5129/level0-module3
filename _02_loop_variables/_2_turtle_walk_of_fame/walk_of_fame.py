import turtle

if __name__ == '__main__':
    bob = turtle.Turtle()
    bob.shape('turtle')
    bob.shapesize(2)
    bob.color('blue', 'green')
    bob.speed(100)

    # TODO 1) Set the X position of the turtle so that it starts on the left.
    bob.penup()
    bob.setx(-400)
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.
    bob.pendown()

    # TODO 3) Set the length of each line in the star to 30
    for j in range(10):
        for i in range(5):
            bob.forward(100)
            bob.right(144)
        bob.penup()
        bob.forward(100)
        bob.pendown()



























    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
