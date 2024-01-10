import turtle as t

pen = t.Turtle()
screen = t.Screen()

screen.bgcolor("black")
pen.pencolor("red")

a = 0
b = 0

pen.speed(0)
pen.penup()
pen.goto(0,200)
pen.pendown()

while True:
    pen.forward(a)
    pen.right(b)
    a+=3
    b+=1
    if b == 250:
        break
t.done()