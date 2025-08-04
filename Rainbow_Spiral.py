import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

hue = 0
for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    t.forward(i)
    t.left(59)
    hue += 0.002

turtle.done()
