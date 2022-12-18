import turtle

turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)

turtle.fillcolor("#b2d8d8")
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()

turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)

window = turtle.Screen()
window.bgcolor('white')
window.title("Bunga buat Selma")

flower = turtle.Turtle()
flower.speed(0)
flower.color('#66b2b2')

rotate = int(180)


def Circles(t, size):
    for i in range(10):
        t.circle(size)
        size = size - 4


def drawCircles(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


drawCircles(flower, 150, 10)

t1 = turtle.Turtle()
t1.speed(20)
t1.color('#008080')

rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10


def drawCircles(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


drawCircles(t1, 130, 10)
t2 = turtle.Turtle()
t2.speed(20)
t2.color('#006666')

rotate = int(80)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5


def drawCircles(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


drawCircles(t2, 110, 10)
t3 = turtle.Turtle()
t3.speed(20)
t3.color('#004c4c')

t = turtle.Turtle()
for i in range(180):
    t.speed(0)
    t.color('#189ad3')
    t.circle(190 - i, 90)
    t.left(90)
    t.color('#1ebbd7')
    t.circle(190 - i, 90)
    t.left(18)

rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 19


def drawCircles(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


drawCircles(t3, 80, 10)
t4 = turtle.Turtle()
t4.speed(20)
t4.color('#71c7ec')

rotate = int(90)


def Circles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 20


def drawCircles(t, size, repeat):
    for i in range(repeat):
        Circles(t, size)
        t.right(360 / repeat)


drawCircles(t4, 40, 10)

turtle.done()
