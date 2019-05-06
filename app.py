import pygame
# INITIAL STATE (POSITION IS MEASURED FROM THE TOP LEFT CORNER, DIRECTION IS IN DEGREES WITH 90 FACING UP)
state = {'pos_x': 10, 'pos_y': 10, 'score': 0, 'time': 0, 'fuel': 1000,
         'altitude': 400, 'vertical_speed': 0, 'boost_duration': 0}


def accelerate_vertical():
    # PHYSICS


def hacer_cosas():
    # BOOST


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hacer_cosas()
        else:
            # RESET DURATION
