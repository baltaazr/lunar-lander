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


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        return math.hypot(self.x, self.y)

    def getPos(self):
        return [self.x, self.y]

    def norm(self):
        ans = [self.x/self.getMng(), self.y/self.getMng()]
        ansV = Vector(ans[0], ans[1])
        return ansV

    def addV(self, v):
        self.x += v.getPos()[0]
        self.y += v.getPos()[1]

    def subV(self, v):
        self.x -= v.getPos()[0]
        self.y -= v.getPos()[1]

    def getAngle(self):
        if(self.x == 0):
            if(self.y > 0):
                return math.pi/2
            else:
                return math.pi*3/2
        ans = math.atan(self.y/self.x)
        if (self.x < 0):
            return ans+math.pi
        return ans

    def scalarMult(self, s):
        self.x *= s
        self.y *= s


# Physics
FUEL_CONSTANT = 1
GRAVITY_CONSTANT = -1
RESISTANCE_CONSTANT = -0.01
DIRECTION = new Vector(0, 1)


def update(state, fuel):
    position = new Vector(init_x, init_y)
    time = 0
    state[3] += state[5]
    state[5] += fuel*FUEL_CONSTANT+GRAVITY_CONSTANT
