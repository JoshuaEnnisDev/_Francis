import pgzrun
from time import sleep

# actors
player1 = Actor("barnacle")
player1.start_pos = player1.pos
player1.end_pos = player1.pos
player1.positions = []
player1.timer = 10
player1.move = False
player1.mouse_down = False

circle_positions = []


def on_mouse_down(pos):
    player1.mouse_down = True


def set_pos():
    for position in player1.positions:
        if player1.timer <= 0:
            player1.timer = 10
            player1.pos = player1.positions.pop(0)
        else:
            player1.timer -= 1


def on_mouse_up(pos):
    player1.mouse_down = False
    player1.move = True
    player1.positions = circle_positions.copy()
    circle_positions.clear()


def on_mouse_move(pos):
    if player1.mouse_down:
        circle_positions.append(pos)


def draw():
    screen.clear()
    if player1.move:
        player1.draw()
    for position in circle_positions:
        screen.draw.filled_circle(position, 5, "red")


def update():
    if player1.move:
        set_pos()
    if len(player1.positions) <= 0:
        player1.move = False



pgzrun.go()
