
import pygame
import random
import time 

pygame.init()

pygame.display.set_caption("Snake")

linewidth = 1

sizex = 30
sizey = 30

color = (225,225 , 225 )

if sizex > sizey or sizey == sizex:
    squaresize = int( ( 979 - 23) /sizex)
else:
    squaresize = int(1680 /sizey)

winxlength = sizex * squaresize
winywidth = sizey * squaresize

win = pygame.display.set_mode((winywidth + linewidth, winxlength + linewidth))

straberryraw = pygame.image.load("pixil-frame-0.png")
straberry = pygame.transform.scale(straberryraw, (squaresize, squaresize))

timekeeper = 0

class snakeblock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(win, (0, 0, 225), (self.x * squaresize, self.y * squaresize, squaresize, squaresize))

    def redanimation(self):
        pygame.draw.rect(win, (225, 0, 0), (self.x * squaresize, self.y * squaresize, squaresize, squaresize))

    def winanumation(self):
        pygame.draw.rect(win, (234, 104, 116), (self.x * squaresize, self.y * squaresize, squaresize, squaresize))

class fruitblock:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y 
        self.color = color
    def draw(self):
        
        if self.easteregg == False:
            pygame.draw.rect(win, self.color, (self.x * squaresize, self.y * squaresize, squaresize, squaresize))
        else:
            win.blit(straberry, (self.x * squaresize, self.y * squaresize))


def titlescreen():

    font = pygame.font.Font('freesansbold.ttf', 80)    
    text = font.render('Start Game', True, (255,0,0)) 
    textRect = text.get_rect()
    textRect.center = (winxlength / 2, winywidth / 2) 

    font2 = pygame.font.Font('freesansbold.ttf', 40)   
    text2 = font2.render('© 2020 by Noah V', True, (255,0,0)) 
    textRect2 = text2.get_rect()
    textRect2.center = (winxlength / 2, (winywidth / 8) * 6) 

    run = True
    while run:
        win.fill((0,0,0))

        if pygame.mouse.get_pressed()[0] == True:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        for i in range( 0 , sizex + 1):
            pygame.draw.line( win , color, (0 , i * squaresize), (winywidth, i * squaresize), linewidth)

        for x in range( 0 , sizey + 1):
            pygame.draw.line( win , color, ( x * squaresize, 0), ( x * squaresize, winxlength), linewidth) 
            
        pygame.draw.rect(win, (0,0,0), textRect)

        pygame.draw.rect(win, (0,0,0), textRect2)
        
        win.blit(text2, textRect2)
        win.blit(text, textRect)

        pygame.display.update()  

def snake():

    pygame.mouse.set_visible(False)
    
    lists2 = []

    lists2.append(fruitblock(random.randint(1, sizex-2), random.randint(1, sizey-2), (0, 225, 0)))
    lists2[0].easteregg = False

    global lists

    xbuffer = 4
    ybuffer = 4

    randomx = random.randint(xbuffer, sizex - (1 + xbuffer))
    randomy = random.randint(ybuffer, sizey - (1 + ybuffer))

    orentation = random.randint(0, 3)

    if orentation ==  0:
        lists = [snakeblock(0, randomy), snakeblock(0 + 1, randomy), snakeblock(0 + 2, randomy), snakeblock( 0 + 3, randomy)]
        direction  = "right"
    elif orentation ==  1:
        lists = [snakeblock(sizex - 1, randomy), snakeblock(sizex - 2, randomy), snakeblock(sizex - 3, randomy), snakeblock(sizex - 4, randomy)]
        direction  = "left"
    elif orentation ==  2:
        lists = [snakeblock(randomx, sizey - 1), snakeblock(randomx, sizey - 2), snakeblock(randomx, sizey - 3), snakeblock(randomx, sizey - 4)]
        direction  = "up"
    elif orentation ==  3:
        lists = [snakeblock(randomx, 0), snakeblock(randomx, 0 + 1), snakeblock(randomx, 0 + 2), snakeblock(randomx, 0 + 3)]
        direction  = "down"

 
    pop = True
    sets = set()

    delay = 150
    timekeeper = time.time()*1000

    run = True
    while run:

        win.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.time.delay( int(delay - ((time.time() * 1000) - timekeeper)))

        timekeeper = time.time()*1000

        keys = pygame.key.get_pressed()
            
        if  ((keys[pygame.K_RIGHT] and not direction  == 'left') or (keys[pygame.K_LEFT] and not direction == 'right')\
        or (keys[pygame.K_UP] and not direction == 'down') or (keys[pygame.K_DOWN] and not direction == "up"))\
        and not ((keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]) or (keys[pygame.K_LEFT] and keys[pygame.K_DOWN]) or (keys[pygame.K_LEFT] and keys[pygame.K_UP])\
        or (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]) or (keys[pygame.K_RIGHT] and keys[pygame.K_UP]) \
        or (keys[pygame.K_DOWN] and keys[pygame.K_UP])):
                        
            if keys[pygame.K_LEFT]:
                if lists[-1].x == 0:
                    run = False
                lists.append(snakeblock(lists[-1].x - 1, lists[-1].y))
                direction = "left"
                
            if keys[pygame.K_UP]:
                if lists[-1].y == 0:
                    run = False
                lists.append(snakeblock(lists[-1].x, lists[-1].y - 1))
                direction = "up"
                
            if keys[pygame.K_DOWN]:
                if lists[-1].y == sizey - 1:
                    run = False
                lists.append(snakeblock(lists[-1].x, lists[-1].y + 1))
                direction = "down"
                
            if keys[pygame.K_RIGHT]:
                if lists[-1].x == sizex - 1:
                    run = False
                lists.append(snakeblock(lists[-1].x + 1, lists[-1].y))
                direction = "right"
                
        else:

            if direction == "left" :
                if lists[-1].x == 0:
                    run = False
                lists.append(snakeblock(lists[-1].x - 1, lists[-1].y))

            if direction == "up" :
                if lists[-1].y == 0:
                    run = False
                lists.append(snakeblock(lists[-1].x, lists[-1].y - 1))

            if direction == "down" :
                if lists[-1].y == sizey - 1:
                    run = False
                lists.append(snakeblock(lists[-1].x, lists[-1].y + 1))

            if direction == "right":
                if lists[-1].x == sizex - 1:
                    run = False
                lists.append(snakeblock(lists[-1].x + 1, lists[-1].y))


        if pop == True :   
            lists.pop(0)
        else:
            pop = True

        if (lists[-1].x == lists2[0].x ) and (lists[-1].y == lists2[0].y):
            pop = False
            lists2.clear()
            lists2.append(fruitblock(random.randint(0, sizex-1), random.randint(0, sizey-1), (0, 225, 0)))
            if random.randint(0, 300) == 0:
                lists2[0].easteregg = True
            else:
                lists2[0].easteregg = False
            

        for x in range(0, len(lists)):
            lists[x].draw()

        if len(lists) == (sizex * sizey):
            winscreen()
        
        sets.clear()

        for i in lists:
            if (str(i.x) + " " + str(i.y) in sets):
                run = False
            else:
                sets.add(str(i.x) + " " + str(i.y))

        lists2[0].draw()

        for i in range( 0 , sizex + 1):
            pygame.draw.line( win , color, (0 , i * squaresize), (winywidth, i * squaresize), linewidth)

        for x in range( 0 , sizey + 1):
            pygame.draw.line( win , color, ( x * squaresize, 0), ( x * squaresize, winxlength), linewidth) 

        pygame.display.update() 
    
def endscreen():

    pygame.mouse.set_visible(True)

    score = len(lists) - 4

    font = pygame.font.Font('freesansbold.ttf', 80)    
    text = font.render('You Died', True, (255,0,0)) 
    textRect = text.get_rect()
    textRect.center = (winxlength / 2, winywidth / 2) 

    font2 = pygame.font.Font('freesansbold.ttf', 40)   
    text2 = font2.render('score: ' + str(score) , True, (255,0,0)) 
    textRect2 = text2.get_rect()
    textRect2.center = (winxlength / 2, (winywidth / 16) * 9) 

    font3 = pygame.font.Font('freesansbold.ttf', 40)   
    text3 = font3.render('Press R to respawn' , True, (255,0,0)) 
    textRect3 = text3.get_rect()
    textRect3.center = (winxlength / 2, (winywidth / 16) * 13) 

    font4 = pygame.font.Font('freesansbold.ttf', 40)   
    text4 = font4.render('Press R to respawn' , True, (255,0,0)) 
    textRect4 = text4.get_rect()
    textRect4.center = (winxlength / 2, (winywidth / 16) * 11) 


    run = True
    while run:
        win.fill((0,0,0))
        
        if pygame.mouse.get_pressed()[0] == True:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for x in range(0, len(lists)):
            lists[x].redanimation()

        for i in range( 0 , sizex + 1):
            pygame.draw.line( win , color, (0 , i * squaresize), (winywidth, i * squaresize), linewidth)

        for x in range( 0 , sizey + 1):
            pygame.draw.line( win , color, ( x * squaresize, 0), ( x * squaresize, winxlength), linewidth) 


        keys = pygame.key.get_pressed()

        if keys[pygame.K_r] == True :
            run = False
            
        pygame.draw.rect(win, (0,0,0), textRect)

        pygame.draw.rect(win, (0,0,0), textRect2)

        pygame.draw.rect(win, (0,0,0), textRect3)

        win.blit(text3, textRect3)
        
        win.blit(text2, textRect2)

        win.blit(text, textRect)

        pygame.display.update()  

def winscreen():
    pygame.mouse.set_visible(True)

    font = pygame.font.Font('freesansbold.ttf', 80)    
    text = font.render('You Win', True, (255,0,0)) 
    textRect = text.get_rect()
    textRect.center = (winxlength / 2, winywidth / 2) 

    run = True
    while run:
        win.fill((0,0,0))
        
        if pygame.mouse.get_pressed()[0] == True:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for x in range(0, len(lists)):
            lists[x].redanimation()

        for i in range( 0 , sizex + 1):
            pygame.draw.line( win , color, (0 , i * squaresize), (winywidth, i * squaresize), linewidth)

        for x in range( 0 , sizey + 1):
            pygame.draw.line( win , color, ( x * squaresize, 0), ( x * squaresize, winxlength), linewidth) 
            
        pygame.draw.rect(win, (0,0,0), textRect)

        win.blit(text, textRect)

        pygame.display.update()  

titlescreen()
snake()
run = True
while run:
    endscreen()
    snake()

pygame.quit()

