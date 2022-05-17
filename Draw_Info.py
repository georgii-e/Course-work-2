import pygame
from math import floor

pygame.init()


class DrawInfo:
    """Клас з більшістю констант для малювання та функціями
    виведення на екран головних написів і стовпців масиву"""
    BLACK_COLOR = 0, 0, 0
    WHITE_COLOR = 255, 255, 255
    RED_COLOR = 255, 0, 0
    GREEN_COLOR = 0, 255, 0
    TITLE_TEXT_COLOR = 166, 116, 88
    SUBTITLE_TEXT_COLOR = 2, 81, 89
    ADDITIONAL_TEXT_COLOR = 63, 133, 140
    LIGHT_BLUE = 196, 238, 242
    BACKGROUND_COLOR = LIGHT_BLUE
    GRAYSCALE = [
        (50, 50, 50),
        (120, 120, 120),
        (190, 190, 190)
    ]
    FORM_COLOR_PASSIVE = WHITE_COLOR
    FORM_COLOR_ACTIVE = BLACK_COLOR
    HEIGHT = 900
    WIDTH = 1600
    SIDE_PAD = 100
    TOP_PAD = 240
    MAX_AMOUNT_TO_VIZ = 1000  # максимальна кількість елементів, сортування яких буде візуалізуватися
    FPS = 120  # регулювання швидкості сортування
    SMALL_FONT = pygame.font.SysFont('comicsans', 36)
    VERY_SMALL_FONT = pygame.font.SysFont('comicsans', 15)
    FONT = pygame.font.SysFont('comicsans', 40)
    LARGE_FONT = pygame.font.SysFont('comicsans', 75)

    def __init__(self, lst):
        """Встановлення головного екрану та стовпців"""
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Course work Yehor Vasyliev")
        pygame.display.set_icon(pygame.image.load("media/icon.png"))
        self.set_lst(lst)

    def set_lst(self, lst):
        """Розрахунок одиничних розмірів комірок"""
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)
        self.block_width = (self.WIDTH - self.SIDE_PAD) / len(self.lst)
        self.block_height = (self.HEIGHT - self.TOP_PAD) / (self.max_value - self.min_value)
        self.start_x = self.SIDE_PAD // 2

    def draw(self, alg_name, ascending):
        """Виведення головного тексту"""
        self.screen.fill(self.BACKGROUND_COLOR)
        title = self.LARGE_FONT.render(f"{alg_name} - {'Ascending' if ascending else 'Descending'}", 1,
                                       self.TITLE_TEXT_COLOR)
        self.screen.blit(title, ((self.WIDTH - title.get_width()) / 2, -20))
        sorting = self.FONT.render(" M - merge sort | Q - quick sort | I - intro sort", 1,
                                   self.SUBTITLE_TEXT_COLOR)
        self.screen.blit(sorting, ((self.WIDTH - sorting.get_width()) / 2, 65))
        controls = self.FONT.render("A - ascending | D - descending | R - reset | SPACE - start sorting", 1,
                                    self.BLACK_COLOR)
        self.screen.blit(controls, ((self.WIDTH - controls.get_width()) / 2, 115))

    def draw_list(self, color_positions={}, clear_bg=False):
        """Виведення стовпців, за умовчанням сірого кольору, якщо функція викликається із
         функції сортування, то два стовпці що переставляються змінюють колір на червоний і зелений.
         clear_bg відповідає за необхідність оновлення екрану (при сортуванні - необхідно, в інших випадках - ні"""
        lst = self.lst
        if clear_bg:
            clear_rect = (self.SIDE_PAD // 2, self.TOP_PAD,
                          self.WIDTH - self.SIDE_PAD, self.HEIGHT - self.TOP_PAD)
            pygame.draw.rect(self.screen, self.BACKGROUND_COLOR, clear_rect)
        if len(lst) <= self.MAX_AMOUNT_TO_VIZ:
            for i, val in enumerate(lst):
                x = self.start_x + i * self.block_width
                y = self.HEIGHT - (val - self.min_value) * self.block_height
                color = self.GRAYSCALE[i % 3]
                if i in color_positions:
                    color = color_positions[i]
                pygame.draw.rect(self.screen, color, (x, y, self.block_width, self.HEIGHT - y))
        if clear_bg:
            pygame.display.update()
