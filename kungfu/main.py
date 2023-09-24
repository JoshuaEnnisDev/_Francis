import pgzrun
from pgzhelper import *
from time import sleep

# actors
player1 = Actor("barnacle")
player1.start_pos = player1.pos
player1.end_pos = player1.pos
player1.positions = []
player1.timer = 10
player1.move = False
mouse_down = False
circle_positions = []


def on_mouse_down(pos):
    global mouse_down
    mouse_down = True

    
def on_mouse_up(pos):
    global mouse_down
    mouse_down = False
    player1.move = True
    player1.positions = circle_positions
    circle_positions.clear()


def on_mouse_move(pos):
    global mouse_down
    if mouse_down:
        circle_positions.append(pos)


def draw():
    screen.clear()
    player1.draw()
    for i, circle in enumerate(circle_positions):
        screen.draw.filled_circle((circle_positions[i]), 5, "red")


def update():
    player1.timer -= 1
    if player1.move == True:
        for position in player1.positions:
            print(position)
            player1.pos = position
        player1.move = False


pgzrun.go()
