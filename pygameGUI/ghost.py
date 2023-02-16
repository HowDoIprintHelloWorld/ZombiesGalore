import pygame

from random import randint


class Ghost():
    def __init__(self):
        self.maxHealth = 4
        self.health = self.maxHealth
        self.damage = 1

        self.lastAttack = 0
        self.attackCooldown = 120

        self.velocity = 5

        self.scale = (200, 200)
        self.imagerect = None

        w, h = pygame.display.get_surface().get_size()
        self.position = [w-self.scale[0], h*(2/3)-self.scale[1]]

    
    def checkShot(self, bullets):
        toRemove = []
        if not bullets:
            return []
        for bullet in bullets:
            if not self.imagerect or not bullet.imagerect:
                continue
            if pygame.Rect.colliderect(self.imagerect, bullet.imagerect):
                self.health -= bullet.damage
                toRemove.append(bullet)
        for bullet in toRemove:
            bullets.remove(bullet)
        return bullets
                
    
    def die(self, player, luck=0):
        baseLuck = 60
        luck = baseLuck + luck
        got = randint(0, 100)
        if got < luck:
            newRand = randint(1,2)
            if newRand == 1:
                player.mag += 3
            else:
                player.health += 1

    
    def playerColision(self, player):
        if not player.imagerect or not self.imagerect:
            return False
        if pygame.Rect.colliderect(self.imagerect, player.imagerect):
            if player.dead:
                return True
            if player.stabbing:
                self.health = 0
            else:
                if self.lastAttack:
                    self.lastAttack -= 1
                else:
                    player.health -= self.damage
                    self.lastAttack = self.attackCooldown
            return True
        return False
    
    def move(self, player):
        if self.playerColision(player):
            return
        self.position = [self.position[0] - self.velocity, self.position[1]]

    
    def drawHealthBar(self, screen):
        position = [self.position[0]+self.scale[0]*0.25, self.position[1]-30]
        fullLen = self.scale[0]*0.75
        fullRect = pygame.Rect(*position, fullLen, 20)
        pygame.draw.rect(screen, (200, 0, 0), fullRect)
        realLen = fullLen * (self.health/self.maxHealth)
        realRect = pygame.Rect(*position, realLen, 20)
        pygame.draw.rect(screen, (0, 200, 0), realRect)


    def draw(self, screen):
        image = pygame.image.load("data/models/enemies/ghostskeleton.png")
        image = pygame.transform.scale(image, self.scale)
        imagerect = image.get_rect().move(self.position)
        self.imagerect = imagerect
        self.drawHealthBar(screen)

        screen.blit(image, imagerect)