import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

pygame.init()
running = True
# screen = pygame.display.set_mode((800, 800)) <- fixed screen size
# adapts to screen size
screen = pygame.display.set_mode(size)
# set title
pygame.display.set_caption("Car Game")
# bg color
screen.fill((60, 220, 0))

# apply changes
pygame.display.update()

# load images
girl = pygame.image.load("car.png")
girl_loc = girl.get_rect()
girl_loc.center = right_lane, height*0.8

ghost = pygame.image.load("otherCar.png")
ghost_loc = ghost.get_rect()
ghost_loc.center = left_lane, height*0.2

counter = 0
# game loop
while running:
    counter += 1
    if counter == 5024:
        speed += 0.15
        counter = 0
        print("Level Up!", speed)
    # enemy code
    ghost_loc[1] += speed
    # 1 --> selects y-coord, adds 1 to its coord each time while loop completed
    # random right/left generation
    if ghost_loc[1] > height:
        if random.randint(0, 1) == 0:
            ghost_loc.center = right_lane, -200
        else:
            ghost_loc.center = left_lane, -200
    # end game
    if girl_loc[0] == ghost_loc[0] and ghost_loc[1] > girl_loc[1]-250: #-250 because dealing with centers of objs
        print("YOU LOSE!")
        break
    # draw graphics
    # road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width / 2 - road_w / 2, 0, road_w, height)
        #  (x-coord to start drawing rect, y-coord, width, height)
    )
    # center line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width / 2 - roadmark_w / 2, 0, roadmark_w, height)
    )
    # white lines
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height)
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height)
    )
    # event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                girl_loc = girl_loc.move([-int(road_w/2), 0])
                # girl_loc[0] -= 1
            if event.key in [K_d, K_RIGHT]:
                girl_loc = girl_loc.move([int(road_w/2), 0])
                # girl_loc[0] += 1
    # draw images
    screen.blit(girl, girl_loc)
    screen.blit(ghost, ghost_loc)
    pygame.display.update()

pygame.quit()