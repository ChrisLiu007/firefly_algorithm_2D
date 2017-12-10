from Swarm import Swarm
import config
import utils


def main():
    swarm = Swarm(config.POPULATION, config.MAX_GENERATION)
    swarm.fireflies_generator(config.POPULATION)

    for firefly in swarm.fireflies:
        firefly.brightness = utils.example_function(firefly)
        # firefly.attractiveness = firefly.brightness

    utils.description(swarm.fireflies)
    print("Firefly number:", utils.index_of_alpha(swarm.fireflies), "is the most attractive")
    swarm.__str__()

    t = 0

    while t < config.MAX_GENERATION:
        for firefly in swarm.fireflies:
            for other_firefly in swarm.fireflies:
                if other_firefly is not firefly and other_firefly.brightness > firefly.brightness:
                    swarm.move(firefly, other_firefly)
                else:
                    swarm.move_randomly(other_firefly)
                swarm.update_attractiveness(firefly, other_firefly)
                swarm.update_brightness(firefly, other_firefly)
        t += 1
        # print(t)

    print()
    swarm.__str__()
    utils.description(swarm.fireflies)

if __name__ == "__main__":
    main()
