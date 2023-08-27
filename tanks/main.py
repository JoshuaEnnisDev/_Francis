from pgzrun import go


WIDTH = 800
HEIGHT = 600

player1 = Actor("church")
p1_gun = Actor("church_gun")

player2 = Actor("lee")
p2_gun = Actor("lee_gun")


def draw():
    player1.draw()
    p1_gun.draw()
    player2.draw()
    p2_gun.draw()


def update():
    screen.fill("green")
    p1_gun.pos = player1.pos
    p1_gun.angle = player1.angle
    if keyboard.w:
        player1.angle = 0
        player1.y -= 4
    elif keyboard.a:
        player1.angle = 90
        player1.x -= 4
    elif keyboard.s:
        player1.angle = 180
        player1.y += 4
    elif keyboard.d:
        player1.angle = -90
        player1.x += 4


go()
