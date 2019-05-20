import pygame as pg
import math
import sys
import numpy as np
from operator import attrgetter

# INITIAL STATE
state = {'timer': 0}

step = 0.001

number_of_specimen = 100

sequence_size = 300000

generation_colors = ['white', 'blue', 'red',
                     'yellow', 'green', 'purple', 'pink']

current_generation = 0


class Specimen:
    def __init__(self, sequence=None):
        self.altitude = 490
        self.fuel = 1000
        self.speed = 0
        self.color = generation_colors[(current_generation-1) % 7]
        if sequence is None:
            self.sequence = generate_sequence(sequence_size)
        else:
            self.sequence = sequence
        self.test_result = None

    def gravity(self):
        # A(t) = 9.8
        self.speed -= 9.8 * step
        self.altitude += self.speed * step

    def boost(self):
        # A(t) = 9.8 - 50 = 40.2
        self.speed += 40.2 * step
        self.altitude += self.speed * step
        self.fuel -= 0.1


def generate_sequence(size):
    p_false = np.random.random()
    return np.random.choice(a=[False, True], size=size, p=[p_false, 1 - p_false])


def generate_specimina(size=100):
    specimina = []
    for i in range(size):
        specimina.append(Specimen())
    return specimina


def generate_next_specimina():
    # GETTING TOP 10 BEST PERFORMING SPECIMEN
    best_specimina = []
    for i in range(10):
        best_specimen = max(previous_specimina, key=attrgetter('test_result'))
        best_specimina.append(best_specimen)
        print(str(i + 1) + '. ' + str(best_specimen.test_result))
        previous_specimina.remove(best_specimen)

    # COPYING OVER 10 SPECIMEN FROM PREVIOUS GENERATION AT RANDOM
    for i in range(10):
        specimen = np.random.choice(previous_specimina)
        previous_specimina.remove(specimen)
        specimen.speed = 0
        specimen.fuel = 1000
        specimen.altitude = 490
        specimina.append(specimen)

    # GENERATING NEW SPECIMEN FROM TOP 10 BEST PERFORMING SPECIMEN OF LAST GENERATION
    for i in range(90):
        dad = np.random.choice(best_specimina)
        mom = np.random.choice(best_specimina)
        n = np.random.randint(sequence_size)
        specimina.append(
            Specimen(sequence=np.append(dad.sequence[:n], mom.sequence[n:])))

    # MUTATION
    noise = np.random.rand(sequence_size)
    for i, n in enumerate(noise):
        if n < 0.5:
            specimina[99].sequence[i] = False
        elif n > 0.90:
            specimina[99].sequence[i] = True
        specimina[99].color = 'orange'


current_generation += 1

specimina = generate_specimina(size=number_of_specimen)

previous_specimina = []


def get_triangle_cords(x, y, r=10):
    return [(x, y - r), (x + r*math.cos(math.pi*(5/4)), y - r*math.sin(math.pi*(5/4))), (x + r*math.cos(math.pi*(7/4)), y - r*math.sin(math.pi*(7/4)))]


pg.init()

pg.font.init()

myfont = pg.font.SysFont('Arial', 15)

size = width, height = 500, 500
black = 0, 0, 0

screen = pg.display.set_mode(size)

while(True):
    # GRAPHICS
    screen.fill(black)

    time_text = myfont.render(
        'time: ' + str(round(state['timer']/1000)), False, (255, 255, 255))

    generation_text = myfont.render(
        'current generation: ' + str(current_generation), False, (255, 255, 255))

    screen.blit(time_text, (420, 470))

    screen.blit(generation_text, (350, 450))

    pg.draw.line(screen, (255, 255, 255), (0, 490), (500, 490))

    for i, specimen in enumerate(specimina):
        pg.draw.polygon(screen, pg.Color(specimen.color), [(round(triangle[0]), round(
            triangle[1])) for triangle in get_triangle_cords(width*i/len(specimina), 500 - specimen.altitude)], 1)

    pg.display.flip()

    # MOVEMENT
    state['timer'] += 1
    for specimen in specimina:
        if state['timer'] < sequence_size:
            boost_bool = specimen.sequence[state['timer']] >= 0.5
        else:
            boost_bool = False
        if boost_bool and specimen.fuel > 0:
            specimen.boost()
        else:
            specimen.gravity()
        if get_triangle_cords(100, 500 - specimen.altitude)[1][1] > 490:
            specimen.test_result = specimen.speed
            previous_specimina.append(specimen)
            specimina.remove(specimen)

    if len(specimina) == 0:
        current_generation += 1
        print('GENERATING NEW GENERATION')
        generate_next_specimina()
        print('NEW GENERATION CREATED')
        previous_specimina = []
        state['timer'] = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
