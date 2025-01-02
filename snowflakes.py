import os
import time
import random

SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FLAKES = 200, 60, 500
SHAPES = ['❅', '❆', '⋆', '✱', '❋', '✻', '✼', '•', '°']


class Flake:
    def __init__(self, pos_x, pos_y, shape):
        self.pos_x, self.pos_y, self.shape = pos_x, pos_y, shape

    def move(self):
        self.pos_y += 1
        self.pos_x = max(0, min(self.pos_x + random.choice([-1, 0, 1]), SCREEN_WIDTH - 1))
        self.shape = random.choice(SHAPES)


clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def draw(flakes, snow_layer):
    screen = [[' '] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

    for x in range(SCREEN_WIDTH):
        for y in range(snow_layer[x]):
            if SCREEN_HEIGHT - 1 - y >= 0:
                screen[SCREEN_HEIGHT - 1 - y][x] = SHAPES[1]

    for f in flakes:
        if 0 <= f.pos_y < SCREEN_HEIGHT:
            screen[f.pos_y][f.pos_x] = f.shape

    print('\n'.join([''.join(row) for row in screen]))


def choose_x(snow_layer, max_layer):
    eligible = [x for x in range(SCREEN_WIDTH) if snow_layer[x] < max_layer[x]]
    return random.choice(eligible) if eligible else random.randint(0, SCREEN_WIDTH - 1)


def main():
    flakes = []
    snow_layer = [0] * SCREEN_WIDTH
    max_layer = [random.randint(1, 3) for _ in range(SCREEN_WIDTH)]  # Ustalanie maksymalnych zasp na 1-3 wiersze

    while True:
        clear_screen()
        if len(flakes) < MAX_FLAKES:
            for _ in range(random.randint(1, 3)):
                if random.random() < 0.7:
                    x = choose_x(snow_layer, max_layer)
                    flakes.append(Flake(x, 0, random.choice(SHAPES)))

        remaining = []
        for flake in flakes:
            flake.move()
            if flake.pos_y >= SCREEN_HEIGHT - snow_layer[flake.pos_x] - 1:
                if snow_layer[flake.pos_x] < max_layer[flake.pos_x]:
                    snow_layer[flake.pos_x] += 1
            else:
                remaining.append(flake)

        flakes = remaining
        draw(flakes, snow_layer)
        time.sleep(0.13)


if __name__ == "__main__":
    os.system('chcp 65001 >nul') if os.name == "nt" else None
    main()
