import pgzrun

WIDTH = 1280
HEIGHT = 640

bg = Actor("td1")

print(not bg.colliderect(bg))

def draw():
    screen.blit("td2", (0, 0))


pgzrun.go()