import turtle
t = turtle.Pen()
t.backward(100)
t.left(90)
t.up()
t.forward(30)
t.down()
t.right(90)
t.forward(100)
t.hideturtle()
t.reset()

import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle
pen = turtle.Turtle()
pen.color("purple")
pen.width(5)
pen.speed(2)

# Function to draw letter 'H'
def draw_H():
    pen.penup()
    pen.goto(-150, 0)
    pen.pendown()
    pen.left(90)
    pen.forward(100)
    pen.backward(50)
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(50)
    pen.backward(100)
    pen.left(270)

# Function to draw letter 'A'
def draw_A():
    pen.left(60)
    pen.forward(100)
    pen.right(120)
    pen.forward(100)
    pen.backward(40)
    pen.left(60)
    pen.backward(60)
    pen.left(180)
    pen.up()
    pen.backward(60)
    pen.right(45)
    pen.backward(40)
    pen.right(140)
    pen.forward(100)
    pen.right(270)
    pen.forward(100)

# Function to draw letter 'W'
def draw_W():
    pen.penup()
    pen.pendown()
    pen.left(160)
    pen.forward(100)
    pen.right(140)
    pen.forward(100)
    pen.left(140)
    pen.forward(100)
    pen.right(140)
    pen.forward(100)

# Function to draw letter 'O'
def draw_O():
    pen.penup()
    pen.goto(200, 0)
    pen.pendown()
    pen.up()
    pen.forward(50)
    pen.down()
    pen.circle(50)


# Draw the letters for "HAWO"
draw_H()
draw_A()
draw_W()
draw_O()

# Hide the turtle and display the result
turtle.done()

    




