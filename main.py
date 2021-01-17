import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1000

def main():

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("BDE")

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                # if minigame1(screen, event): # clicking the rec
                #     screen.fill(BLACK)
                #     pygame.display.update()
                # minigame2(screen, event) # clicking 4 corners real fast

                if minigame3(screen, event):
                    break
                # minigame5() # 
                # minigame6()
                # minigame7()
                # minigame8()
                # minigame9()
                # minigame10()
        break
            
def minigame1(screen, event):
    width = 50
    height = width
    pos = pygame.mouse.get_pos()
    rect = pygame.Rect(WINDOW_WIDTH / 2 - width, WINDOW_HEIGHT / 2 - height, width, height)
    pygame.draw.rect(screen, GREEN, rect, 0)
    if rect.collidepoint(pos):
        pygame.draw.rect(screen, RED, rect, 0)
        pygame.display.update()
        if (event.type == pygame.MOUSEBUTTONUP):
            return True
    else:
        pygame.draw.rect(screen, GREEN, rect, 0)
        pygame.display.update()

def minigame2(screen, event):
    width = 50
    height = width
    counter = 0
    pos = pygame.mouse.get_pos()
    rectTopLeft = pygame.Rect(0, 0, width, height)
    rectTopRight = pygame.Rect(WINDOW_WIDTH - width, 0, width, height)
    rectBottomLeft = pygame.Rect(0, WINDOW_HEIGHT - height, width, height)
    rectBottomRight = pygame.Rect(WINDOW_WIDTH - width, WINDOW_HEIGHT - height, width, height)

    pygame.draw.rect(screen, GREEN, rectTopLeft, 0)
    pygame.draw.rect(screen, GREEN, rectTopRight, 0)
    pygame.draw.rect(screen, GREEN, rectBottomLeft, 0)
    pygame.draw.rect(screen, GREEN, rectBottomRight, 0)
    pygame.display.update()


    if rectTopLeft.collidepoint(pos):
        pygame.draw.rect(screen, RED, rectTopLeft, 0)
        pygame.display.update()
        if (event.type == pygame.MOUSEBUTTONUP):
            pygame.draw.rect(screen, BLACK, rectTopLeft, 0)
            pygame.display.update()
            counter += 1 
            if counter == 4:      
                return

    if rectTopRight.collidepoint(pos):
        pygame.draw.rect(screen, RED, rectTopRight, 0)
        pygame.display.update()
        if (event.type == pygame.MOUSEBUTTONUP):
            pygame.draw.rect(screen, BLACK, rectTopRight, 0)
            pygame.display.update()
            counter += 1 
            if counter == 4:      
                return

    if rectBottomLeft.collidepoint(pos):
        pygame.draw.rect(screen, RED, rectBottomLeft, 0)
        pygame.display.update()
        if (event.type == pygame.MOUSEBUTTONUP):
            pygame.draw.rect(screen, BLACK, rectBottomLeft, 0)
            pygame.display.update()
            counter += 1 
            if counter == 4:      
                return

    if rectBottomRight.collidepoint(pos):
        pygame.draw.rect(screen, RED, rectBottomRight, 0)
        pygame.display.update()
        if (event.type == pygame.MOUSEBUTTONUP):
            pygame.draw.rect(screen, BLACK, rectBottomRight, 0)
            pygame.display.update()
            counter += 1 
            if counter == 4:      
                return

def minigame3(screen, event):
    rectList = []
    counter = 0
    for i in range(0,4):
        rect = generateRandRect()
        rectList.append(rect)

        pos = pygame.mouse.get_pos()
        pygame.draw.rect(screen, GREEN, rect, 0)
        pygame.display.update()
        for rectangle in rectList:
            if rectangle.collidepoint(pos):
                pygame.draw.rect(screen, RED, rect, 0)
                pygame.display.update()
                if (event.type == pygame.MOUSEBUTTONUP):
                    counter += 1
            else:
                pygame.draw.rect(screen, GREEN, rect, 0)
                pygame.display.update()
    if counter == 5:
        return True

def generateRandRect():
    width = random.randint(50,100)
    height = width
    left = random.randint(0, WINDOW_WIDTH - width)
    top = random.randint(0, WINDOW_HEIGHT - height)
    return pygame.Rect(left, top, width, height)

main()