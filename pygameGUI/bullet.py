import pygame



class Bullet():
    def __init__(self, position):
        self.position = position
        self.velocity = 30
        self.acceleration = -1
        self.scale = (200, 200)
        
        self.damage = 2

    
    def move(self):
        self.velocity += self.acceleration
        self.position = [self.position[0]+self.velocity, self.position[1]]

    
    def draw(self, screen):
        image = pygame.image.load("data/models/items/bullet.png")
        image = pygame.transform.scale(image, self.scale)
        imagerect = image.get_rect().move(self.position)
        self.imagerect = imagerect

        screen.blit(image, imagerect)

