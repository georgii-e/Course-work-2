import pygame
import random
import Config
from Draw_Info import DrawInfo


class ArrayProcessing:
    """Клас для роботи з масивом"""
    SIDE_PAD = 100
    TOP_PAD = 240

    def __init__(self, screen):
        self.__amount_to_vis = Config.MAX_AMOUNT_TO_VIS
        self.__width = DrawInfo.WIDTH
        self.__height = DrawInfo.HEIGHT
        self.__screen = screen

    def generate_list(self, n, min_val, max_val):
        """Генерація масиву, міняє місцями максимальне і
        мінімальне значення в разі необхідності"""
        self.__lst = []
        self.__min_value = min_val
        self.__max_value = max_val
        if self.__max_value < self.__min_value:
            self.__max_value, self.__min_value = self.__min_value, self.__max_value
        for i in range(n):
            val = random.randint(self.__min_value, self.__max_value)
            self.__lst.append(val)
        self.set_lst()

    def get_lst(self):
        return self.__lst

    def set_lst(self):
        """Розрахунок одиничних розмірів комірок"""
        self.__block_width = (self.__width - self.SIDE_PAD) / len(self.__lst)
        self.__block_height = (self.__height - self.TOP_PAD) / (self.__max_value - self.__min_value)
        self.__start_x = self.SIDE_PAD // 2

    def draw_list(self, color_positions={}, clear_bg=False):
        """Виведення стовпців, за умовчанням сірого кольору, якщо функція викликається із
         функції сортування, то два стовпці що переставляються змінюють колір на червоний і зелений.
         clear_bg відповідає за необхідність оновлення екрану (при сортуванні - необхідно, в інших випадках - ні"""
        lst = self.__lst
        if clear_bg:
            clear_rect = (self.SIDE_PAD // 2, self.TOP_PAD,
                          self.__width - self.SIDE_PAD, self.__height - self.TOP_PAD)
            pygame.draw.rect(self.__screen, DrawInfo.BACKGROUND_COLOR, clear_rect)
        if len(lst) <= self.__amount_to_vis:
            for i, val in enumerate(lst):
                x = self.__start_x + i * self.__block_width
                y = self.__height - (val - self.__min_value) * self.__block_height
                color = DrawInfo.GRAYSCALE[i % 3]
                if i in color_positions:
                    color = color_positions[i]
                pygame.draw.rect(self.__screen, color, (x, y, self.__block_width, self.__height - y))
            if clear_bg:
                pygame.display.update()
