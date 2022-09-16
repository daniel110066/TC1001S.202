from random import *
from turtle import *
from freegames import path

car = path('car.gif')
#tiles = list(range(32)) * 2
tiles = [
    "Bake","Word","List","Four",
    "Five","Nine","Gold","Corn",
    "Good","Best","Cute","Zero",
    "Huge","Cool","Tree","Race",
    "Rice","Keep","Lace","Beam",
    "Game","Mars","Tide","Ride",
    "Hide","Exit","Hope","Cold",
    "From","Need","Stay","Come"
    ] * 2
state = {'mark': None}
hide = [True] * 64
##tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
foundtiles = 0
globalclicks = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    global foundtiles
    global globalclicks

    globalclicks += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot     
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        foundtiles += 2



        

def draw():
    "Draw image and tiles."
    clear() ## clears the screen
    goto(0, 0) ## places the car at the center of the screen
    shape(car)
    stamp()   
    global foundtiles
    global globalclicks


    ## draws the squares if they are hidden
    ## for every number from 0 to 64
    for count in range(64):
        if hide[count]: ## if the itle is hidden
            x, y = xy(count) ## find the coordinate of the tile
            square(x, y) ## place a square over it

    up()
    goto(0, 200)
    down()
    color('black')
    write("Tiles found : " + str(foundtiles), font=('Arial', 14, 'normal'), align = 'center')
    goto(-140, 200)
    color('black')
    write("Total clicks : " + str(globalclicks), font=('Arial', 14, 'normal'), align = 'center')

    mark = state['mark'] ## defines the state for a marked tile

    if mark is not None and hide[mark]: ## if the tile is marked and hidden
        x, y = xy(mark) ## get the location of the mark
        up()
        ## this line determines the position the numbers will appear in
        goto(x + 27, y + 1.5)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align = 'center')
        

    if foundtiles == 64:
        goto(0, 0)
        color('green')
        write("WINNER", font=('Arial', 30, 'normal'), align = 'center')   

    update() ## updates the screen
    ontimer(draw, 100) ## recursive method that calls draw every 100 ms

shuffle(tiles)
setup(420, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()