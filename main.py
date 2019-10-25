import numpy as np 
import pandas as pd
import sys
import pygame
import json
import random
import time

from player import Player


def draw_map(screen, map_matrix, player, font):
    for i in range( map_matrix.shape[0] ):
        for j in range( map_matrix.shape[1] ):
            x = 720/map_matrix.shape[0]
            y = 720/map_matrix.shape[1]
            if j == player.x and i == player.y:
                color = (0, 0, 255)
            elif map_matrix[i][j] == -1:
                color = (0, 0, 0)
            elif map_matrix[i][j] == 1:
                color = (0, 255, 0)
            else:
                direction = player.Q.iloc[i + j*map_matrix.shape[0] ].idxmax()
                value = round(player.Q.iloc[i + j*map_matrix.shape[0] ][direction], 1)
                text = font.render( direction + ":" + str(value), False, (255, 0, 0))
                #textRect = text.get_rect()
                ## cener rect
                #textRect.center = ( x*(j+0.5), y*(i+0.5) )
                #textRect.center = ( 100, 100)
                screen.blit(text, (x*(j+0.2), (i+0.4)*y) )
                continue
            
            rect = pygame.Rect(x*j, i*y, x, y)
            #rect = pygame.Rect(0, 0, 100, 100)
            pygame.draw.rect(screen, color, rect)


def update(screen, map_matrix, player, font):
    done = player.Q_learn( map_matrix )
    player.log()
    screen.fill( (255, 255, 255) )
    draw_map(screen, map_matrix, player, font)
    pygame.display.update()
    return done

def main(path):
    # read json
    with open(path) as json_file:
        dict_file = json.load(json_file)
        map_matrix = np.array(dict_file["map"])
        rewards = np.array(dict_file["rewards"])
    done = False

    # init game
    pygame.init()
    clock = pygame.time.Clock()

    # display height and width
    display_height = 720
    disply_width = 720

    screen = pygame.display.set_mode( (disply_width, display_height) )
    pygame.display.set_caption('Mouse Cheese')
    font_name = pygame.font.get_default_font()
    print(font_name)
    font = pygame.font.SysFont( font_name , 20)


    q_matrix = np.zeros( (map_matrix.shape[0]*map_matrix.shape[1] , 4) )
    index = []
    columns = ["up", "right", "down", "left"]
    # create index
    for i in range(map_matrix.shape[0]):
        for j in range(map_matrix.shape[1]):
            index.append(str(i)+"-"+str(j))
    q_matrix = pd.DataFrame(q_matrix, index = index, columns = columns)

    player = Player(0, 0,  q_matrix, rewards )

    paused = False

    # main loop
    while True:
        # for each event
        for event in pygame.event.get():
            # if event is quit, then set alive to false
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN :
                paused = not paused
        if not paused:
            done = update(screen, map_matrix, player, font)
            if done == True:
                time.sleep(3)
            if done is not None:
                # reset position
                player.x = 0
                player.y = 0

        clock.tick(30)
                
        

    

if __name__ == "__main__":
    main(sys.argv[1])