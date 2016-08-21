#snow is code from a tutorial

import pygame
import random

pygame.init()

black = [0, 0, 0]
white = [255, 255, 255]
red = [200, 0, 0]
blue = [100, 240, 212]
pink = [230, 0, 160]
orange = [210, 100, 0]
brown = [139, 69, 19]
dark_green = [0, 100, 0]
yellow = [255, 215, 0]
green = [0, 255, 0]

size = [400, 400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")

star_list = []

for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    star_list.append([x,y])

clock = pygame.time.Clock()

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)

    for i in range(len(star_list)):
        pygame.draw.circle(screen, white, star_list[i], 2)
        star_list[i][1]+=1

        if star_list[i][1] >400:
            y = random.randrange(-50, -10)
            star_list[i][1] = y
            x = random.randrange(0, 400)
            star_list[i][0] = x

        #draws house
        pygame.draw.rect(screen, red, [150, 300, 75, 100])
        
        #roof
        pygame.draw.polygon(screen, orange, [[150, 300], [224, 300], [187, 247]])
        
        #windows and door
        pygame.draw.rect(screen, blue, [163, 325, 10, 15])
        pygame.draw.rect(screen, blue, [200, 325, 10, 15])
        pygame.draw.rect(screen, blue, [163, 375, 10, 15])
        pygame.draw.rect(screen, blue, [200, 375, 10, 15])
        pygame.draw.rect(screen, brown, [180, 370, 14, 30])
        
        #trees
        pygame.draw.polygon(screen, dark_green, [[350, 400], [335, 325], [320, 400]])
        pygame.draw.polygon(screen, dark_green, [[90, 400], [105, 325], [120, 400]])
        pygame.draw.polygon(screen, dark_green, [[20, 400], [35, 325], [50, 400]])
        
        #snowman
        pygame.draw.circle(screen, white, [260, 395], 10, 0)
        pygame.draw.circle(screen, white, [260, 382], 7, 0)
        pygame.draw.circle(screen, black, [262, 381], 1, 0)
        pygame.draw.circle(screen, black, [258, 381], 1, 0)
        
        #moon
        pi = 3.14
        pygame.draw.arc(screen, yellow,  [30, 20, 60, 75],  pi, 3* pi / 2, 4)
            


                    

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
