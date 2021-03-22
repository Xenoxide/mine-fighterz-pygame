### main issue: audio files will not load ###

import pygame # .pylintrc file is to load the C extensions
import datetime
import loadassets
import dialogue
import random

pygame.init() #initalize pygame
clock = pygame.time.Clock() #for limiting the fps
backdrops, sprites = loadassets.loadAssets() #load assets


# I don't know why I have to multiply by two, otherwise it won't fit
screen = pygame.display.set_mode((480 * 2, 360 * 2)) 

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday = week_days[datetime.date(2020,7,24).weekday()]
playerName = "No Name"

#set icon/caption
pygame.display.set_caption("Mine Fighterz!")
pygame.display.set_icon(sprites[13])

#quality of life functions
def drawRect(x, y, width, height, color, br=0):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height), border_radius=br)

def setBackdrop(backdropNum):
    screen.blit(backdrops[backdropNum], (0, 0))

def renderText(inputText, pos, size, fontColor):
    arial = pygame.font.Font('assets/misc/notpiratedfont.ttf', size)
    renderedFont = arial.render(inputText, True, fontColor)
    screen.blit(renderedFont, pos)

def gPrint(inputText, width, pos):
    x, y = pos
    drawRect(x, y, width + 5, 30, (255, 255, 255))
    renderText(inputText, (x + 2.5, y), 25, (0, 0, 0))

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
    x, y = pos
    toRender = pygame.transform.scale(
        theSprite, 
        (int(float(width) * scale), 
        int(float(height) * scale))
    )
    toRender = pygame.transform.rotate(toRender, rotation)
    screen.blit(toRender, (x, y))
    #note: scaling too much returns error "pygame.error: Out of memory"

def xCheck(bool1, bool2): #exclusive check (1 and 10 never happen for both)
    if not bool1 and not bool2:
        return 0
    if bool1 and not bool2:
        return 1
    if bool2 and not bool1:
        return 10
    if bool1 and bool2:
        return 11

def waitToPass(): #wait for the user to press space
    _pass = False
    while not _pass:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    _pass = True
                    pass

                arrowCheck = xCheck(event.key == pygame.K_LEFT, event.key == pygame.K_RIGHT)
                if arrowCheck == 1:
                    print('')
                if arrowCheck == 10:
                    print('')
            if event.type == pygame.QUIT:
                running = False
                quit()

#scenes
if random.randint(0, 1):
    scene0_num = 9
else:
    scene0_num = 15

running = True
setBackdrop(scene0_num)
createVarDisplay("Name", playerName, (15, 10), (170, 100))
createVarDisplay("Day", weekday, (800, 10), (140, 90))
pygame.display.update()
waitToPass()

setBackdrop(11)
rS(8, (390, 465), 0.4)
pygame.display.update()
pygame.time.wait(2000)
waitToPass()
for i in range(7):
    setBackdrop(11)
    rS(8, (390, 465), 0.4)
    gPrint(dialogue.scene1[i], 50, (400, 400))
    pygame.display.update()
    waitToPass()
