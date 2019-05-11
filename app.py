import pygame
import math
import sys
# INITIAL STATE
state = {'altitude': 490, 'fuel': 1000,  'speed': 0, 'timer': 0}

step = 0.001


def gravity():
    # A(t) = 9.8
    state['speed'] -= 9.8 * step
    state['altitude'] += state['speed'] * step


def boost():
    # A(t) = 9.8 - 50 = 40.2
    state['speed'] += 40.2 * step
    state['altitude'] += state['speed'] * step
    state['fuel'] -= 0.1


def get_triangle_cords(x, y, r=10):
    return [(x, y - r), (x + r*math.cos(math.pi*(5/4)), y - r*math.sin(math.pi*(5/4))), (x + r*math.cos(math.pi*(7/4)), y - r*math.sin(math.pi*(7/4)))]


pygame.init()

pygame.font.init()

myfont = pygame.font.SysFont('Arial', 15)

size = width, height = 200, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while(True):
    # RUN GRAPHICS USING STATE
    screen.fill(black)

    altitude_text = myfont.render(
        'altitude: ' + str(round(state['altitude'])), False, (255, 255, 255))

    fuel_text = myfont.render(
        'fuel: ' + str(round(state['fuel'])), False, (255, 255, 255))

    speed_text = myfont.render(
        'speed: ' + str(round(state['speed'])), False, (255, 255, 255))

    screen.blit(altitude_text, (0, 0))
    screen.blit(fuel_text, (0, 20))
    screen.blit(speed_text, (0, 40))

    pygame.draw.line(screen, (255, 255, 255), (0, 490), (500, 490))

    pygame.draw.polygon(screen, (255, 255, 255), [(round(triangle[0]), round(triangle[1])) for triangle in get_triangle_cords(
        100, 500 - state['altitude'])], 1)

    pygame.display.flip()

    # CONTROLS

    if pygame.time.get_ticks() > state['timer']:
        state['timer'] += 1
        if pygame.key.get_pressed()[273] and state['fuel'] > 0:
            boost()
        else:
            gravity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # END
    if get_triangle_cords(100, 500 - state['altitude'])[1][1] > 490:
        if abs(state['speed']) < 5:
            print('SUCCESS')
        else:
            print('FAIL')
        sys.exit()
