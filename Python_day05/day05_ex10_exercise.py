from turtle import Turtle

data_list = [{
    "direction" : "L",
    "angle" : 0,
    "length" : 10
},{
    "direction" : "L",
    "angle" : 90,
    "length" : 100
},{
    "direction" : "L",
    "angle" : 90,
    "length" : 50
},{
    "direction" : "R",
    "angle" : 90,
    "length" : 100
},{
    "direction" : "R",
    "angle" : 90,
    "length" : 10
},{
    "direction" : "L",
    "angle" : 90,
    "length" : 0
}]


t = Turtle()
t.color("RED")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(-300, 0)
t.pendown()

def moveTurtle() :
    for data in data_list :
        direction = data['direction']
        angle = data['angle']
        length = data['length']

        t.left(angle) if direction=='L' else t.right(angle)
        t.forward(length)

for i in range(5) :
    moveTurtle()

input("PRess any key")