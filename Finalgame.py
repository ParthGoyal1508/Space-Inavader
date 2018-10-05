import pygame, sys, os, time, random, math
import SS, BULLET, DRAGON


#-------------------------Initialization---------------------
pygame.init()

# Color codes
colors = {
    "black": (0, 0, 0),
    "blue": (100, 230, 230),
    "white": (255, 255, 255)
}

# Game Sound files
space_sound = pygame.mixer.Sound("fastinvader3.wav")
skey_sound = pygame.mixer.Sound("ufo_highpitch.wav")
freeze_sound = pygame.mixer.Sound("shoot.wav")
shoot_sound = pygame.mixer.Sound("invaderkilled.wav")

# Background Image
bg = pygame.image.load("wallpaper2.png")
bg = pygame.transform.scale(bg, (800, 800))

pygame.mouse.set_visible(0)
clock = pygame.time.Clock()
size = [800, 800]
display = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invendors")

ship_width = 100
ship_height = 100

score = 0
font = pygame.font.SysFont("Wide Latin", 32)

#------------------- The Game--------------------------------

ship = SS.SpaceShip()

bullets1 = []
bullets2 = []

x_move = 0

bugs = []
bug = DRAGON.dragon(display)
bugs.append(bug)
initial_time = round(time.time())

gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_q):
                gameLoop = False

            if(event.key == pygame.K_a):
                x_move = -5

            if(event.key == pygame.K_d):
                x_move = 5

            if(event.key == pygame.K_SPACE):
                pygame.mixer.Sound.play(space_sound)
                bullet = BULLET.Bullet1(ship.x + 30, ship.y - 35)
                bullets1.append(bullet)
            if(event.key == pygame.K_s):
                pygame.mixer.Sound.play(skey_sound)
                bullet = BULLET.Bullet2(ship.x + 30, ship.y - 35)
                bullets2.append(bullet)

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_a or event.key == pygame.K_d):
                x_move = 0

    display.fill(colors["black"])

    display.blit(bg, (0, 0))

    if round(time.time()) - initial_time == 10:
        bugs.append(DRAGON.dragon(display))
        initial_time = round(time.time())

    for i in bugs:
        if i.death_time - round(time.time()) > 0:
            i.reprint(display)
            for item in bullets1:
                if item.hit(i.x, i.y):
                    bullets1.remove(item)
                    score += 1
                    print("SCORE:: " + str(score))
                    pygame.mixer.Sound.play(shoot_sound)
                    bugs.remove(i)

            for item in bullets2:
                if item.hit(i.x, i.y):
                    i.image = pygame.image.load("alien2.png")
                    i.image = pygame.transform.scale(i.image, (100, 100))
                    i.death_time += 5
                    pygame.mixer.Sound.play(freeze_sound)
                    bullets2.remove(item)

        elif round(time.time()) - i.death_time == 0:
            bugs.remove(i)

    text = font.render("Score: " + str(score), True, colors["blue"])
    display.blit(text, (680, 30))

    for i in bullets1:
        if(i.x <= 800 and i.y <= 800):
            i.draw(display, "blue")
            i.move(1.66)
        if(i.y < -30):
            bullets1.remove(i)

    for i in bullets2:
        if(i.x <= 800 and i.y <= 800):
            i.draw(display, "white")
            i.move(3.32)
        if(i.y < -30):
            bullets2.remove(i)

    ship.x += x_move

    if ship.x < 0:
        ship.x -= x_move
    if ship.x + 50 > 750:
        ship.x -= x_move

    ship.draw(display)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
