import sys, pygame
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

enemy = "tile036.png"
enemy = pygame.image.load(enemy)
enemy_rect = enemy.get_rect()
enemy_rect.centerx = width/3
enemy_rect.centery = height/3

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
    screen.blit(enemy, enemy_rect)
    pygame.display.flip()