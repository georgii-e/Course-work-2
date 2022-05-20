import pygame
import random
import Config
from Draw_Info import DrawInfo


class ArrayProcessing:
    """Клас для роботи з масивом"""
    SIDE_PAD = 100
    TOP_PAD = 240

    def __init__(self, screen):
        self.amount_to_vis = Config.MAX_AMOUNT_TO_VIS
        self.width = DrawInfo.WIDTH
        self.height = DrawInfo.HEIGHT
        self.screen = screen

    def generate_list(self, n, min_val, max_val):
        """Генерація масиву, міняє місцями максимальне і
        мінімальне значення в разі необхідності"""
        self.lst = []
        self.min_value = min_val
        self.max_value = max_val
        if max_val < min_val:
            max_val, min_val = min_val, max_val
        for i in range(n):
            val = random.randint(min_val, max_val)
            self.lst.append(val)
        self.set_lst()

    def set_lst(self):
        """Розрахунок одиничних розмірів комірок"""
        self.block_width = (self.width - self.SIDE_PAD) / len(self.lst)
        self.block_height = (self.height - self.TOP_PAD) / (self.max_value - self.min_value)
        self.start_x = self.SIDE_PAD // 2

    def draw_list(self, color_positions={}, clear_bg=False):
        """Виведення стовпців, за умовчанням сірого кольору, якщо функція викликається із
         функції сортування, то два стовпці що переставляються змінюють колір на червоний і зелений.
         clear_bg відповідає за необхідність оновлення екрану (при сортуванні - необхідно, в інших випадках - ні"""
        lst = self.lst
        if clear_bg:
            clear_rect = (self.SIDE_PAD // 2, self.TOP_PAD,
                          self.width - self.SIDE_PAD, self.height - self.TOP_PAD)
            pygame.draw.rect(self.screen, DrawInfo.BACKGROUND_COLOR, clear_rect)
        if len(lst) <= self.amount_to_vis:
            for i, val in enumerate(lst):
                x = self.start_x + i * self.block_width
                y = self.height - (val - self.min_value) * self.block_height
                color = DrawInfo.GRAYSCALE[i % 3]
                if i in color_positions:
                    color = color_positions[i]
                pygame.draw.rect(self.screen, color, (x, y, self.block_width, self.height - y))
            if clear_bg:
                pygame.display.update()
