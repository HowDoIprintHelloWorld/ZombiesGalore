import pygame

from pygameGUI.bullet import Bullet


class Player():
    def __init__(self):
        self.health = 3
        self.dead = False

        self.bullets = []
        self.shootCooldown = 60
        self.stabCooldown = 240
        self.stabDuration = 30
        self.loaded = 6
        self.maxCap = 6
        self.mag = self.maxCap

        self.stabbing = False
        
        self.imageState = "heroidle"
        self.sw, self.sh = pygame.display.get_surface().get_size()
        self.scale = (200, 200)
        
        self.lookTimer = 0
        self.lastShoot = 0
        self.lastReload = 0

        self.position = (self.sw/10, self.sh*(2/3)-self.scale[1])


    def updateBullets(self):
        self.bullets = [bullet for bullet in self.bullets if bullet.velocity > 0]
    

    def changeLook(self, new):
        self.imageState = new
        #pygame.time.wait(1000)
        #self.imageState = "heroidle"


    def shoot(self):   
        if self.lastShoot != 0 or self.loaded <= 0 or self.lastReload > 0:
            return
        bullet = Bullet(self.position)
        self.bullets.append(bullet)
        self.changeLook("herogun")
        self.lookTimer = 30
        self.lastShoot = self.shootCooldown
        self.loaded -= 1

    
    def checkDeath(self):
        if self.health <= 0:
            self.dead = True
            self.health = 0


    def triggerReload(self):
        if not self.mag:
            return
        self.lastReload = 75
        self.changeLook("heroreload")
        self.lookTimer = 150

    
    def stab(self):
        if self.lastShoot > 0:
            return
        self.lastShoot = self.stabCooldown
        self.lookTimer = self.stabDuration * 2
        self.changeLook("herostab")


    def doreload(self):
        if self.lastReload == 1:
            added = 0
            for i in range(self.maxCap):
                if self.mag == 0 or self.loaded >= self.maxCap:
                    break
                self.mag -= 1
                self.loaded += 1
        if self.lastReload > 0:
            self.lastReload -= 1


    def tick(self, timer):
        if self.lastShoot > 0:
            self.lastShoot -= 1
        if self.lookTimer > 0:
            self.lookTimer -= 1

    
    def isStabbing(self):
        if self.lastShoot >= self.stabCooldown - self.stabDuration:
            self.stabbing = True
        else:
            self.stabbing = False


    

    def draw(self, screen):
        if self.lookTimer == 0:
            self.changeLook("heroidle")
        
        self.tick(self.lastShoot)
        self.tick(self.lookTimer)
        self.isStabbing()

        image = pygame.image.load("data/models/player/" + self.imageState + ".png")
        image = pygame.transform.scale(image, self.scale)
        imagerect = image.get_rect().move(self.position)
        self.imagerect = imagerect

        screen.blit(image, imagerect)