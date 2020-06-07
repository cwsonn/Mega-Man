import pygame

pygame.init()

win = pygame.display.set_mode((560, 418))

pygame.display.set_caption("My First Pygame")

# This goes outside the while loop, near the top of the program

bg = pygame.image.load('Art_Assets/MegaMan_Backdrop.png')
# char = pygame.image.load('Art_Assets/standing.png')

# load in our sounds
bulletSound = pygame.mixer.Sound('MM_Assets/05 - MegaBuster.wav')
hitSound = pygame.mixer.Sound('MM_Assets/34 - PiPiPi.wav')
mmDamageSound = pygame.mixer.Sound('MM_Assets/07 - MegamanDamage.wav')
music = pygame.mixer.music.load('MM_Assets/05 Ruined Highway.mp3')
# music volume control between 0 and 1
pygame.mixer.music.set_volume(.5)
# play music on infinite loop
pygame.mixer.music.play(-1)

score = 0

screen_width = 560

# set the game clock
clock = pygame.time.Clock()


class player(object):
    lDMG = [pygame.image.load('MM_Assets/LDMG1.png'), pygame.image.load('MM_Assets/LDMG2.png')]
    rDMG = [pygame.image.load('MM_Assets/RDMG1.png'), pygame.image.load('MM_Assets/RDMG2.png')]

    walkRight = [pygame.image.load('MM_Assets/R0.png'), pygame.image.load('MM_Assets/R1.png'),
                 pygame.image.load('MM_Assets/R2.png'),
                 pygame.image.load('MM_Assets/R3.png'), pygame.image.load('MM_Assets/R4.png'),
                 pygame.image.load('MM_Assets/R5.png'),
                 pygame.image.load('MM_Assets/R6.png'), pygame.image.load('MM_Assets/R7.png'),
                 pygame.image.load('MM_Assets/R8.png'), pygame.image.load('MM_Assets/R9.png'),
                 pygame.image.load('MM_Assets/R10.png')]

    walkLeft = [pygame.image.load('MM_Assets/L0.png'), pygame.image.load('MM_Assets/L1.png'),
                pygame.image.load('MM_Assets/L2.png'),
                pygame.image.load('MM_Assets/L3.png'), pygame.image.load('MM_Assets/L4.png'),
                pygame.image.load('MM_Assets/L5.png'),
                pygame.image.load('MM_Assets/L6.png'), pygame.image.load('MM_Assets/L7.png'),
                pygame.image.load('MM_Assets/L8.png'), pygame.image.load('MM_Assets/L9.png'),
                pygame.image.load('MM_Assets/L10.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = True
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 5, self.y, 45, 52)
        self.isHit = False
        self.hitCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        else:
            if not self.standing:
                if self.left:
                    win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(self.walkRight[0], (self.x, self.y))
                else:
                    win.blit(self.walkLeft[0], (self.x, self.y))
            self.hitbox = (self.x + 5, self.y, 45, 52)
            # this line will enable the hitbox
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        """if self.left:
            win.blit(self.lDMG[0], (self.x, self.y))
            win.blit(self.lDMG[1], (self.x, self.y))
            win.blit(self.lDMG[0], (self.x, self.y))
            win.blit(self.lDMG[1], (self.x, self.y))
        elif self.right:
            win.blit(self.rDMG[0], (self.x, self.y))
            win.blit(self.rDMG[1], (self.x, self.y))
            win.blit(self.rDMG[0], (self.x, self.y))
            win.blit(self.rDMG[1], (self.x, self.y))"""


        self.isHit = True
        self.isJump = False
        self.jumpCount = 10
        self.x = 50
        self.y = 240
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        # text = font1.render('-10', 1, (255,0,0))
        # win.blit(text, ((screen_width/2 - (text.get_width()/2)),210))
        #pygame.display.update()
        # reset the jump count on being hit

        # add a delay so that the message stays on the screen
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            # add this block of code so you can still quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 100
                    pygame.quit()


class projectile(object):

    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        # the * facing is to determine the bullet direction
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('MM_Assets/RE1_2.png'),
                 pygame.image.load('MM_Assets/RE1_3.png'),
                 pygame.image.load('MM_Assets/RE1_4.png'), pygame.image.load('MM_Assets/RE1_5.png'),
                 pygame.image.load('MM_Assets/RE1_6.png'),
                 pygame.image.load('MM_Assets/RE1_7.png'), pygame.image.load('MM_Assets/RE1_8.png'),
                 pygame.image.load('MM_Assets/RE1_9.png')]

    walkLeft = [pygame.image.load('MM_Assets/LE1_2.png'),
                pygame.image.load('MM_Assets/LE1_3.png'),
                pygame.image.load('MM_Assets/LE1_4.png'), pygame.image.load('MM_Assets/LE1_5.png'),
                pygame.image.load('MM_Assets/LE1_6.png'),
                pygame.image.load('MM_Assets/LE1_7.png'), pygame.image.load('MM_Assets/LE1_8.png'),
                pygame.image.load('MM_Assets/LE1_9.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 5, self.y + 2, 40, 57)
        self.health = 10
        self.visible = True


    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 25:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                # draw the hitbox and move it along with the enemy character
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] - 7, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0),
                             (self.hitbox[0] - 7, self.hitbox[1] - 20, 50 - ((50 / 10) * (10 - self.health)), 10))
            self.hitbox = (self.x + 5, self.y + 2, 40, 57)
            # this line will enable the hitbox
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        # check if you are going to move past the end point for this enemy
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                # if no move forward
                self.x += self.vel
            # if yes flip the velocity so the enemy turns around
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.hitbox = (self.x, self.y, 0, 0)
            self.visible = False
        print('hit')
        pass


# function where all game objects are being drawn
def redrawGameWindow():
    # draw background
    win.blit(bg, (0, 0))
    # draw the scoreboard
    text = font.render('Score: ' + str(score), 1, (255, 255, 255))
    win.blit(text, (390, 10))
    # draw the player
    megaman.draw(win)
    # draw the enemy
    badguy.draw(win)
    # draw the bullets
    for bullet in bullets:
        bullet.draw(win)
    # update the screen
    pygame.display.update()


# create an instance of the player character
font = pygame.font.SysFont('comicsans', 30, True)

megaman = player(50, 240, 45, 51)
badguy = enemy(100, 235, 64, 64, 450)
shootLoop = 0
bullets = []
# main game loop
run = True
while run:
    # set game to run at 27 fps
    clock.tick(27)

    # PLAYER COLLISION
    if badguy.visible == True:
        if megaman.hitbox[1] < badguy.hitbox[1] + badguy.hitbox[3] and megaman.hitbox[1] + megaman.hitbox[3] > \
                badguy.hitbox[1]:
            # check if the player is inside the hitbox with the x coordinates
            if megaman.hitbox[0] + megaman.hitbox[2] > badguy.hitbox[0] and megaman.hitbox[0] < badguy.hitbox[0] + \
                    badguy.hitbox[2]:
                mmDamageSound.play()
                megaman.hit()
                score -= 10

    # BULLET DELAY TO PREVENT RAPID SHOTS
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # BULLET COLLISION
    for bullet in bullets:
        # check if the bullet is above the bottom of the rectangle and below the top of the rectangle
        if bullet.y - bullet.radius < badguy.hitbox[1] + badguy.hitbox[3] and bullet.y + bullet.radius > badguy.hitbox[
            1]:
            # check if the bullet is inside the hitbox with the x coordinates
            if bullet.x + bullet.radius > badguy.hitbox[0] and bullet.x - bullet.radius < badguy.hitbox[0] + \
                    badguy.hitbox[2]:
                hitSound.play()
                badguy.hit()
                score += 10
                # remove the bullet
                bullets.pop(bullets.index(bullet))

        if bullet.x < screen_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # define the key controls
    keys = pygame.key.get_pressed()
    move_left = keys[pygame.K_LEFT]
    move_right = keys[pygame.K_RIGHT]
    # down = keys[pygame.K_DOWN]
    # up = keys[pygame.K_UP]
    fire = keys[pygame.K_SPACE]
    jump = keys[pygame.K_UP]

    if fire and shootLoop == 0:
        bulletSound.play()
        if megaman.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(
                projectile(round(megaman.x + (megaman.width + 10) // 2), round(megaman.y + (megaman.height - 20) // 2),
                           6, (135, 206, 250), facing))

        shootLoop = 1

    if move_left and megaman.x > megaman.vel:
        megaman.x -= megaman.vel
        megaman.left = True
        megaman.right = False
        megaman.standing = False
    elif move_right and megaman.x < screen_width - megaman.width - megaman.vel:
        megaman.x += megaman.vel
        megaman.left = False
        megaman.right = True
        megaman.standing = False
    else:
        megaman.standing = True
        megaman.walkCount = 0

    if not megaman.isJump:
        # if up and y > vel:
        #    y -= vel
        # if down and y < screen_width - height - vel:
        #    y += vel
        if jump:
            # megaman.left = False
            # megaman.right = False
            megaman.isJump = True
            megaman.walkCount = 0

    else:
        # else if you are jumping do the following
        # set the negative so that the character comes back down from the jump
        if megaman.jumpCount >= -10:
            neg = 1
            if megaman.jumpCount < 0:
                neg = -1
            # set the y coordinate during the jump
            megaman.y -= (megaman.jumpCount ** 2) / 4 * neg
            megaman.jumpCount -= 1
        else:
            megaman.isJump = False
            megaman.jumpCount = 10

    redrawGameWindow()

pygame.quit()
