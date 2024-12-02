import turtle as t

def purp_square(): # purple square
    t.fillcolor('purple') # sets to purple 
    t.pencolor('red')
    t.begin_fill()
    for i in range(1, 5): #turns right and goes equidistant every iteration
        t.forward(100)
        t.right(90)
    t.end_fill()

def blue_rect(): # blue rectangle 
    t.fillcolor('blue') #sets color of rect
    t.begin_fill()
    for r in range(2): # draws rect 
        t.forward(20)
        t.left(90)
        t.forward(10)
        t.left(90)
    t.end_fill() # fills rect

def or_hex():
    t.fillcolor('orange') #sets color of orange regular hexagon
    t.begin_fill()
    for i in range(6): #dimensions of hexagon
        t.left(60)
        t.forward(10) 
    t.end_fill()


def red_hex():
    angles = [90, 60, 40,120,20,50] #irregular hexagon possible angles
    t.fillcolor('red')
    t.begin_fill()
    for i in range(5):
        t.right(angles[i]) # uses listed angles to make hexagon
        t.forward(100)
    t.end_fill()
        
        
def get_away_():
    t.left(90)
    t.penup() # moves pen up so turtle cant draw while moving away
    t.forward(130)
    t.pendown() # put the pen back down so turtle can draw


purp_square()

get_away_()

blue_rect()

get_away_()

or_hex()

get_away_()

red_hex()

get_away_()






    
