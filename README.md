# firefly_algorithm_2D
### Firefly Algorithm in 2D on Python "Ad Fontes" project CS@UCU2017

```python
config.py

POPULATION = 35
MAX_GENERATION = 50
ALPHA = 0.2
ABSORPTION = 1
MIN_X = 0
MAX_X = 20
MIN_Y = 0
MAX_Y = 20
```
```python
Firefly.py

class Firefly:
    def __init__(self, x, y, brightness):
        self.x = x
        self.y = y
        self.brightness = brightness
        self.attractiveness = self.brightness
```
```python
Swarm.py

import random
from Firefly import Firefly
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
        fraction = 2
        delta_x = (other_firefly.x - firefly.x) / fraction
        delta_y = (other_firefly.y - firefly.y) / fraction
        firefly.x += delta_x
        firefly.y += delta_y

    def move_randomly(self, firefly):
        new_x_direction = random.randrange(self.minX, self.maxX)
        new_y_direction = random.randrange(self.minY, self.maxY)
        delta_x = new_x_direction - firefly.x
        delta_y = new_y_direction - firefly.y
        firefly.x += delta_x / self.width
        firefly.y += delta_y / self.height

    def get_attractiveness(self, firefly, other_firefly):
        distance = utils.distance(firefly, other_firefly)
        if distance == 0:
            return other_firefly.brightness
        else:
            return other_firefly.brightness / (self.absorption * distance)

    def update_attractiveness(self):
        self.most_attractive = []
        for firefly in self.fireflies:
            attractiveness_best = 0
            most_attractive = firefly
            for other_firefly in self.fireflies:
                if firefly is not other_firefly and firefly.brightness < other_firefly.brightness:
                attractiveness = self.get_attractiveness(firefly, other_firefly)
                if attractiveness_best < attractiveness:
                    attractiveness_best = attractiveness
                    most_attractive = other_firefly
            self.most_attractive.append(most_attractive)

    def fireflies_generator(self, population):
        for i in range(population):
            x = random.randrange(self.minX, self.maxX, 1)
            y = random.randrange(self.minY, self.maxY, 1)
            brightness = 0
            self.fireflies.append(Firefly(x, y, brightness))

    def __str__(self):
        tmp_area = [['..' for _ in range(self.width)] for _ in range(self.height)]

        for i, firefly in enumerate(self.fireflies):
            if self.minX < 0:
                x = firefly.x + self.width / 2
            else:
                x = firefly.x
            if self.minY < 0:
                y = firefly.y + self.height / 2
            else:
                y= firefly.y
            if x > self.width or x < 0 or y < 0 or y > self.height:
                print("Firefly", i, "is out", firefly.x, firefly.y)
            tmp_area[int(y)][int(x)] = str(i)
        for ar in tmp_area:
        print(ar)
```

```python
Main.py

from Swarm import Swarm
import config
import utils

def main():
    swarm = Swarm(config.ALPHA, config.ABSORPTION)
    update_brightness(swarm.fireflies)
    swarm.update_attractiveness()
    utils.description(swarm.fireflies)

    swarm.__str__()

    t = 0

    while t < config.MAX_GENERATION:
        for i, firefly in enumerate(swarm.fireflies):

            other_firefly = swarm.most_attractive[i]

            if other_firefly is not firefly and other_firefly.attractiveness > firefly.attractiveness:
                swarm.move(firefly, other_firefly)
            elif other_firefly.attractiveness == firefly.attractiveness:
                swarm.move_randomly(other_firefly)

            update_brightness(swarm.fireflies)
            swarm.update_attractiveness()

        t += 1

    print()
    swarm.__str__()

def update_brightness(fireflies):
    for firefly in fireflies:
        firefly.brightness = -utils.Ackley_global_minimum(firefly)
        firefly.attractiveness = firefly.brightness

if __name__ == "__main__":
    main()
```

```python
utils.py

import math

def distance(firefly, other_firefly):
    return math.sqrt((other_firefly.x - firefly.x) ** 2 + (other_firefly.y - firefly.y) ** 2)

def Ackley_global_minimum(firefly):
    result = firefly.x ** 2 + firefly.y ** 2

    result /= 2
    result = math.sqrt(result)
    result /= -5
    result = -20 * math.exp(result)

    result2 = math.cos(2 * math.pi * firefly.x) + math.cos(2 * math.pi * firefly.y)
    result2 /= 2
    result2 = math.exp(result2) + 20 + math.e

    return result - result2

def Ackley_global_maximum(firefly):
    result = abs(firefly.x) + abs(firefly.y)
    result *= math.exp(-(firefly.x ** 2 + firefly.y ** 2))
    return result

def Michalewicz(firefly):
    return  -(math.sin(firefly.x) * math.sin((firefly.x**2)/math.pi)**20) + -(math.sin(firefly.y) * math.sin((2 * firefly.y**2)/math.pi)**20)

def description(fireflies):
    for i, firefly in enumerate(fireflies):
        print(i, "x:", firefly.x, "y:", firefly.y, "brightness:", firefly.brightness)

def index_of_alpha(fireflies):
    alpha = fireflies[0]
    for firefly in fireflies:
        if firefly.brightness > alpha.brightness:
            alpha = firefly
    return fireflies.index(alpha)
```
