import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pensize(1)
colors = ["cyan", "magenta", "lime", "orange", "white"]

for i in range(360):
    t.color(colors[i % len(colors)])
    t.forward(i * 2)
    t.backward(i * 2)
    t.left(1)

turtle.done()
