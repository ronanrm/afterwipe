import turtle
import random as r

def random_color(): # makes random color for pen color except blue
    color = ['green', 'yellow', 'blue', 'purple', 'cyan', 'brown', 'orange', 'red', 'maroon', 'pink']
    rand_color = r.choice(color)
    if rand_color == 'blue':
        return 'black'
    else: return rand_color
    
sweeney = turtle.Turtle() # creates two turtles that can be used for control
sweeney.pencolor(random_color()) # sets pencolors as random color
sydney = turtle.Turtle()
sydney.pencolor(random_color())

def get_away():# moves sydney turtle away without drawing so the shapes are more defined
    sydney.penup()
    sydney.left(90)
    sydney.forward(200)
    sydney.pendown()

def house(t): # makes a sideways house and upside down house
    get_away()
    t.fillcolor(random_color())
    t.begin_fill()
    for i in range(4): # makes square
        t.forward(20)
        t.right(90)
    t.end_fill()  # ends coloring of house 
    t.left(90)
    t.fillcolor(random_color())
    t.begin_fill()
    for i in range(3): # makes triangle attached to square
        t.left(120)
        t.forward(20)
    t.end_fill() # ends coloring of roof

house(sydney)
house(sweeney)


    
    


    
