import pygame
import math
import random

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
    pygame.display.set_caption("How fast?")
    numTargets = 3
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Click on the ' + str(numTargets) + " targets as fast as you can", True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    screen.blit(text, textRect)
    rectList = []
    running  = True
    for i in range(0,numTargets):
            rect = generateRandRect()
            rectList.append(rect)
            pygame.draw.rect(screen, GREEN, rect, 0)
            pygame.display.update()

    start = pygame.time.get_ticks()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    for rectangle in rectList:
                        if rectangle.collidepoint(pos):
                            rectList.remove(rectangle)
                            screen.fill(BLACK)
                            for rect in rectList:
                                pygame.draw.rect(screen, GREEN, rect, 0)
                            pygame.display.update()
                            numTargets -= 1
                if numTargets == 0:
                    total_time = (pygame.time.get_ticks() - start) / 1000
                    running = False
                    print(str(total_time) + " seconds")
                    break
           
def generateRandRect():
    width = random.randint(50,100)
    height = width
    left = random.randint(0, WINDOW_WIDTH - width)
    top = random.randint(0, WINDOW_HEIGHT - height)

    return pygame.Rect(left, top, width, height)

main()