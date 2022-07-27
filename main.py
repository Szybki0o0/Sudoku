import random

import pygame
import math

pygame.init()
pygame.display.init()


def SettingWindow():
    (width, height) = 460, 460
    global screen
    global font
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    font = pygame.font.Font(None, 45)


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
                    pygame.draw.rect(screen, orange, pygame.Rect(element.left, element.top, 40, 40), 3)
                    pygame.display.update()
                else:
                    pygame.draw.rect(screen, white, pygame.Rect(element.left, element.top, 40, 40), 3)
        # Activates rectangle changing color to red
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for element in rectList:
                    if element.collidepoint(pygame.mouse.get_pos()):
                        activeCoordinateLeft = element.left
                        activeCoordinateTop = element.top
                        pygame.draw.rect(screen, red, pygame.Rect(element.left, element.top, 40, 40), 3)
                        pygame.display.update()
            # Inserts numbers to rectangles and overwrite old numbers looping through numbers 1-9
            if event.type == pygame.KEYDOWN:
                for i in range(1, 10):
                    if event.key == i + 48:
                        if rectDict[str(activeCoordinateLeft) + str(activeCoordinateTop)] != 0:
                            pygame.draw.rect(screen, white, pygame.Rect(activeCoordinateLeft + 12, activeCoordinateTop + 7, 20, 25))
                        screen.blit(font.render(f"{i}", True, black), (activeCoordinateLeft + 12, activeCoordinateTop + 7))
                        rectDict[str(activeCoordinateLeft) + str(activeCoordinateTop)] = i
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
    black = (0, 0, 0)
    red = (255, 0, 0)
    orange = (255, 165, 0)
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
    for col in range(1, 10):
        for row in range(1, 9):
            if row == 1:
                pygame.draw.rect(screen, white, pygame.Rect(x, y, 40, 40))
                rectList.append(pygame.Rect(x, y, 40, 40))
            if row % 3 == 0:
                pygame.draw.rect(screen, white, pygame.Rect(x + devide, y, 40, 40))
                rectList.append(pygame.Rect(x, y, 40, 40))
                x += devide
            else:
                pygame.draw.rect(screen, white, pygame.Rect(x + inside, y, 40, 40))
                rectList.append(pygame.Rect(x, y, 40, 40))
                x += inside
        if col % 3 == 0:
            rectList.append(pygame.Rect(x, y, 40, 40))
            y += devide
        else:
            rectList.append(pygame.Rect(x, y, 40, 40))
            y += inside
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
rectDict = {}
rectListVertical = []
rectListHorizontal = []
rectListBoxed = []
# Creates dictionary of numbers in speciffic rectangles
for rect in rectList:
    cords = str(rect.left) + str(rect.top)
    # cords = int(cords)
    rectDict[cords] = 0

# Creates list of cords of rectangles in horizontal order
for rect in rectDict:
    rectListHorizontal.append(rect)

# Creates list of cords of rectangles in vertical order
def VerticalOrder():
    tile = 1
    verticalTile = 1
    for col in range(1, 10):
        for rect in rectDict:
            if tile == col:
                rectListVertical.append(rect)
            if tile == col + (verticalTile * 9):
                rectListVertical.append(rect)
                verticalTile += 1
            tile += 1
        tile = 1
        verticalTile = 1
VerticalOrder()

# Creates list of cords of rectangles in boxes horizontally
def BoxedOrder():
    i = 1
    firstList = []
    secondList = []
    thirdList = []
    for rect in rectListHorizontal:
        if i <= 27:
            firstList.append(rect)
        elif 27 < i <= 54:
            secondList.append(rect)
        else:
            thirdList.append(rect)
        i+=1

    tile = 1
    boxedTile = 1
    for col in range(1, 10):
        for rect in firstList:
            if tile == col:
                rectListBoxed.append(rect)
            if tile == col + (boxedTile * 9):
                rectListBoxed.append(rect)
                boxedTile += 1
            tile += 1
        tile = 1
        boxedTile = 1

    for col in range(1, 10):
        for rect in secondList:
            if tile == col:
                rectListBoxed.append(rect)
            if tile == col + (boxedTile * 9):
                rectListBoxed.append(rect)
                boxedTile += 1
            tile += 1
        tile = 1
        boxedTile = 1

    for col in range(1, 10):
        for rect in thirdList:
            if tile == col:
                rectListBoxed.append(rect)
            if tile == col + (boxedTile * 9):
                rectListBoxed.append(rect)
                boxedTile += 1
            tile += 1
        tile = 1
        boxedTile = 1
BoxedOrder()

# screen.blit(font.render("1",True,black),(rectList[0].left+12,rectList[0].top+7))

# print(rectDict.keys())


# Generates board with random numbers
def GeneratingBoard():
    maxRects = 30
    isRightNumber = False
    for i in range(1,maxRects+1):
        randomIndex = random.randint(0,80)
        while isRightNumber == False:
            if rectDict[rectListHorizontal[randomIndex]] == 0:
                randomNumber = random.randint(1,9)
                rectDict[rectListHorizontal[randomIndex]] = randomNumber
                if CheckingCorectness(rectListHorizontal[randomIndex]):
                    isRightNumber = True
                    cordLeft = 0
                    cordTop = 0
                    if rectListHorizontal[randomIndex][0] == '4' or rectListHorizontal[randomIndex][0] == '8':
                        cordLeft = int(rectListHorizontal[randomIndex][0:2])
                        cordTop = int(rectListHorizontal[randomIndex][2:])
                        # print(cordLeft,cordTop,rectListHorizontal[randomIndex])
                    else:
                        cordLeft = int(rectListHorizontal[randomIndex][0:3])
                        cordTop = int(rectListHorizontal[randomIndex][3:])
                        # print(cordLeft,cordTop,rectListHorizontal[randomIndex])
                    screen.blit(font.render(f"{randomNumber}", True, black), (cordLeft + 12, cordTop+ 7))
                    # print(rectDict)
            else:
                randomIndex = random.randint(0, 80)
        isRightNumber = False
# Function responsible for checking correctness of inputs on the board
def CheckingCorectness(key):
    truthIndex = 0
    # HORIZONTAL CHECK

    # Gathering data
    tempHorizontalList = []
    horizontalIndex = rectListHorizontal.index(key) + 1
    horizontalLineIndex = math.ceil(horizontalIndex / 9)
    horizontalLastTileIndex = horizontalLineIndex * 9
    horizontalFirstTIleIndex = horizontalLastTileIndex - 8

    # Creating temporary list of 8 rectangles in line
    h = 1
    for rect in rectListHorizontal:
        if horizontalLastTileIndex >= h >= horizontalFirstTIleIndex:
            tempHorizontalList.append(rect)
        h += 1
    tempHorizontalList.remove(key)

    # Checking correctness
    for rect in tempHorizontalList:
        if rectDict[rect] == rectDict[key]:
            truthIndex += 1
    # VERTICAL CHECK

    # Gathering data
    tempVerticalList = []
    verticalIndex = rectListVertical.index(key) + 1
    verticalLineIndex = math.ceil(verticalIndex / 9)
    verticalLastTileIndex = verticalLineIndex * 9
    verticalFirstTIleIndex = verticalLastTileIndex - 8

    # Creating temporary list of 8 rectangles in line
    v = 1
    for rect in rectListVertical:
        if verticalLastTileIndex >= v >= verticalFirstTIleIndex:
            tempVerticalList.append(rect)
        v += 1
    tempVerticalList.remove(key)

    # Checking correctness
    for rect in tempVerticalList:
        if rectDict[rect] == rectDict[key]:
            truthIndex += 1
    # BOXED CHECK

    # Gathering data
    tempBoxedList = []
    boxedIndex = rectListBoxed.index(key) + 1
    boxIndex = math.ceil(boxedIndex / 9)
    boxedLastTileIndex = boxIndex * 9
    boxedFirstTIleIndex = boxedLastTileIndex - 8

    # Creating temporary list of 8 rectangles in box
    b = 1
    for rect in rectListBoxed:
        if boxedLastTileIndex >= b >= boxedFirstTIleIndex:
            tempBoxedList.append(rect)
        b += 1
    tempBoxedList.remove(key)

    # Checking correctness
    for rect in tempBoxedList:
        if rectDict[rect] == rectDict[key]:
            truthIndex += 1

    # FINAL CHECK
    if truthIndex == 0:
        return True
    else:
        return False


GeneratingBoard()
# print(CheckingCorectness('168124'))
StartingWindow()
