import pgzrun
from pgzhelper import *
from time import sleep

# actors
player1 = Actor("barnacle")
player1.start_pos = player1.pos
player1.end_pos = player1.pos
player1.positions = []
player1.timer = 10


def on_mouse_down(pos):
    player1.start_pos = pos


def on_mouse_up(pos):
    player1.end_pos = pos
    for position in player1.positions:
        if player1.timer == 10:
            player1.pos = position


def on_mouse_move(pos):
    player1.positions.append(pos)
    # player1.pos = pos


def draw():
    screen.clear()
    player1.draw()


def update():
    player1.timer -= 1
    if player1.timer <= 0:
        player1.timer = 10


pgzrun.go()
