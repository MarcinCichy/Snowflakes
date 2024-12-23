import os
import time
import random


"""
    UWAGA - ten kod uruchamiać jedynie w Linuxie, ponieważ w Windowsie nie działa poprawnie wyświetlanie znaków Unicode.
    NOTE - run this code only in Linux, because in Windows the display of Unicode characters does not work correctly

"""

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 60

# SHAPES = ['❅', '❆', '⋆', '✱', '❋', '✻', '✼', '•', '°']
SHAPES = ['\u2745', '\u2746', '\u22C6', '\u2731', '\u274B', '\u273B', '\u273C', '\u2022', '\u00B0']


class Flake:
    def __init__(self, x_pos, y_pos, shape, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape = shape
        self.speed = speed

    def snowflake_move_down(self):
        self.y_pos += self.speed
        self.x_pos += random.choice([-1, 0, 1])
        self.x_pos = max(0, min(self.x_pos, SCREEN_WIDTH - 1))
        self.shape = random.choice(SHAPES)


def clear_screen():
    """Czyści ekran w zależności od systemu operacyjnego."""
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_screen(flakes):
    screen = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

    for flake in flakes:
        if 0 <= flake.y_pos < SCREEN_HEIGHT and 0 <= flake.x_pos < SCREEN_WIDTH:
            screen[flake.y_pos][flake.x_pos] = flake.shape

    for row in screen:
        print(''.join(row))


def main():
    flakes = []
    while True:
        clear_screen()

        for _ in range(random.randint(1, 8)):
            if random.random() < 0.8:
                x = random.randint(0, SCREEN_WIDTH - 1)
                symbol = random.choice(SHAPES)
                speed = random.randint(1, 2)
                flakes.append(Flake(x, 0, symbol, speed))

        for flake in flakes:
            flake.snowflake_move_down()

        flakes = [flake for flake in flakes if flake.y_pos < SCREEN_HEIGHT]

        draw_screen(flakes)

        time.sleep(0.15)


if __name__ == "__main__":
    if os.name == "nt":
        os.system('chcp 65001 >nul')
    main()
