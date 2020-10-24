import sys, pygame, random
pygame.init()

# Screen Setup
size = width, height = 800,600
playerSpeed = 5
white = 255, 255, 255
screen = pygame.display.set_mode(size)

# Character Setup
class Enemy:
    def __init__(self):
        self.imageName = "tile036.png"
        self.loadedImage = pygame.image.load(self.imageName)
        self.image_rect = self.loadedImage.get_rect()
        self.speed = [0,0]
enemy1 = Enemy()

lance = "tile024.png"
lance = pygame.image.load(lance)
lance_rect = lance.get_rect()


# Character Spawn
lance_rect.centerx = width/2
lance_rect.centery = height/2

OFFSCREENDISTANCE = 30
def enemySpawn(enemy1, width, height, OFFSCREENDISTANCE):
    spawnSide = random.randint(0,3)
    OFFSCREENDISTANCE = 30
    if spawnSide == 0:
        enemySpawnx = -OFFSCREENDISTANCE
        enemySpawny = random.randint(0, height)
        speedX = random.randint(1,6)
        speedY = random.randint(-3,3)
    elif spawnSide == 1:
        enemySpawnx = random.randint(0, width)
        enemySpawny = -OFFSCREENDISTANCE
        speedX = random.randint(-3,3)
        speedY = random.randint(1,6)
    elif spawnSide == 2:
        enemySpawnx = width + OFFSCREENDISTANCE
        enemySpawny = random.randint(0, height)
        speedX = random.randint(-6,-1)
        speedY = random.randint(-3,3)
    elif spawnSide == 3:
        enemySpawnx = random.randint(0, width)
        enemySpawny = height + OFFSCREENDISTANCE
        speedX = random.randint(-3,3)
        speedY = random.randint(-6,-1)

    enemy1.image_rect.centerx = enemySpawnx
    enemy1.image_rect.centery = enemySpawny
    enemy1.speed = [speedX,speedY]

enemySpawn(enemy1, width, height, OFFSCREENDISTANCE)
justSpawned = True
# Main
#def main(screen, enemy1, lance, lance_rect, justSpawned, width, height, playerSpeed, white):
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and lance_rect.centerx > 0:
            lance_rect = lance_rect.move(-playerSpeed,0)

        if event.key == pygame.K_RIGHT and lance_rect.centerx < width:
            lance_rect = lance_rect.move(playerSpeed,0)

        if event.key == pygame.K_UP and lance_rect.centery > 0:
            lance_rect = lance_rect.move(0,-playerSpeed)

        if event.key == pygame.K_DOWN and lance_rect.centery < height:
            lance_rect = lance_rect.move(0,playerSpeed)

    if (enemy1.image_rect.centerx < width + OFFSCREENDISTANCE and enemy1.image_rect.centerx > -OFFSCREENDISTANCE and enemy1.image_rect.centery < height + OFFSCREENDISTANCE and enemy1.image_rect.centery > -OFFSCREENDISTANCE) or justSpawned == True:
            enemy1.image_rect = enemy1.image_rect.move(enemy1.speed)
            justSpawned = False
    else:
        enemySpawn(enemy1, width, height, OFFSCREENDISTANCE)
        justSpawned = True

    screen.fill(white)
    screen.blit(lance, lance_rect)
    screen.blit(enemy1.loadedImage, enemy1.image_rect)
    pygame.display.flip()
    
    
""" while 1:
    main(screen, enemy1, lance, lance_rect, justSpawned, width, height, playerSpeed, white) """