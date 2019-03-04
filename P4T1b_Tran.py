# Uses turtles
import turtle

# Creates a playground for turtles
win = turtle.Screen()

# Create a turtle and assign to t
t = turtle.Turtle()

# Increases pen size and changes cursor into blue turtle
t.pensize(4)            
t.pencolor("blue")    
t.shape("turtle")

# Draws my initials (JT)
t.forward(100)
t.penup()
t.backward(50)
t.pendown()
t.left(270)
t.forward(100)
t.left(270)
t.forward(50)
t.penup()
t.left(180)
t.forward(170)
t.left(90)
t.pendown()
t.forward(100)
t.left(90)
t.forward(50)
t.backward(100)

# End commands 
win.mainloop()            
