from static import Colours
import pygame


def transformImage(images):
    return pygame.transform.scale(images, (images.get_width() * 2, images.get_height() * 2))


def rotateImage(images, direction):
    return pygame.transform.rotate(images, 90*direction)


class PortalSprite(pygame.sprite.Sprite):
    def __init__(self, colour, name):
        super().__init__()
        self.direction = None
        self.x = None
        self.y = None
        self.name = name
        self.colour = colour
        self.state = "open"
        self.counter = 0
        self.index = 0
        self.idleImages = transformImage(pygame.image.load('PortalImages/Idle.xcf'))
        self.closeImages = transformImage(pygame.image.load('PortalImages/Close.xcf'))
        self.openImages = transformImage(pygame.image.load('PortalImages/Open.xcf'))
        self.images = None
        self.width = 128
        self.height = 128
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.intersectionLine = None

    def getImage(self):
        surface = pygame.Surface((self.width, self.height)).convert_alpha()
        self.image = surface
        self.image.set_colorkey((0, 0, 0))
        surface.blit(rotateImage(self.images, self.direction), (0, 0), ((self.index * self.width), 0, self.width, self.height))

    def setPos(self, projectile):
        self.state = "open"
        if projectile.name == 1:
            self.x = projectile.intersectionLine.xi1
            self.y = projectile.intersectionLine.yi1
        elif projectile.name == 2:
            self.x = projectile.intersectionLine.xi2
            self.y = projectile.intersectionLine.yi2

    def setLine(self, line):
        self.intersectionLine = line
        self.direction = self.intersectionLine.direction

portalSprites = pygame.sprite.Group()
portal = PortalSprite(Colours.blue, 1)
portal2 = PortalSprite(Colours.orange, 2)
portalSprites.add(portal)
portalSprites.add(portal2)
