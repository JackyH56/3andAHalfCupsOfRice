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
                if minigame1(screen, event): # clicking the rec
                    screen.fill(BLACK)
                    pygame.display.update()
                # minigame2(screen, event) # clicking 4 corners real fast 
                # minigame3() # aimlab
                # minigame5() # 
                # minigame6()
                # minigame7()
                # minigame8()
                # minigame9()
                # minigame10()
            
def minigame1(screen, event):
    width = 50
    height = 50
    pos = pygame.mouse.get_pos()
    rect = pygame.Rect(WINDOW_WIDTH/2 - width, WINDOW_HEIGHT / 2 - height, width, height)
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
    

    return

def mingame3(screen, event):
    left = random.randint(0, WINDOW_WIDTH)
    top = random.randint()
main()