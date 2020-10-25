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
    def __init__(self, imageName):
        self.imageName = imageName
        self.loadedImage = pygame.image.load(self.imageName)
        self.image_rect = self.loadedImage.get_rect()
        self.speed = [0,0]
        self.justSpawned = True
enemy1 = Enemy("tile033.png")
enemy2 = Enemy("tile033.png")
enemy3 = Enemy("tile033.png")
enemy4 = Enemy("tile033.png")
enemy5 = Enemy("tile033.png")
enemy6 = Enemy("tile040.png")
enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]

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
        speedX = random.randint(4,8)
        speedY = random.randint(-3,3)
    elif spawnSide == 1:
        enemySpawnx = random.randint(0, width)
        enemySpawny = -OFFSCREENDISTANCE
        speedX = random.randint(-3,3)
        speedY = random.randint(4,8)
    elif spawnSide == 2:
        enemySpawnx = width + OFFSCREENDISTANCE
        enemySpawny = random.randint(0, height)
        speedX = random.randint(-8,-4)
        speedY = random.randint(-3,3)
    elif spawnSide == 3:
        enemySpawnx = random.randint(0, width)
        enemySpawny = height + OFFSCREENDISTANCE
        speedX = random.randint(-3,3)
        speedY = random.randint(-8,-4)

    enemy.image_rect.centerx = enemySpawnx
    enemy.image_rect.centery = enemySpawny
    enemy.speed = [speedX,speedY]

for enemy in enemies:
    enemySpawn(enemy, width, height, OFFSCREENDISTANCE)
    enemy.justSpawned = True

# Main
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    
    #enemy1
    if (enemy1.image_rect.centerx < width + OFFSCREENDISTANCE and enemy1.image_rect.centerx > -OFFSCREENDISTANCE and enemy1.image_rect.centery < height + OFFSCREENDISTANCE and enemy1.image_rect.centery > -OFFSCREENDISTANCE) or enemy1.justSpawned == True:
            enemy1.image_rect = enemy1.image_rect.move(enemy1.speed)
            enemy1.justSpawned = False
    else:
        enemySpawn(enemy1, width, height, OFFSCREENDISTANCE)
        enemy1.justSpawned = True
    
    #enemy2
    if (enemy2.image_rect.centerx < width + OFFSCREENDISTANCE and enemy2.image_rect.centerx > -OFFSCREENDISTANCE and enemy2.image_rect.centery < height + OFFSCREENDISTANCE and enemy2.image_rect.centery > -OFFSCREENDISTANCE) or enemy2.justSpawned == True:
            enemy2.image_rect = enemy2.image_rect.move(enemy2.speed)
            enemy2.justSpawned = False
    else:
        enemySpawn(enemy2, width, height, OFFSCREENDISTANCE)
        enemy2.justSpawned = True

    #enemy3
    if (enemy3.image_rect.centerx < width + OFFSCREENDISTANCE and enemy3.image_rect.centerx > -OFFSCREENDISTANCE and enemy3.image_rect.centery < height + OFFSCREENDISTANCE and enemy3.image_rect.centery > -OFFSCREENDISTANCE) or enemy3.justSpawned == True:
            enemy3.image_rect = enemy3.image_rect.move(enemy3.speed)
            enemy3.justSpawned = False
    else:
        enemySpawn(enemy3, width, height, OFFSCREENDISTANCE)
        enemy3.justSpawned = True

    #enemy4
    if (enemy4.image_rect.centerx < width + OFFSCREENDISTANCE and enemy4.image_rect.centerx > -OFFSCREENDISTANCE and enemy4.image_rect.centery < height + OFFSCREENDISTANCE and enemy4.image_rect.centery > -OFFSCREENDISTANCE) or enemy4.justSpawned == True:
            enemy4.image_rect = enemy4.image_rect.move(enemy4.speed)
            enemy4.justSpawned = False
    else:
        enemySpawn(enemy4, width, height, OFFSCREENDISTANCE)
        enemy4.justSpawned = True

    #enemy5
    if (enemy5.image_rect.centerx < width + OFFSCREENDISTANCE and enemy5.image_rect.centerx > -OFFSCREENDISTANCE and enemy5.image_rect.centery < height + OFFSCREENDISTANCE and enemy5.image_rect.centery > -OFFSCREENDISTANCE) or enemy5.justSpawned == True:
            enemy5.image_rect = enemy5.image_rect.move(enemy5.speed)
            enemy5.justSpawned = False
    else:
        enemySpawn(enemy5, width, height, OFFSCREENDISTANCE)
        enemy5.justSpawned = True

    #enemy6
    if (enemy6.image_rect.centerx < width + OFFSCREENDISTANCE and enemy6.image_rect.centerx > -OFFSCREENDISTANCE and enemy6.image_rect.centery < height + OFFSCREENDISTANCE and enemy6.image_rect.centery > -OFFSCREENDISTANCE) or enemy6.justSpawned == True:
            enemy6.image_rect = enemy6.image_rect.move(enemy6.speed)
            enemy6.justSpawned = False
    else:
        enemySpawn(enemy6, width, height, OFFSCREENDISTANCE)
        enemy6.justSpawned = True
    
    for enemy in enemies:
        if abs(enemy.image_rect.centerx - lance_rect.centerx) < 32 and abs(enemy.image_rect.centery - lance_rect.centery) < 32:
            score = str(round(float(time.time()-start_time),3))
            font = pygame.font.Font('freesansbold.ttf', 108)
            text = font.render("Score: " + score, True, white)
            textRect = text.get_rect()
            textRect.center = (width // 2, height // 2)
            screen.blit(text, textRect)
            pygame.display.update()
            time.sleep(2)
            sys.exit()

    screen.blit(background, (0,0))
    screen.blit(lance, lance_rect)
    for enemy in enemies:
        screen.blit(enemy.loadedImage, enemy.image_rect)
    pygame.display.flip()