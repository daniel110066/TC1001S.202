from math import sqrt
from turtle import *
import turtle as T
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    signX=(end.x - start.x)/abs(end.x - start.x)
    signY=(end.y - start.y)/abs(end.y - start.y)
    
    for count in range(4):
        forward((end.x - start.x))
        left((signX/signY)*(90))

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    radius = sqrt((start.x-end.x)*(start.x-end.x)+(start.y-end.y)*(start.y-end.y))
    goto(start.x,start.y-radius)
    down()
    begin_fill()
    T.circle(radius)
    end_fill()
    

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    goto(end.x, start.y)
    goto(end.x, end.y)
    goto(start.x,end.y)
    goto(start.x, start.y)
    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    goto(start.x + (end.x - start.x)*2, start.y)
    goto(end.x, end.y)
    goto(start.x, start.y)
    end_fill()
    

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#Add a new color
onkey(lambda: color('yellow'), 'Y')
#--------------
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
