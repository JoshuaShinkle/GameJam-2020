import sys, pygame, random
pygame.init()

size = width, height = 800,600
speed = 5
white = 255, 255, 255

screen = pygame.display.set_mode(size)

lance = "tile024.png"
lance = pygame.image.load(lance)
lance_rect = lance.get_rect()
lance_rect.centerx = width/2
lance_rect.centery = height/2

class Enemy:
    def __init__(self):
        self.imageName = "tile036.png"
        self.loadedImage = pygame.image.load(self.imageName)
        self.image_rect = self.loadedImage.get_rect()

enemy1 = Enemy()
enemy1.image_rect.centerx = width/3
enemy1.image_rect.centery = height/3

enemy2 = Enemy()
enemy2.image_rect.centerx = width/4
enemy2.image_rect.centery = height/4

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and lance_rect.centerx > 0:
            lance_rect = lance_rect.move(-speed,0)

        if event.key == pygame.K_RIGHT and lance_rect.centerx < width:
            lance_rect = lance_rect.move(speed,0)

        if event.key == pygame.K_UP and lance_rect.centery > 0:
            lance_rect = lance_rect.move(0,-speed)

        if event.key == pygame.K_DOWN and lance_rect.centery < height:
            lance_rect = lance_rect.move(0,speed)

    screen.fill(white)
    screen.blit(lance, lance_rect)
    screen.blit(enemy1.loadedImage, enemy1.image_rect)
    screen.blit(enemy2.loadedImage, enemy2.image_rect)
    pygame.display.flip()