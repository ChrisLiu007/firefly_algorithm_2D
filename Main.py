from Swarm import Swarm
import config
import utils

def main():
    swarm = Swarm(config.ALPHA, config.ABSORPTION)
    update_brightness(swarm.fireflies)
    swarm.update_attractiveness()

    utils.description(swarm.fireflies)
    print()

    for i, f in enumerate(swarm.most_attractive):
        print(i, "-", swarm.fireflies.index(f), end="|")

    print()

    # print("Firefly number:", utils.index_of_alpha(swarm.fireflies), "is the brightest")
    swarm.__str__()

    t = 0

    while t < config.MAX_GENERATION:
        for i, firefly in enumerate(swarm.fireflies):
            other_firefly = swarm.most_attractive[i]

            if other_firefly is not firefly and other_firefly.attractiveness > firefly.attractiveness:
                swarm.move(firefly, other_firefly)
            else:
                swarm.move_randomly(other_firefly)
            update_brightness(swarm.fireflies)
            swarm.update_attractiveness()
            # print()
            # swarm.__str__()
        t += 1
        # print(t)

    print()
    swarm.__str__()
    utils.description(swarm.fireflies)

def update_brightness(fireflies):
    for firefly in fireflies:
        firefly.brightness = -utils.Ackley_global_minimum(firefly) / 10
        firefly.attractiveness = firefly.brightness
        # print(firefly.brightness)

if __name__ == "__main__":
    main()
