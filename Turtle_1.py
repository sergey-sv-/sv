import turtle

turtle.shape('turtle')
turtle.speed(0)

for i in range(1, 1000, 1):
    turtle.forward(i*2)
    turtle.left(90)

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



turtle.exitonclick()
