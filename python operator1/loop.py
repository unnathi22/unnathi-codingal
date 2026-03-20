import turtle
turtle.Screen().bgcolor("orange")
pen=turtle.Turtle()
size=0
while True:
    for i in range(4):
        pen.forward(size+1)
        pen.right(90)
        size=size-5
    size=size+1
    
