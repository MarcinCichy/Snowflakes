import os
import time
import random

SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FLAKES = 200, 60, 500
SHAPES = ['❅', '❆', '⋆', '✱', '❋', '✻', '✼', '•', '°']

class Flake:
    def __init__(self, x, y, shape):
        self.x, self.y, self.shape = x, y, shape
    def move(self):
        self.y += 1
        self.x = max(0, min(self.x + random.choice([-1, 0, 1]), SCREEN_WIDTH - 1))
        self.shape = random.choice(SHAPES)


clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def draw(flakes, snow_layer):
    screen = [[' '] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

    # Rysowanie zalegającego śniegu
    for x in range(SCREEN_WIDTH):
        for y in range(snow_layer[x]):
            if SCREEN_HEIGHT - 1 - y >= 0:
                screen[SCREEN_HEIGHT - 1 - y][x] = SHAPES[1]

    # Rysowanie płatków śniegu w ruchu
    for f in flakes:
        if 0 <= f.y < SCREEN_HEIGHT:
            screen[f.y][f.x] = f.shape

    # Wyświetlenie ekranu
    print('\n'.join([''.join(row) for row in screen]))


def choose_x(snow_layer, target_layer):
    eligible = [x for x in range(SCREEN_WIDTH) if snow_layer[x] < target_layer[x]]
    return random.choices(eligible, [target_layer[x] - snow_layer[x] for x in eligible], k=1)[0] if eligible else None


def main():
    flakes, snow_layer, target_layer = [], [0]*SCREEN_WIDTH, [random.randint(1, 3) for _ in range(SCREEN_WIDTH)]
    while True:
        clear_screen()
        if len(flakes) < MAX_FLAKES:
            for _ in range(random.randint(1, 3)):
                if random.random() < 0.7:
                    x = choose_x(snow_layer, target_layer) or random.randint(0, SCREEN_WIDTH - 1)
                    flakes.append(Flake(x, 0, random.choice(SHAPES)))
        remaining = []
        for flake in flakes:
            flake.move()
            if flake.y >= SCREEN_HEIGHT - snow_layer[flake.x] - 1:
                snow_layer[flake.x] = min(snow_layer[flake.x] + random.randint(1, 2), target_layer[flake.x])
            else:
                remaining.append(flake)
        flakes = remaining
        draw(flakes, snow_layer)
        time.sleep(0.13)


if __name__ == "__main__":
    os.system('chcp 65001 >nul') if os.name == "nt" else None
    main()