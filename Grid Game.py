import turtle

#Draw
draw = turtle.Turtle()
draw.speed(0)
draw.color("blue")
draw.shapesize(stretch_wid=1, stretch_len=1)
draw.goto(0, 0)
draw.setheading(0)

#Directions
def Forward():
    draw.penup()
    draw.setheading(90)
    draw.fd(50)
    
def RTurn():
    draw.penup()
    draw.setheading(0)
    draw.fd(50)
    
def LTurn():
    draw.penup()
    draw.setheading(180)
    draw.fd(50)

def UTurn():
    draw.penup()
    draw.setheading(270)
    draw.fd(50)

#Square
def DSquare():
    draw.fillcolor("red")
    draw.pendown()
    draw.begin_fill()
    for i in range(4):
        draw.fd(50)
        draw.lt(90)
    draw.penup()
    draw.end_fill()

#Circle
def DCircle():
    draw.fillcolor("blue")
    draw.pendown()
    draw.begin_fill()
    draw.circle(25)
    draw.penup()
    draw.end_fill()
    
#Triangle
def DTriangle():
    draw.fillcolor("green")
    draw.pendown()
    draw.begin_fill()
    for i in range(3):
        draw.fd(50)
        draw.lt(120)
    draw.penup()
    draw.end_fill()


#Creating Display
win = turtle.Screen()
win.title("Pick a Number, any Number")
win.bgcolor("black")
win.setup(width=1000, height=650)
win.onkey(Forward, 'Up')
win.onkey(LTurn, 'Left')
win.onkey(RTurn, 'Right')
win.onkey(UTurn, 'Down')
win.onkey(DSquare, '4')
win.onkey(DCircle, '0')
win.onkey(DTriangle, '3')
win.listen()
win.mainloop()