#THIS IS THE EXPIRIMENTAL SCRIPT
import pygame 
import datetime
import loadassets
import dialogue as d
import random
import threading

print("start")
pygame.init() #initalize pygame
clock = pygame.time.Clock() #for limiting the fps
backdrops, sprites = loadassets.loadAssets() #load assets

screen = pygame.display.set_mode((960, 720)) 

week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weekday = week_days[int(datetime.datetime.now().strftime("%w"))]
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
    return (toRender.get_rect()).move(x, y)
    #note: scaling too much returns error "pygame.error: Out of memory"

mouseClicked = False
def isQuit(rect=None): #background quit function
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                _pass = True
                pass
        if event.type == pygame.QUIT:
            running = False
            print("exit")
            quitThread.join()
            quit()
        if event == pygame.MOUSEBUTTONDOWN and not rect == None:
            mouseClicked = rect.collidepoint(event.pos)


def createTextbox(displayText, sceneNum=1, inputBox=False):
    if inputBox:
        scene(sceneNum)
        text = ''
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #always need a quit option
                    running = False
                    print("exit")
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True
                        return text
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode #the part that actually adds text
                drawRect(152, 400, 656, 50, (0, 255, 0), 5)
                drawRect(154.5, 402.5, 651, 45, (255, 255, 255), 5)
                renderText(displayText, (154.5, 402.5), 25, (0, 0, 0))
                drawRect(152, 463, 656, 50, (0, 255, 255), 5)
                drawRect(154.5, 465.5, 651, 45, (255, 255, 255), 5)
                renderText(text, (154.5, 465.5), 25, (0, 0, 0))
                pygame.display.update()
      
    if not inputBox:
        drawRect(152, 463, 656, 50, (0, 255, 255), 5)
        drawRect(154.5, 465.5, 651, 45, (255, 255, 255), 5)
        renderText(displayText, (154.5, 465.5), 25, (0, 0, 0))


#scenes
if random.randint(0, 1):
    scene0_num = 9
else:
    scene0_num = 15

def scene(num, e_params=0):
    if num == 1:
        setBackdrop(11)
        createVarDisplay("Name", playerName, (15, 10), (170, 100))
        createVarDisplay("Day", weekday, (800, 10), (140, 90))
        rS(8, (390, 465), 0.3 * e_params + 0.35 * (not  e_params))

running = True
quitThread = threading.Thread(target=isQuit)
setBackdrop(scene0_num)
pygame.display.update()
pygame.time.wait(2000)

scene(1)
pygame.time.wait(2000)
for i in range(7):
    scene(1)
    createTextbox(d.scene1[i], 1, False)
    pygame.display.update()
    pygame.time.wait(2000)

playerName = createTextbox(d.scene1[7], 1, True)
createTextbox(d.scene1[8] + playerName + d.scene1[9], 1, False)
pygame.display.update()
pygame.time.wait(2000)
createTextbox(playerName + d.scene1[10], 1, False)
pygame.display.update()
pygame.time.wait(2000)
createTextbox(d.scene1[11], 1, False)
pygame.display.update()
pygame.time.wait(2000)
createTextbox(d.scene1[12], 1, False)
pygame.display.update()

