import pygame

pygame.init()
pygame.display.init()

def SettingWindow():
    (width,height) = 460,460
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")

def StartingWindow():
    isRunning = True
    activeCoordinateLeft = 0
    activeCoordinateTop = 0
    pygame.display.flip()
    while isRunning:
        # print(pygame.mouse.get_pos())
        # Updates frames of rectangles changing color to orange
        # and on mouse away changing back to white rect
        for element in rectList:
            if element.left == activeCoordinateLeft and element.top == activeCoordinateTop:
                pygame.draw.rect(screen, red, pygame.Rect(element.left, element.top, 40, 40), 3)
                pygame.display.update()
            else:
                if element.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, orange, pygame.Rect(element.left,element.top,40,40),3)
                    pygame.display.update()
                else:
                    pygame.draw.rect(screen, white, pygame.Rect(element.left, element.top, 40, 40))
        # Activates rectangle changing color to red
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for element in rectList:
                    if element.collidepoint(pygame.mouse.get_pos()):
                        activeCoordinateLeft = element.left
                        activeCoordinateTop = element.top
                        pygame.draw.rect(screen, red, pygame.Rect(element.left, element.top, 40, 40), 3)
                        pygame.display.update()
            # Makes closing window available
            if event.type == pygame.QUIT:
                isRunning = False
            if isRunning == False:
                pygame.quit()

def SettingColors():
    global orange
    global white
    global red
    global black
    black = (0,0,0)
    red = (255,0,0)
    orange = (255,165,0)
    white = (255, 255, 255)

SettingColors()
SettingWindow()

def DrawingBoard():
    global rectList
    rectList = []
    x = 40
    y = 40
    inside = 42
    devide = 44
    # Draws from right to left and adds rectangles to list the same way
    for col in range(1,10):
        for row in range(1,9):
            if row == 1:
                pygame.draw.rect(screen,white,pygame.Rect(x,y,40,40))
                rectList.append(pygame.Rect(x,y,40,40))
            if row % 3 == 0:
                pygame.draw.rect(screen,white,pygame.Rect(x+devide,y,40,40))
                rectList.append(pygame.Rect(x,y,40,40))
                x+=devide
            else:
                pygame.draw.rect(screen,white,pygame.Rect(x+inside,y,40,40))
                rectList.append(pygame.Rect(x,y,40,40))
                x+=inside
        if col % 3 == 0:
            rectList.append(pygame.Rect(x, y, 40, 40))
            y+=devide
        else:
            rectList.append(pygame.Rect(x, y, 40, 40))
            y+=inside
        x = 40

    # I know something higher is wrong and it adds 9 more rectangles but
    # I created this wonderful piece of code that removes it :)
    top = 0
    for el in rectList:
        if el.left == 40 and el.top == top:
            rectList.remove(el)
        else:
            top = el.top

DrawingBoard()

StartingWindow()




