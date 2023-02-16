import pygame


def drawGround(screen, w, h):
    rect = pygame.Rect( 0, h*(2/3), w, h/3)
    pygame.draw.rect(screen, (250, 214, 165), rect)


def drawOcean(screen, w, h):
    rect = pygame.Rect(0, h*(5/6), w, h/6)
    pygame.draw.rect(screen, (86, 113, 137), rect)


def drawStat(screen, string, image, stringPos, imagePos, imageSize):
    font = pygame.font.SysFont(None, 50)
    img = font.render(string, True, (0,0,0))
    screen.blit(img, stringPos)
    image = pygame.image.load(image)
    image = pygame.transform.scale(image, imageSize)
    imagerect = image.get_rect().move(imagePos)
    screen.blit(image, imagerect)


def drawAmmo(screen, loaded, mag):
    drawStat(screen, f"{str(loaded)}/{str(mag)}", "data/models/items/bullet.png", (20, 20), (15, 162-200), (150, 150))


def drawWeaponCooldown(screen, stabCooldown):
    font = pygame.font.SysFont(None, 50)
    img = font.render(f"{str(round(stabCooldown/60, 1))}s", True, (0,0,0))
    screen.blit(img, (140, 20))
    image = pygame.image.load("data/models/items/dagger.png")
    image = pygame.transform.scale(image, (60, 60))
    imagerect = image.get_rect().move((200, 0))
    screen.blit(image, imagerect)


def drawHealth(screen, health):
    drawStat(screen, str(health), "data/models/items/heart.png", (270, 20), (290,5), (60, 60))


def drawScore(screen, score):
    sw, _ = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont(None, 50)
    img = font.render(str(score), True, (0,0,0))
    screen.blit(img, (sw-100, 20))


def drawGameOver(screen):
    sw, sh = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont(None, 200)
    img = font.render(f"Game Over!", True, (0,0,0))
    screen.blit(img, (sw/2-400, sh/2))
    sw, sh = pygame.display.get_surface().get_size()
    font = pygame.font.SysFont(None, 50)
    img = font.render(f"Enter to retry...", True, (90,90,90))
    screen.blit(img, (sw/2-125, sh/2+175))


def setBackground(screen):
    w, h = pygame.display.get_surface().get_size()
    screen.fill((123, 143, 161))
    drawGround(screen, w, h)
    # drawOcean(screen, w, h)