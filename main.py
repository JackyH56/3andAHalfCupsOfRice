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
FONT_SIZE = 32
TIME_DELAY = 3000

def main():
    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Mouse Sensitivity Calibrator")
    numTargets = 5
    imageList = []
    running  = True
    completed = False
    accurateClicks = 0
    totalClicks = 0
    displayInstructions(screen, font, numTargets)
    pygame.display.update()
    setupTime = pygame.time.get_ticks()
    #pause 3 seconds before starting
    pygame.time.wait(TIME_DELAY)
    clearScreen(screen)
    #draw rectangles
    iconList = ["icon-bhotify.png", "icon-bone-bhote.png", "icon-booble-bhrome.png", "icon-recycle.png"]
    for i in range(numTargets):
        image = pygame.image.load(random.choice(iconList)).convert()
        icon_width = 95
        icon_height = 96
        coord = generateRandCoord(95, 96)
        imageList.append((image, pygame.Rect(coord[0],coord[1], icon_width, icon_height)))
        screen.blit(image, coord)
    pygame.display.update()
    start = pygame.time.get_ticks() - setupTime
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif not completed:
                displayTimer(screen, font)
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONUP:
                    totalClicks += 1
                    for image in imageList:
                        if image[1].collidepoint(pos):
                            accurateClicks += 1
                            imageList.remove(image)
                            clearScreen(screen)
                            for image in imageList:
                                screen.blit(image[0], (image[1][0],image[1][1]))
                                # pygame.draw.rect(screen, GREEN, rect, 0)
                            pygame.display.update()
                            numTargets -= 1
                            if numTargets == 0:
                                total_time = (pygame.time.get_ticks() - start)
                                completed = True
                                accuracy = (accurateClicks / totalClicks) * 100
                                stopTimer(screen, font, total_time)
                                displayAccuracy(screen, font, accuracy)
            else:
                continue

def generateRandCoord(width, height):
    x = random.randint(0, WINDOW_WIDTH - width)
    y = random.randint(0, WINDOW_HEIGHT - height)
    return (x,y)
#returns a random pygame.rect object
def generateRandRect():
    width = random.randint(50,100)
    height = width
    left = random.randint(0, WINDOW_WIDTH - width)
    top = random.randint(0, WINDOW_HEIGHT - height)

    return pygame.Rect(left, top, width, height)

def displayInstructions(screen, font, numTargets):
    text1 = font.render('Click on the ' + str(numTargets) + " targets as fast as you can", True, GREEN, BLACK)
    text1Rect = text1.get_rect()
    text1Rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    screen.blit(text1, text1Rect)
    
    text2 = font.render('Get ready...', True, GREEN, BLACK)
    text2Rect = text2.get_rect()
    text2Rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 + FONT_SIZE)
    screen.blit(text2, text2Rect)

    return

def displayTimer(screen, font):
    pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH-100,0,100,50))
    text = font.render("%d"%(pygame.time.get_ticks() - TIME_DELAY), True, WHITE, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_WIDTH-text_rect.width//2, 30)
    screen.blit(text, text_rect)
    pygame.display.update()
    
    return

def stopTimer(screen, font, time):
    pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH-100,0,100,50))
    text = font.render(str(time), True, WHITE, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_WIDTH-text_rect.width//2, 30)
    screen.blit(text, text_rect)
    pygame.display.update()

    return

def displayAccuracy(screen, font, accuracy):
    text = font.render("Accuracy: {:.2f}%".format(accuracy), True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    screen.blit(text, textRect)
    pygame.display.update()

def clearScreen(screen):
    screen.fill(BLACK)

    return

main()