import pygame
SCREEN_WIDTH,SCREEN_HEIGHT=(1000,600)
WIDTH,HEIGHT=(600,600)
ROWS,COLS=8,8
SQUARE_SIZE=WIDTH//COLS

#rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
VOILET=(224, 64, 251)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))