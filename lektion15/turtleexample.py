import turtle

turtle.color('green', 'lightgreen')
turtle.begin_fill()
while True:
    turtle.forward(150)
    turtle.left(210)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.done()
