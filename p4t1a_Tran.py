# Uses turtles
import turtle

# Creates a playground for turtles
win = turtle.Screen()

# Create a turtle and assign to t
t = turtle.Turtle()

# Draws a square with a for loop
for i in (1,2,3,4):
    t.forward(50)
    t.left(90)

# Pick up pen and moves to the right and puts pen down 
t.penup()
t.forward(100)
t.pendown()

# Draws a triangle with a for loop
for i in (1,2,3):
    t.forward(100)          
    t.left(120)
    
# End commands 
win.mainloop()            
