import random
from Firefly import Firefly
from math import sqrt, exp, cos, pi, e
import config
import utils

class Swarm:
    def __init__(self, alpha=0.2, absorption=1):
        self.alpha = alpha
        self.absorption = absorption
        self.fireflies = []
        self.width = config.WIDTH
        self.height = config.HEIGHT

    def move(self, firefly, other_firefly):
        delta_x = self._get_new_attractiveness_(firefly, other_firefly) * (other_firefly.x - firefly.x) + self.alpha * random.gauss(0, 0.5)
        # print("deltaX", deltaX)
        delta_y = self._get_new_attractiveness_(firefly, other_firefly) * (other_firefly.y - firefly.y) + self.alpha * random.gauss(0, 0.5)
        # print("deltaY", deltaY)
        # print("firefly:", self.fireflies.index(firefly))
        # print("other_firefly:", self.fireflies.index(other_firefly))
        firefly.x += delta_x
        firefly.y += delta_y
        self._position_handler_(firefly)

    def move_randomly(self, firefly):
        new_x_direction = random.randrange(0, self.width)
        new_y_direction = random.randrange(0, self.height)
        delta_x = new_x_direction - firefly.x
        delta_y = new_y_direction - firefly.y
        firefly.x += delta_x / 10
        firefly.y += delta_y / 10

    def _position_handler_(self, firefly):
        if firefly.x < 0 or firefly.x > self.width:
            firefly.x = random.randrange(0, self.width)
        if firefly.y < 0 or firefly.y > self.height:
            firefly.y = random.randrange(0, self.height)

    def update_brightness(self, firefly, other_firefly):
        new_brightness = self._get_new_brightness_(firefly, other_firefly)
        # print("new_brightness:", new_brightness)
        # print("distance:", utils.distance(firefly, other_firefly))
        firefly.brightness *= new_brightness
        other_firefly.brightness *= new_brightness

    def _get_new_brightness_(self, firefly, other_firefly):
        return exp(-self.absorption * utils.distance(firefly, other_firefly))

    def _get_new_attractiveness_(self, firefly, other_firefly, B=1):
        return B * exp(-self.absorption * utils.distance(firefly, other_firefly) ** 2)

    def update_attractiveness(self, firefly, other_firefly):
        new_attractiveness = self._get_new_attractiveness_(firefly, other_firefly)
        # print("distance:", utils.distance(firefly, other_firefly))
        firefly.attractiveness *= new_attractiveness
        other_firefly.attractiveness *= new_attractiveness
        # print("new_attractiveness", new_attractiveness)

    def fireflies_generator(self, population):
        for i in range(population):
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            brightness = 0
            self.fireflies.append(Firefly(x, y, brightness))

    def __str__(self):
        tmp_area = [['..' for _ in range(self.width)] for _ in range(self.height)]

        for i, firefly in enumerate(self.fireflies):
            if firefly.x >= self.height or firefly.y >= self.width:
                print("Firefly", i, "is out", firefly.x, firefly.y)
            tmp_area[min(int(firefly.x), self.height - 1)][min(int(firefly.y), self.width - 1)] = str(i)
        for ar in tmp_area:
            print(ar)



