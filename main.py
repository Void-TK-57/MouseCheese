import numpy as np 
import sys
import pygame
import json
import random

from player import Player

def draw_map(screen, map_matrix, player):
    for i in range( map_matrix.shape[0] ):
        for j in range( map_matrix.shape[1] ):
            if j == player.x and i == player.y:
                color = (0, 0, 255)
            elif map_matrix[i][j] == -1:
                color = (0, 0, 0)
            elif map_matrix[i][j] == 1:
                color = (0, 255, 0)
            else:
                continue
            x = 360/map_matrix.shape[0]
            y = 360/map_matrix.shape[1]
            rect = pygame.Rect(x*j, i*y, x, y)
            #rect = pygame.Rect(0, 0, 100, 100)
            pygame.draw.rect(screen, color, rect)


def update(screen, map_matrix, player):
    done = player.Q_learn( map_matrix )
    player.log()
    screen.fill( (255, 255, 255) )
    draw_map(screen, map_matrix, player)
    pygame.display.update()
    return done

def main(path):
    # read json
    with open(path) as json_file:
        map_matrix = np.array(json.load(json_file)["map"])

    # init game
    pygame.init()

    # display height and width
    display_height = 360
    disply_width = 360

    screen = pygame.display.set_mode( (disply_width, display_height) )
    pygame.display.set_caption('Mouse Cheese')

    clock = pygame.time.Clock()

    player = Player(0, 0, np.zeros( (map_matrix.shape[0]*map_matrix.shape[1] , 4) )

    done = False

    player.log()
    screen.fill( (255, 255, 255) )
    draw_map(screen, map_matrix, player)
    pygame.display.update()

    # main loop
    while True:
        # for each event
        for event in pygame.event.get():
            # if event is quit, then set alive to false
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN :
                if done != True:
                    done = update(screen, map_matrix, player)
        clock.tick(30)
                
        

    

if __name__ == "__main__":
    main(sys.argv[1])