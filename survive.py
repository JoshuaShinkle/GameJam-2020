import sys, pygame, random, time
pygame.init()


# Screen Setup
size = width, height = 800,600
playerSpeed = 5
white = 255, 255, 255
screen = pygame.display.set_mode(size)
cobbleStone = "tile012.png"
background = pygame.image.load(cobbleStone)
background = pygame.transform.scale(background, (800, 600))
start_time = time.time()


# Character Setup
class Enemy:
    def __init__(self):
        self.imageName = "tile033.png"
        self.loadedImage = pygame.image.load(self.imageName)
        self.image_rect = self.loadedImage.get_rect()
        self.speed = [0,0]
enemy1 = Enemy()
enemy2 = Enemy()

lance = "tile027.png"
lance = pygame.image.load(lance)
lance_rect = lance.get_rect()


# Character Spawn
lance_rect.centerx = width/2
lance_rect.centery = height/2

OFFSCREENDISTANCE = 30
def enemySpawn(enemy, width, height, OFFSCREENDISTANCE):
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

    enemy.image_rect.centerx = enemySpawnx
    enemy.image_rect.centery = enemySpawny
    enemy.speed = [speedX,speedY]

enemySpawn(enemy1, width, height, OFFSCREENDISTANCE)
enemySpawn(enemy2, width, height, OFFSCREENDISTANCE)
enemy1JustSpawned = True
enemy2JustSpawned = True
# Main
#def main(screen, enemy1, lance, lance_rect, justSpawned, width, height, playerSpeed, white, OFFSCREENDISTANCE):
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score = str(round(float(time.time()-start_time),3))
            font = pygame.font.Font('freesansbold.ttf', 108)
            text = font.render("Score: " + score, True, white)
            textRect = text.get_rect()
            textRect.center = (width // 2, height // 2)
            screen.blit(text, textRect)
            pygame.display.update()
            time.sleep(2)
            sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and lance_rect.centerx > 0:
            lance_rect = lance_rect.move(-playerSpeed,0)

        if event.key == pygame.K_RIGHT and lance_rect.centerx < width:
            lance_rect = lance_rect.move(playerSpeed,0)

        if event.key == pygame.K_UP and lance_rect.centery > 0:
            lance_rect = lance_rect.move(0,-playerSpeed)

        if event.key == pygame.K_DOWN and lance_rect.centery < height:
            lance_rect = lance_rect.move(0,playerSpeed)

    if (enemy1.image_rect.centerx < width + OFFSCREENDISTANCE and enemy1.image_rect.centerx > -OFFSCREENDISTANCE and enemy1.image_rect.centery < height + OFFSCREENDISTANCE and enemy1.image_rect.centery > -OFFSCREENDISTANCE) or enemy1JustSpawned == True:
            enemy1.image_rect = enemy1.image_rect.move(enemy1.speed)
            enemy1JustSpawned = False
    else:
        enemySpawn(enemy1, width, height, OFFSCREENDISTANCE)
        enemy1JustSpawned = True
    
    if (enemy2.image_rect.centerx < width + OFFSCREENDISTANCE and enemy2.image_rect.centerx > -OFFSCREENDISTANCE and enemy2.image_rect.centery < height + OFFSCREENDISTANCE and enemy2.image_rect.centery > -OFFSCREENDISTANCE) or enemy2JustSpawned == True:
            enemy2.image_rect = enemy2.image_rect.move(enemy2.speed)
            enemy2JustSpawned = False
    else:
        enemySpawn(enemy2, width, height, OFFSCREENDISTANCE)
        enemy2JustSpawned = True
    

    screen.blit(background, (0,0))
    screen.blit(lance, lance_rect)
    screen.blit(enemy1.loadedImage, enemy1.image_rect)
    screen.blit(enemy2.loadedImage, enemy2.image_rect)
    pygame.display.flip()
    
    
""" while 1:
    main(screen, enemy1, lance, lance_rect, justSpawned, width, height, playerSpeed, white, OFFSCREENDISTANCE) """