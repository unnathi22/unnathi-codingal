import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,600 )
polygon=turtle.Turtle()
sides=7
sidelength=50
angle=360/sides
for i in range(sides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()