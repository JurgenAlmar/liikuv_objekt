import pygame
import sys
import random
import os


pygame.init()


lBlue = (153, 204, 255)
red = (255, 0, 0)


screenX, screenY = 640, 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Liikuvad mustad ruudud")


def load_image(filename):
    if os.path.exists(filename):
        return pygame.transform.scale(pygame.image.load(filename), (50, 50))
    else:
        print(f"Error: {filename} not found!")
        pygame.quit()
        sys.exit()


ruut = load_image("ruut.png")
mustruut = load_image("mustruut.png")


posX, posY = 100, 100
speed = 5

# Font
font = pygame.font.Font(None, 36)

# Loome mustad ruudud
num_mustad_ruudud = 5
mustad_ruudud = [
    {"x": random.randint(0, screenX - 50), "y": random.randint(0, screenY - 50),
     "dx": random.choice([-2, 2]), "dy": random.choice([-2, 2])}
    for _ in range(num_mustad_ruudud)
]


clock = pygame.time.Clock()

gameover = False
while not gameover:
    screen.fill(lBlue)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and posX > 0:
        posX -= speed
    if keys[pygame.K_RIGHT] and posX < screenX - 50:
        posX += speed
    if keys[pygame.K_UP] and posY > 0:
        posY -= speed
    if keys[pygame.K_DOWN] and posY < screenY - 50:
        posY += speed


    for ruut_data in mustad_ruudud:
        ruut_data["x"] += ruut_data["dx"]
        ruut_data["y"] += ruut_data["dy"]


        if ruut_data["x"] <= 0 or ruut_data["x"] >= screenX - 50:
            ruut_data["dx"] *= -1
        if ruut_data["y"] <= 0 or ruut_data["y"] >= screenY - 50:
            ruut_data["dy"] *= -1


    screen.blit(ruut, (posX, posY))
    for ruut_data in mustad_ruudud:
        screen.blit(mustruut, (ruut_data["x"], ruut_data["y"]))


    for ruut_data in mustad_ruudud:
        if pygame.Rect(posX, posY, 50, 50).colliderect(pygame.Rect(ruut_data["x"], ruut_data["y"], 50, 50)):
            gameover = True
            screen.fill(lBlue)
            game_over_text = font.render("Mäng läbi, said surma", True, red)
            screen.blit(game_over_text, (70, 300))
            pygame.display.flip()
            pygame.time.delay(2000)
            break


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
