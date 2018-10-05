import pygame, sys, os, time, random, math


class SpaceShip(object):
    def __init__(self):
        self.image = pygame.image.load("spaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.x = 400
        self.y = 720

    def draw(self, surface):
        image = self.image
        surface.blit(image, (self.x, self.y))
