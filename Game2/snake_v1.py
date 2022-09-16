from turtle import *
from random import randrange
from random import choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['green', 'blue', 'yellow', 'black', 'purple']
colorSnek = 'black'
colorFood = 'green'


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def randColor():
    global colorSnek 
    global colorFood
    colorSnek = choice(colors)
    colorFood = choice(colors)
    if colorFood == colorSnek:
        randColor()
    

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    global colorFood
    global colorSnek

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        #food moving one random step
        i = randrange(-1, 2) * 10
        while i+food.x>150 or i+food.x<-150:
            i = randrange(-1, 1) * 10
        food.x += i
        
        j = randrange(-1, 2) * 10
        while j+food.y>150 or j+food.y<-150:
            j = randrange(-1, 1) * 10
        food.y += j
        #---------------------------
        
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnek)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)

randColor()
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
