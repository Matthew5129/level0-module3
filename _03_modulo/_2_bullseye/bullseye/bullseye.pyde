def setup():
    # Set the size of your sketch
    size(400, 400)
    
    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    s = 400
    for i in range(4):
        fill("#FF0000")
        ellipse(200, 200, s, s)
        s-= 100
        for i in range(4):
            if i % 2 == 0:
                fill
                ellipse
            else:
                fill("#FFFFFF")
        # Use an if statement and modulo to alternate the color of your rings
    
    pass
