import turtle

def show_logo():
    try:
        screen = turtle.Screen()
        screen.title("Logo")

        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()

        t.penup()
        t.goto(-200, 120)
        t.pendown()

        t.color("deepskyblue")
        t.begin_fill()

        for _ in range(2):
            t.forward(400)
            t.right(90)
            t.forward(240)
            t.right(90)

        t.end_fill()

        cx, cy = 20, 10

        t.penup()
        t.goto(cx, cy + 30)
        t.pendown()
        t.dot(55, "yellow")

        for angle in range(0, 360, 15):
            t.penup()
            t.goto(cx, cy + 30)
            t.setheading(angle)
            t.forward(28)
            t.pendown()

            t.color("yellow")
            t.begin_fill()
            t.right(90)
            t.forward(4)
            t.left(120)
            t.forward(12)
            t.left(120)
            t.forward(12)
            t.end_fill()

        t.penup()
        t.goto(cx, cy - 15)
        t.color("yellow")
        t.begin_fill()

        t.goto(cx - 45, cy - 20)
        t.goto(cx - 15, cy - 30)
        t.goto(cx - 5, cy - 35)
        t.goto(cx, cy - 45)
        t.goto(cx + 5, cy - 35)
        t.goto(cx + 15, cy - 30)
        t.goto(cx + 45, cy - 20)
        t.goto(cx, cy - 15)

        t.end_fill()

        t.penup()
        t.goto(-175, 80)
        t.color("yellow")
        t.width(4)

        for _ in range(4):
            t.setheading(0)
            t.pendown()
            t.circle(12, 180)
            t.right(90)
            t.penup()
            t.forward(8)
            t.right(90)
            t.pendown()
            t.circle(-12, 180)
            t.penup()
            t.setheading(-90)
            t.forward(52)

        screen.update()

    except turtle.Terminator:
        pass