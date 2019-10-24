import numpy as np 
import sys
import pygame
import json

def draw_map(screen, map_matrix):
    screen.fill( (255, 255, 255) )
    for i in range( map_matrix.shape[0] ):
        for j in range( map_matrix.shape[1] ):
            pass

def main(path):
    # read json
    with open(path) as json_file:
        map_matrix = np.array(json.load(json_file)["map"])

    print(map_matrix)

    # init game
    pygame.init()

    # display height and width
    display_height = 600
    disply_width = 600

    screen = pygame.display.set_mode( (disply_width, display_height) )
    pygame.display.set_caption('Mouse Cheese')

    clock = pygame.time.Clock()


    # main loop
    while True:
        # for each event
        for event in pygame.event.get():
            # if event is quit, then set alive to false
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                pass
    
        clock.tick(30)

    

if __name__ == "__main__":
    main(sys.argv[1])