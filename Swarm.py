import random
from Firefly import Firefly
from math import sqrt, exp, cos, pi, e
import config
import utils

class Swarm:
    def __init__(self, alpha, absorption):
        self.alpha = alpha
        self.absorption = absorption
        self.fireflies = []
        self.most_attractive = []
        self.minX = config.MIN_X
        self.maxX = config.MAX_X
        self.minY = config.MIN_Y
        self.maxY = config.MAX_Y
        self.width = self.maxX - self.minX
        self.height = self.maxY - self.minY
        self.fireflies_generator(config.POPULATION)

    def move(self, firefly, other_firefly):
        # print("firefly.x:", firefly.x, "firefly.y:", firefly.y)
        # print("other_firefly.x:", other_firefly.x, "other_firefly.y:", other_firefly.y)
        # delta_x = self.get_attractiveness(firefly, other_firefly) * (other_firefly.x - firefly.x) + self.alpha * random.gauss(0, 0.5)
        # print("deltaX", delta_x)
        # delta_y = self.get_attractiveness(firefly, other_firefly) * (other_firefly.y - firefly.y) + self.alpha * random.gauss(0, 0.5)
        # print("deltaY", delta_y)
        # print("firefly:", self.fireflies.index(firefly))
        # print("other_firefly:", self.fireflies.index(other_firefly))
        delta_x = (other_firefly.x - firefly.x) / 10
        delta_y = (other_firefly.y - firefly.y) / 10
        firefly.x += delta_x
        firefly.y += delta_y

        # print("firefly.x:", firefly.x, "firefly.y:", firefly.y)
        self._position_handler_(firefly)

    def move_randomly(self, firefly):
        new_x_direction = random.randrange(self.minX, self.maxX)
        new_y_direction = random.randrange(self.minY, self.maxY)
        delta_x = new_x_direction - firefly.x
        delta_y = new_y_direction - firefly.y
        firefly.x += delta_x / 10
        firefly.y += delta_y / 10

    def _position_handler_(self, firefly):
        if firefly.x < self.minX or firefly.x > self.maxX:
            firefly.x = random.randrange(self.minX, self.maxX)
            print("triggered firefly:", self.fireflies.index(firefly))
        if firefly.y < self.minY or firefly.y > self.maxY:
            firefly.y = random.randrange(self.minY, self.maxY)
            print("triggered firefly:", self.fireflies.index(firefly))

    # def update_brightness(self, firefly, other_firefly):
    #     new_brightness = self._get_new_brightness_(firefly, other_firefly)
    #     # print("new_brightness:", new_brightness)
    #     # print("distance:", utils.distance(firefly, other_firefly))
    #     firefly.brightness *= new_brightness
    #     other_firefly.brightness *= new_brightness
    #
    # def _get_new_brightness_(self, firefly, other_firefly):
    #     return exp(-self.absorption * utils.distance(firefly, other_firefly))
    #
    # def _get_new_attractiveness_(self, firefly, other_firefly, B=1):
    #     return B * exp(-self.absorption * utils.distance(firefly, other_firefly) ** 2)
    #
    # def update_attractiveness(self, firefly, other_firefly):
    #     new_attractiveness = self._get_new_attractiveness_(firefly, other_firefly)
    #     # print("distance:", utils.distance(firefly, other_firefly))
    #     firefly.attractiveness *= new_attractiveness
    #     other_firefly.attractiveness *= new_attractiveness
    #     # print("new_attractiveness", new_attractiveness)

    def get_attractiveness(self, firefly, other_firefly):
        # attractiveness = other_firefly.brightness * exp(-self.absorption * utils.distance(firefly, other_firefly))
        attractiveness = other_firefly.brightness / self.absorption * utils.distance(firefly, other_firefly)
        # attractiveness = other_firefly.brightness / (utils.distance(firefly, other_firefly) + 1e-10)
        # print(attractiveness)
        return attractiveness

    def update_attractiveness(self):
        for firefly in self.fireflies:
            attractiveness = []
            for other_firefly in self.fireflies:
                if firefly is other_firefly:
                    attractiveness.append(firefly.brightness)
                else:
                    attractiveness.append(self.get_attractiveness(firefly, other_firefly))
            index = attractiveness.index(max(attractiveness))
            self.most_attractive.append(self.fireflies[index])

    def fireflies_generator(self, population):
        for i in range(population):
            x = random.randrange(self.minX, self.maxX, 1)
            y = random.randrange(self.minY, self.maxY, 1)
            brightness = 0
            self.fireflies.append(Firefly(x, y, brightness))

    def __str__(self):
        tmp_area = [['..' for _ in range(self.width)] for _ in range(self.height)]
        # print(tmp_area)

        for i, firefly in enumerate(self.fireflies):
            if self.minX < 0:
                x = firefly.x + self.width / 2
            else:
                x = firefly.x
            if self.minY < 0:
                y = firefly.y + self.height / 2
            else:
                y= firefly.y
            # print("x:", x, "y:", y)
            if x > self.width or x < 0 or y < 0 or y > self.height:
                print("Firefly", i, "is out", firefly.x, firefly.y)
            tmp_area[int(y)][int(x)] = str(i)
        for ar in tmp_area:
            print(ar)