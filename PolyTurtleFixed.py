"""
Turtle
This uses Turtle graphics to draw a polygon
that has the desired side lengths and angles of the user.
"""
from turtle import Screen, Turtle


wn = Screen()      # Creates a playground for turtles

def prompt_user_for_integer(prompt):
    text = input(prompt)
    return int(text) 

sideLength = prompt_user_for_integer("Enter the desired length of sides:")
corner = prompt_user_for_integer("Enter the desired number of corners:")

class PolyTurtle(Turtle):
    def __init__(self, sideLength, corner):
        super().__init__()
        self.distance = sideLength
        self.turn = corner
        self.angle = 180 - ((corner - 2)*180/corner)

    def move_and_turn(self):
        self.forward(self.distance)        # Tell turtle to move forward by chosen units
        self.left(self.angle)         # Tell turtle to turn by certain degrees based on designated number of corners

                                                   

 
kevin = PolyTurtle(sideLength, corner)       # Create a turtle, assign to Kevin
if kevin.turn >= 3:                  # Loop corner function as many times as angle input
    for i in range(kevin.turn):
        kevin.move_and_turn()

wn.mainloop()  # Wait for user to close window
