
import pygame
import random
import time 

pygame.init()

winxlength = 500
winywidth = 364

win = pygame.display.set_mode((winxlength,winywidth))
pygame.display.set_caption("Snake")

pygame.mouse.set_visible(False)

linewidth = 1

sizex = 15
sizey = 15

color = (225,225 , 225 )

pop = True

direction  = "right"

if sizex > sizey or sizey == sizex:
    squaresize = int( ( 979 - 23) /sizex)
else:
    squaresize = int(1680 /sizey)

winxlength = sizex * squaresize
winywidth = sizey * squaresize
win = pygame.display.set_mode((winywidth + linewidth, winxlength + linewidth))

class snakeblock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(win, (0, 0, 225), (self.x * squaresize, self.y * squaresize, squaresize, squaresize))

class fruitblock:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y 
        self.color = color
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x * squaresize, self.y * squaresize, squaresize, squaresize))

lists2 = []

lists2.append(fruitblock(random.randint(0, sizex-1), random.randint(0, sizey-1), (0, 225, 0)))



lists = [snakeblock(0, 0), snakeblock(1, 0), snakeblock(2, 0), snakeblock(3, 0)]

time.sleep(5)

sets = set()


run = True
while run:

    win.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
            if pop == True :   
                lists.pop(0)
            else:
                pop = True

        if keys[pygame.K_UP]:
            if lists[-1].y == 0:
                run = False
            lists.append(snakeblock(lists[-1].x, lists[-1].y - 1))
            direction = "up"
            if pop == True :   
                lists.pop(0)
            else:
                pop = True

        if keys[pygame.K_DOWN]:
            if lists[-1].y == sizey - 1:
                run = False
            lists.append(snakeblock(lists[-1].x, lists[-1].y + 1))
            direction = "down"
            if pop == True :   
                lists.pop(0)
            else:
                pop = True
        
        if keys[pygame.K_RIGHT]:
            if lists[-1].x == sizex - 1:
                run = False
            lists.append(snakeblock(lists[-1].x + 1, lists[-1].y))
            direction = "right"
            if pop == True :   
                lists.pop(0)
            else:
                pop = True

    else:

        if direction == "left" :
            if lists[-1].x == 0:
                run = False
            lists.append(snakeblock(lists[-1].x - 1, lists[-1].y))
            direction = "left"
            

        if direction == "up" :
            if lists[-1].y == 0:
                run = False
            lists.append(snakeblock(lists[-1].x, lists[-1].y - 1))
            direction = "up"
            

        if direction == "down" :
            if lists[-1].y == sizey - 1:
                run = False
            lists.append(snakeblock(lists[-1].x, lists[-1].y + 1))
            direction = "down"
            
        
        if direction == "right":
            if lists[-1].x == sizex - 1:
                run = False
            lists.append(snakeblock(lists[-1].x + 1, lists[-1].y))
            direction = "right"

        if pop == True :   
            lists.pop(0)
        else:
            pop = True

    if (lists[-1].x == lists2[0].x ) and (lists[-1].y == lists2[0].y):
        pop = False
        lists2.clear()
        lists2.append(fruitblock(random.randint(0, sizex-1), random.randint(0, sizey-1), (0, 225, 0)))

    for i in range( 0 , sizex + 1):
        pygame.draw.line( win , color, (0 , i * squaresize), (winywidth, i * squaresize), linewidth)

    for x in range( 0 , sizey + 1):
        pygame.draw.line( win , color, ( x * squaresize, 0), ( x * squaresize, winxlength), linewidth) 


    for x in range(0, len(lists)):
        lists[x].draw()
    

    sets.clear()

    for i in lists:
        if (str(i.x) + " " + str(i.y) in sets):
            run = False
        else:
            sets.add(str(i.x) + " " + str(i.y))


    lists2[0].draw()

    pygame.display.update() 
    
pygame.quit()


