import turtle

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
b = 90
sides = 3
for it in range(1, 10, 1):
    for i in range(sides):
        turtle.forward(a)
        z = 360 / sides
        turtle.left(z)
    turtle.penup()
    turtle.setpos(-a, 0)
    turtle.pendown()
    a += 5
    sides += 1

turtle.exitonclick()
