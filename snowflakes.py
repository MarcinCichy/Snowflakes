import os
import time
import random

"""
    UWAGA - ten kod uruchamiać jedynie w Linuxie, ponieważ w Windowsie nie działa poprawnie wyświetlanie znaków Unicode.
    NOTE - run this code only in Linux, because in Windows the display of Unicode characters does not work correctly
"""

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 60
MAX_FLAKES = 500  # Maksymalna liczba aktywnych płatków śniegu

# Definicja kształtów płatków śniegu
SHAPES = ['\u2745', '\u2746', '\u22C6', '\u2731', '\u274B', '\u273B', '\u273C', '\u2022', '\u00B0']


class Flake:
    def __init__(self, x_pos, y_pos, shape, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.shape = shape
        self.speed = speed

    def snowflake_move_down(self):
        self.y_pos += self.speed
        self.x_pos += random.choice([-1, 0, 1])  # Lekkie przesunięcie w lewo lub prawo
        self.x_pos = max(0, min(self.x_pos, SCREEN_WIDTH - 1))  # Zapobieganie wychodzeniu poza ekran
        self.shape = random.choice(SHAPES)  # Zmiana kształtu płatka


def clear_screen():
    """Czyści ekran w zależności od systemu operacyjnego."""
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_screen(flakes, snow_layer):
    screen = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

    # Rysowanie warstwy śniegu
    draw_snow_layer(screen, snow_layer)

    # Rysowanie płatków śniegu
    for flake in flakes:
        if 0 <= flake.y_pos < SCREEN_HEIGHT and 0 <= flake.x_pos < SCREEN_WIDTH:
            screen[flake.y_pos][flake.x_pos] = flake.shape

    # Wyświetlanie ekranu
    for row in screen:
        print(''.join(row))


def draw_snow_layer(screen, snow_layer):
    """Rysuje warstwę śniegu na ekranie."""
    for x in range(SCREEN_WIDTH):
        for y in range(snow_layer[x]):
            if y < SCREEN_HEIGHT:
                screen[SCREEN_HEIGHT - 1 - y][x] = SHAPES[1]  # Użycie drugiego kształtu jako śniegu


def choose_random_x(snow_layer, target_layer):
    """Wybiera losową kolumnę z większą szansą na kolumny z niższym snow_layer."""
    eligible_x = [x for x in range(SCREEN_WIDTH) if snow_layer[x] < target_layer[x]]
    if not eligible_x:
        return None  # Wszystkie kolumny osiągnęły swój cel

    weights = [target_layer[x] - snow_layer[x] for x in eligible_x]
    selected_x = random.choices(eligible_x, weights=weights, k=1)[0]
    return selected_x


def main():
    flakes = []
    snow_layer = [0] * SCREEN_WIDTH
    target_layer = [random.randint(1, 3) for _ in range(SCREEN_WIDTH)]  # Losowy cel dla każdej kolumny

    while True:
        clear_screen()

        # Dodawanie nowych płatków, jeśli liczba aktywnych płatków jest poniżej limitu
        if len(flakes) < MAX_FLAKES:
            for _ in range(random.randint(1, 3)):  # Dodawanie 1-3 płatków na iterację
                if random.random() < 0.7:  # Prawdopodobieństwo dodania płatka 70%
                    x = choose_random_x(snow_layer, target_layer)
                    if x is None:
                        # Jeśli nie ma dostępnych kolumn, nadal dodaj płatek, ale nie kumuluj śniegu
                        x = random.randint(0, SCREEN_WIDTH - 1)
                    symbol = random.choice(SHAPES)
                    speed = 1  # Stała prędkość płatka
                    flakes.append(Flake(x, 0, symbol, speed))

        remaining_flakes = []

        for flake in flakes:
            flake.snowflake_move_down()

            x = flake.x_pos
            y = flake.y_pos

            # Obliczenie pozycji, na której płatek powinien się zatrzymać
            top_snow_y = SCREEN_HEIGHT - snow_layer[x] - 1

            if y >= top_snow_y:
                # Ustawienie płatka na poziomie top_snow_y
                flake.y_pos = top_snow_y

                if snow_layer[x] < target_layer[x]:
                    # Aktualizacja warstwy śniegu z losową wysokością, upewniając się, że nie przekracza celu
                    layer_height = random.randint(1, 2)  # Ograniczenie do 1-2, aby uniknąć szybkiego osiągania celu
                    snow_layer[x] = min(snow_layer[x] + layer_height, target_layer[x])
                # Płatka zatrzymuje się, więc nie dodajemy go do remaining_flakes
            else:
                # Płatka nadal w ruchu
                remaining_flakes.append(flake)

        flakes = remaining_flakes

        draw_screen(flakes, snow_layer)

        time.sleep(0.13)


if __name__ == "__main__":
    if os.name == "nt":
        os.system('chcp 65001 >nul')  # Ustawienie kodowania na UTF-8 w Windows
    main()
