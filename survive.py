import sys, pygame
pygame.init()

size = width, height = 800,600
speed = 5
white = 255, 255, 255

screen = pygame.display.set_mode(size)

player = "tile024.png"

lance = pygame.image.load(player)
lance_rect = lance.get_rect()
lance_rect.centerx = width/2
lance_rect.centery = height/2

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            lance_rect = lance_rect.move(-speed,0)
        if event.key == pygame.K_RIGHT:
            lance_rect = lance_rect.move(speed,0)
        if event.key == pygame.K_UP:
            lance_rect = lance_rect.move(0,-speed)
        if event.key == pygame.K_DOWN:
            lance_rect = lance_rect.move(0,speed)

    screen.fill(white)
    screen.blit(lance, lance_rect)
    pygame.display.flip()