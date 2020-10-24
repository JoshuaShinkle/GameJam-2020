import sys, pygame
pygame.init()

size = width, height = 800,600
speed = [2, 2]
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

    screen.fill(white)
    screen.blit(lance, lance_rect)
    pygame.display.flip()