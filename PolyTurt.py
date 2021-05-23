"""
Turtle
This uses Turtle graphics to draw a polygon
that has the desired side lengths and angles of the user.
"""
from turtle import Screen, Turtle     

class PolyTurtle(Turtle):     #Turtle contstruct that contains the length of the polygon's sides, the number of corners the polygon will have, and the angle required for the turtle to turn per corner of the shape.
    def __init__(self, sideLength, corner, polyColor):
        super().__init__()
        self.distance = sideLength
        self.turn = corner
        self.angle = 180 - ((corner - 2)*180/corner)

    def move_and_turn(self):
        self.pencolor(polyColor)           # Choose a color for the drawn shape.
        self.forward(self.distance)        # Tell turtle to move forward by chosen units.
        self.left(self.angle)              # Tell turtle to turn by certain degrees based on designated number of corners.

def prompt_user_for_integer(prompt):       # Function for accepting integer input.
    text = input(prompt)
    return int(text) 

def prompt_user_for_string(prompt):        # Function for accepting string input.
    text = input(prompt)
    return str(text) 

wn = Screen()      # Creates a window to display turtle actions.

while True:             #Loop prompt for side length, corners, and color so many polygons can be drawn.
    sideLength = prompt_user_for_integer("Enter the desired length of sides:")
    corner = prompt_user_for_integer("Enter the desired number of corners:")
    polyColor = prompt_user_for_string("What color would like the polygon to be?")
 
    myTurt = PolyTurtle(sideLength, corner, polyColor)       # Create a turtle object, assign to myTurt.
    if myTurt.turn >= 3:                                     # Loop corner function as many times as angle input.
        for i in range(myTurt.turn):
            myTurt.move_and_turn()




wn.mainloop()  # Wait for user to close window
