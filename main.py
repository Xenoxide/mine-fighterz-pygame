### main issue: audio files will not load ###

import pygame # .pylintrc file is to load the C extensions
import datetime
import loadassets
import random

pygame.init() #initalize pygame
clock = pygame.time.Clock() #for limiting the fps
backdrops, sprites = loadassets.loadAssets() #load assets


# I don't know why I have to multiply by two, otherwise it won't fit
screen = pygame.display.set_mode((480 * 2, 360 * 2)) 

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday = week_days[datetime.date(2020,7,24).weekday()]
playerName = "No Name"

#quality of life functions
def drawRect(x, y, width, height, color, br=0):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height), border_radius=br)

def setBackdrop(backdropNum):
    screen.blit(backdrops[backdropNum], (0, 0))

def renderText(inputText, pos, size, fontColor):
    arial = pygame.font.Font('assets/misc/notpiratedfont.ttf', size)
    renderedFont = arial.render(inputText, True, fontColor)
    screen.blit(renderedFont, pos)

def createVarDisplay(val, val2, pos, lens):
    x, y = pos
    len1, len2 = lens
    drawRect(x, y, len1, 30, (230, 240, 255), 5)
    drawRect(x + len1 - len2 - 5, y + 2.5, len2, 25, (255, 140, 26), 5)
    renderText(val + ": ", (x + 2.5, y - 2.5), 20, (0, 0, 0))
    renderText(val2, (x + len1 - len2, y - 2.5), 20, (255, 255, 255))

def rS(spriteNum, pos, scale=1, rotation=0): #render sprite with rotation and scale (optional)
    theSprite = sprites[spriteNum]
    width = theSprite.get_width()
    height = theSprite.get_height()
    toRender = pygame.transform.scale(theSprite, (width * scale, height * scale))
    toRender = pygame.transform.rotate(toRender, rotation)
    screen.blit(toRender, pos)
    #note: scaling too much returns error "pygame.error: Out of memory"


#scenes
if random.randint(0, 1):
    scene0_num = 9
else:
    scene0_num = 15

def scene_init():
    setBackdrop(scene0_num)
    createVarDisplay("Name", playerName, (15, 10), (170, 100))
    createVarDisplay("Day", weekday, (800, 10), (140, 90))
    pygame.display.update()
    pygame.time.wait(2000)

def scene1():
    setBackdrop(11)
    



#game loop
running = True
while running:

    rS(2, (200, 200))
    #clock.tick(30)
    #createVarDisplay("Name", playerName, (15, 10), (170, 100))
    #createVarDisplay("Day", weekday, (800, 10), (140, 90))
    #scene_init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.update()
