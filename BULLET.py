import pygame, sys, os, time, random, math


size = [800, 800]
display = pygame.display.set_mode(size)

colors = {
    "black": (0, 0, 0),
    "blue": (100, 230, 230),
    "white": (255, 255, 255)
}


class Bullets(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hit(self, x, y):
        if x-30 < self.x < x+100:
            if y+100 > self.y > y:
                return True

    def draw(self, surface, color):
        pygame.draw.ellipse(surface, colors[color], (self.x, self.y, 40, 40))

    def move(self, pos):
        self.y -= pos


class Bullet1(Bullets):
    def __init__(self, x, y):
        super(Bullet1, self).__init__(x, y)
        super(Bullet1, self).draw(display, "blue")
        super(Bullet1, self).move(1.66)
        super(Bullet1, self).hit(x, y)


class Bullet2(Bullets):
    def __init__(self, x, y):
        super(Bullet2, self).__init__(x, y)
        super(Bullet2, self).draw(display, "white")
        super(Bullet2, self).move(3.32)
        super(Bullet2, self).hit(x, y)
