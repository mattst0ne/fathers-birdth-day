import turtle
import random

bg = turtle.Screen()
bg.bgcolor("light blue")

tato = turtle.Turtle()
tato.shape("turtle")
tato.speed(75)

# draw lines
tato.penup()
tato.goto(-190, -180)
tato.color("yellow")
tato.pensize(6)
tato.pendown()
tato.goto(190, -180)
tato.penup()

tato.penup()
tato.goto(-160, -150)
tato.color("purple")
tato.pensize(6)
tato.pendown()
tato.goto(160, -150)
tato.penup()

tato.penup()
tato.goto(-130, -120)
tato.color("teal")
tato.pensize(6)
tato.pendown()
tato.goto(130, -120)
tato.penup()

# draw cake
tato.goto(-74, -110)
tato.pendown()
tato.color("white")
tato.goto(50, -110)
tato.left(90)
tato.forward(60)
tato.left(90)
tato.forward(125)
tato.left(90)
tato.forward(60)
tato.penup()

# draw candles
tato.goto(-60, -40)
tato.color("aquamarine")
tato.pendown()
tato.pensize(3)
tato.goto(-60, -20)
tato.penup()

tato.goto(-40, -40)
tato.color("yellow")
tato.pendown()
tato.pensize(3)
tato.goto(-40, -20)
tato.penup()

tato.goto(-20, -40)
tato.color("green")
tato.pendown()
tato.pensize(3)
tato.goto(-20, -20)
tato.penup()

tato.goto(0, -40)
tato.color("pink")
tato.pendown()
tato.pensize(3)
tato.goto(0, -20)
tato.penup()

tato.goto(20, -40)
tato.color("blue")
tato.pendown()
tato.pensize(3)
tato.goto(20, -20)
tato.penup()

# print message
tato.goto(-110, 35)
tato.color("grey")
tato.pendown()
tato.write("Happy Birthday Tato! I love you!", "24pt bold")


# send the turtle to the corner
tato.penup()
tato.goto(-250, 250)

input()
