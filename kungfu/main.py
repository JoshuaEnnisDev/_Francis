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
    if len(player1.positions) != 0:
        player1.pos = player1.positions.pop(0)
    else:
        clock.unschedule(set_pos)


def update_pos():
    num_pos = len(player1.positions)
    clock.schedule_interval(set_pos, 1 / num_pos)


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
    player1.draw()
    for circle in circle_positions:
        screen.draw.filled_circle((circle), 5, "red")


def update():
    if player1.move:
        update_pos()
        player1.move = False


pgzrun.go()
