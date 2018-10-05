import pygame, sys, os, time, random, math


class dragon(object):
    def __init__(self, surface):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 150)
        self.death_time = 8 + round(time.time())
        self.time = round(time.time())
        self.image = pygame.image.load("alien1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        surface.blit(self.image, (self.x, self.y))

    def reprint(self, surface):
        surface.blit(self.image, (self.x, self.y))
