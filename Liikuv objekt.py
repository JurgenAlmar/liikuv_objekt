import pygame
import sys
import random

pygame.init()


lBlue = (153, 204, 255)
red = [255, 0, 0]


screenX, screenY = 640, 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Liikuvad mustad ruudud")


ruut = pygame.image.load("ruut.png")
ruuttransform = pygame.transform.scale(ruut, (50, 50))

mustruut = pygame.image.load("mustruut.png")
mustruuttransform = pygame.transform.scale(mustruut, (50, 50))


posX, posY = 100, 100
speed = 5



num_mustad_ruudud = 5
mustad_ruudud = []
for _ in range(num_mustad_ruudud):
    mustad_ruudud.append({
        "x": random.randint(0, screenX - 50),
        "y": random.randint(0, screenY - 50),
        "dx": random.choice([-3, 3]),
        "dy": random.choice([-3, 3])
    })

gameover = False
while not gameover:
    screen.fill(lBlue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        posX -= speed
    if keys[pygame.K_RIGHT]:
        posX += speed
    if keys[pygame.K_UP]:
        posY -= speed
    if keys[pygame.K_DOWN]:
        posY += speed


    for ruut in mustad_ruudud:
        ruut["x"] += ruut["dx"]
        ruut["y"] += ruut["dy"]


        if ruut["x"] <= 0 or ruut["x"] >= screenX - 50:
            ruut["dx"] *= -1
        if ruut["y"] <= 0 or ruut["y"] >= screenY - 50:
            ruut["dy"] *= -1


    screen.blit(ruuttransform, (posX, posY))
    for ruut in mustad_ruudud:
        screen.blit(mustruuttransform, (ruut["x"], ruut["y"]))

def check_collision(ruutx, ruuty, mustruutx, mustruuty):
    if abs(ruutx - mustruutx) < 45 and abs(ruuty - mustruuty) < 55:
        global ruut_x_direction
        global ruut_y_direction
        global mustruut_x_direction
        global mustruut_y_direction
        ruut_x_direction = 0
        ruut_y_direction = 0
        mustruut_x_direction = 0
        mustruut_y_direction = 0
        game_over()


def game_over():
    display_game_over = font.render("mäng läbi said surma", True,red)
    screen.blit(display_game_over, (70, 300))


check_collision(ruut.centerx, ruut.centery, mustruut.centerx, mustruut.centery)
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()
