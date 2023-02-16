import pygame
from random import randint

from pygameGUI.background import setBackground, drawAmmo, drawWeaponCooldown, drawHealth, drawGameOver, drawScore
from pygameGUI.player import Player
from pygameGUI.ghost import Ghost


def nextSpawn():
    next = randint(1,3)
    fps = 60
    next = fps * next
    return next



def main(backend):
    pygame.init()

    fpsClock = pygame.time.Clock()

    width, height = 1200, 800
    screen = pygame.display.set_mode((width, height))

    while True:
        currGame = True
        player = Player()

        next = nextSpawn()
        enemies = []

        score = 0

        # Game loop.
        while currGame:
            

            if not player.dead:
                score += 1
                if next <= 0:
                    enemies.append(Ghost())
                    next = nextSpawn()
                next -= 1

            setBackground(screen)
            drawAmmo(screen, player.loaded, player.mag)
            drawWeaponCooldown(screen, player.lastShoot)
            drawHealth(screen, player.health)
            drawScore(screen, score//60)
            if player.dead:
                drawGameOver(screen)

            player.checkDeath()
            player.draw(screen)
            player.doreload()
            player.updateBullets()

            for bullet in player.bullets:
                bullet.move()
                bullet.draw(screen)

            for enemy in enemies:
                player.bullets = enemy.checkShot(player.bullets)
                if enemy.health <= 0:
                    enemy.die(player)
                    enemies.remove(enemy)
                    continue
                enemy.move(player)
                enemy.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    if not player.dead:
                        if event.key == pygame.K_SPACE:
                            player.shoot()
                        elif event.key == pygame.K_r:
                            player.triggerReload()
                        elif event.key == pygame.K_e:
                            player.stab()
                        elif event.key == pygame.K_p:
                            player.health = 0
                    else:
                        if event.key == pygame.K_RETURN:
                            currGame = False
                    
        
            pygame.display.flip()
            fpsClock.tick(60)