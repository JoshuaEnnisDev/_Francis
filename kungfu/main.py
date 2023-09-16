import pgzrun


# actors
player1 = Actor("barnacle")
player1.start_pos = player1.pos
player1.end_pos = player1.pos


def on_mouse_down(pos):
    player1.start_pos = pos
    player1.pos = player1.start_pos


def on_mouse_up(pos):
    player1.end_pos = pos


def on_mouse_move():
    pass


def draw():
    player1.draw()


pgzrun.go()
