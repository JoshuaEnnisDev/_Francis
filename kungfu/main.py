import pgzrun
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


def set_pos():
    if len(player1.positions) != 0:
        player1.pos = player1.positions.pop(0)
    else:
        clock.unschedule(set_pos)


def update_pos(delta):
    # player1.positions.reverse()
    
    num_pos = len(player1.positions)
    print(num_pos)
    clock.schedule_interval(set_pos, 1 / num_pos)
    # for position in player1.positions: 
    #     clock.schedule(set_pos, 1.0)
    #     player1.pos = position


def on_mouse_up(pos):
    global mouse_down
    mouse_down = False
    player1.move = True
    player1.positions = circle_positions.copy()
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


def update(delta):
    if player1.move:
        update_pos(delta)
        player1.move = False



pgzrun.go()
