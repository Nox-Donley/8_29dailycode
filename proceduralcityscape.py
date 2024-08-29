import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Procedural Cityscape")

# Function to draw a building with random features
def draw_building():
    xpos = random.randrange(-100, 800)
    ypos = random.randrange(0, 800)
    width = random.randrange(100, 200)
    color = random.randrange(50, 200)
    pygame.draw.rect(screen, (color, color, color), (xpos, ypos, width, 800)) #building
    pygame.draw.rect(screen, (0,0,0), (xpos, ypos, width, 800), 2) #black outline
    for i in range (xpos+10, xpos + width - 20, 30):
        for j in range(ypos + 10, ypos + 600, 60):
            pygame.draw.rect(screen, (200, 200, 50), (i, j, 20, 40))#windows

def draw_clouds():
    xpos = random.randrange(-100, 900)
    ypos = random.randrange(-100, 100)
    radius = random.randrange(25, 75)
    pygame.draw.circle(screen, (210, 210, 210), (xpos, ypos), radius)

def draw_rain():
    xpos = random.randrange(-100, 800)
    ypos = random.randrange(0, 800)
    pygame.draw.rect(screen, (0,0,130), (xpos, ypos, 3, 20)) #building

screen.fill((20, 20, 100))
for i in range(20):
    draw_clouds()
    draw_clouds()
    draw_building()   
    draw_building() 
    draw_building() 
    draw_clouds()
    draw_clouds()
    draw_rain()
    draw_rain()
    draw_rain()
    draw_rain()
    draw_rain()


pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()
