import pygame
# INITIAL STATE (DIRECTION IS IN DEGREES WITH 90 FACING UP)
state = {'score': 0, 'time': 0, 'fuel': 1000, 'altitude': 400,
         'horizontal_speed': 400, 'vertical_speed': 0, 'direction': 90}


def accelerate_vertical:
    # PHYSICS


pygame.init()

size = width, height = 500, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while(True):
    # RUN GRAPHICS USING STATE

    # UPDATE STATE DEPENDING ON PHYISICS
    accelerate_vertical()

    # CONTROLS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN
        if event.key == pygame.K_LEFT:
                # ROTATE LEFT
            if event.key == pygame.K_RIGHT:
                # ROTATE LEFT
            if event.key == pygame.K_UP:
                # ROTATE LEFT
            if event.key == pygame.K_s:
                # SPEED UP THE GAME
