import turtle
import math
turtle.shape('turtle')
turtle.speed(0)

# # Square spiral drawing
# for i in range(1, 1000, 1):
#     turtle.forward(i*2)
#     turtle.left(90)

# 10 Square drawing
# for i in range(10, 100, 10):
#     turtle.forward(i)
#     turtle.left(90)
#     turtle.forward(i)
#     turtle.left(90)
#     turtle.forward(i)
#     turtle.left(90)
#     turtle.forward(i)
#     turtle.left(90)
#     turtle.penup()
#     turtle.setpos(-i / 2, -i / 2)
#     turtle.pendown()


# # Spiral drawing
# k = 5
# fi_rad = 0.1
# fi_degr = fi_rad * (90 / 3.14)
# for i in range(0, 1000):
#     ro = k * fi_rad
#     turtle.forward(ro)
#     turtle.left(fi_degr)
#     fi_rad += 0.1
#     ro += ro

# Multi Polygon drawing
a = 50
sides = 3
for iteration in range(1, 10, 1):
    k = 2 * math.sin(math.pi / sides)
    z = a / k
    turtle.pencolor('blue')
    turtle.setpos(z, 0)
    turtle.left(180 / sides)
    turtle.pencolor('black')
    for i in range(sides):
        print(360 / sides)  # test string
        turtle.forward(a)
        turtle.left(360 / sides)
    a += 5
    sides += 1

turtle.exitonclick()
