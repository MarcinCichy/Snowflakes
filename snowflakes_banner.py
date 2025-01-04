import os
import time
import random
import pyfiglet

# ------------------ USTAWIENIA ------------------
SCREEN_W, SCREEN_H = 200, 60
TEXT = "H A P P Y  N E W   Y E A R"
FONT_NAME = "banner3"
FORCED_HEIGHT = 7
BOTTOM_MARGIN = 1
MAX_FLAKES = 700
SNOW_CHARS = ['❅', '❆', '⋆', '✱', '❋', '✻', '✼', '•', '°']
MIN_SNOW, MAX_SNOW = 9, 14
SLEEP_TIME = 0.01


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_ascii_mask(text, font, height, width=200):
    """Zwraca maskę (listę list True/False) z PyFiglet, przyciętą/dopełnioną do podanej wysokości."""
    fig = pyfiglet.Figlet(font=font, width=width)
    art = fig.renderText(text).rstrip('\n')
    lines = art.split('\n')
    if len(lines) < height:
        lines += [''] * (height - len(lines))
    elif len(lines) > height:
        lines = lines[:height]
    w = max(len(line) for line in lines) if lines else 0
    mask = []
    for line in lines:
        row = [(ch != ' ') for ch in line.ljust(w)]
        mask.append(row)
    return mask


class Flake:
    def __init__(self, x, y, shape):
        self.x, self.y, self.shape = x, y, shape

    def fall(self):
        self.y += 1
        self.x = max(0, min(self.x + random.choice([-1, 0, 1]), SCREEN_W - 1))
        if random.random() < 0.2:
            self.shape = random.choice(SNOW_CHARS)


def main():
    mask = generate_ascii_mask(TEXT, FONT_NAME, FORCED_HEIGHT, width=200)
    mask_h, mask_w = len(mask), len(mask[0]) if mask else 0
    start_y = SCREEN_H - BOTTOM_MARGIN - mask_h
    start_x = (SCREEN_W - mask_w) // 2

    snow_layer = [0] * SCREEN_W
    max_layer = [random.randint(MIN_SNOW, MAX_SNOW) for _ in range(SCREEN_W)]
    flakes = []

    clear_screen()
    while True:
        # Dodaj nowe płatki
        if len(flakes) < MAX_FLAKES:
            for _ in range(random.randint(1, 4)):
                x = random.randint(0, SCREEN_W - 1)
                if snow_layer[x] < SCREEN_H - 1:
                    flakes.append(Flake(x, 0, random.choice(SNOW_CHARS)))

        # Ruch płatków i osadzanie w śniegu / literach
        new_flakes = []
        for f in flakes:
            f.fall()
            if f.y >= SCREEN_H:
                continue
            snow_start = SCREEN_H - snow_layer[f.x]
            # Sprawdź literę
            if (start_y <= f.y < start_y + mask_h) and (start_x <= f.x < start_x + mask_w):
                if mask[f.y - start_y][f.x - start_x]:
                    if snow_layer[f.x] < max_layer[f.x]:
                        snow_layer[f.x] += 1
                    continue
            # Sprawdź zaspę
            if f.y >= snow_start - 1:
                if snow_layer[f.x] < max_layer[f.x]:
                    snow_layer[f.x] += 1
            else:
                new_flakes.append(f)
        flakes = new_flakes

        # Rysowanie
        clear_screen()
        screen = [[' '] * SCREEN_W for _ in range(SCREEN_H)]
        # Zaspy
        for x in range(SCREEN_W):
            h = snow_layer[x]
            for i in range(h):
                screen[SCREEN_H - 1 - i][x] = '❆'
        # Płatki w locie
        for f in flakes:
            if 0 <= f.y < SCREEN_H:
                screen[f.y][f.x] = f.shape
        # Wycinanie liter
        for r in range(mask_h):
            for c in range(mask_w):
                if mask[r][c]:
                    sy, sx = start_y + r, start_x + c
                    if 0 <= sx < SCREEN_W and 0 <= sy < SCREEN_H:
                        screen[sy][sx] = ' '
        print('\n'.join(''.join(row) for row in screen))
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    if os.name == "nt":
        os.system("chcp 65001>nul")
    main()
