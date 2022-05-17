import random
import pygame
from Draw_Info import DrawInfo

pygame.init()


class SecondaryElements:
    """Клас для обробки другорядних елементів"""
    ALLOWED_BUTTONS = [pygame.K_0, pygame.K_1, pygame.K_2,
                       pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                       pygame.K_8, pygame.K_9, pygame.K_MINUS]  # цифри (від 1 до 9 та -) що будуть зчитуватися
    ERROR_TEXT = "Incorrect value"
    SUCCESS_TEXT = "SUCCESS"

    def __init__(self, text, x, y, screen):
        """Оголошення розмірів, координат та кольору другорядного тексту і форм введення"""
        self.width = 60
        self.height = 45
        self.user_text = ""
        self.text = text
        self.text_rect = DrawInfo.SMALL_FONT.render(self.text, 1, DrawInfo.BLACK_COLOR)
        self.color_passive = DrawInfo.FORM_COLOR_PASSIVE
        self.color_active = DrawInfo.FORM_COLOR_ACTIVE
        self.text_color = DrawInfo.ADDITIONAL_TEXT_COLOR
        self.screen = screen
        self.x = x
        self.y = y
        self.color = self.color_passive

    def output_forms(self):
        """Виведення тексту і форм"""
        users_text_rect = DrawInfo.SMALL_FONT.render(self.user_text, 1, DrawInfo.BLACK_COLOR)
        self.input_rect = pygame.Rect(self.x + self.text_rect.get_width(), self.y + 5,
                                      max(self.width, users_text_rect.get_width()), self.height)
        pygame.draw.rect(self.screen, self.color, self.input_rect, 2)
        self.screen.blit(self.text_rect, (self.x, self.y))
        self.screen.blit(users_text_rect, (self.input_rect.x, self.y + 2))

    def is_data_correct(self):
        """Перевірка коректності введених даних"""
        if self.text == "Size:":
            if not (self.user_text.isdigit() and int(self.user_text) in range(100, 50000)):
                return False
            return True
        if self.text == "Max value:" or self.text == "Min value:":
            is_digit = lambda x: x.isdigit() if x[:1] != '-' else x[1:].isdigit()
            if not is_digit(self.user_text):
                return False
            return True
        else:
            return False

    @staticmethod
    def output_success(screen):
        """Виведення повідомлення про успішне сортування без візуалізації"""
        success_text_rect = DrawInfo.LARGE_FONT.render(SecondaryElements.SUCCESS_TEXT, 1, DrawInfo.SUBTITLE_TEXT_COLOR)
        screen.blit(success_text_rect, ((DrawInfo.WIDTH - success_text_rect.get_width()) / 2,
                                        (DrawInfo.HEIGHT - success_text_rect.get_height()) / 2))

    @staticmethod
    def draw_error(*boxes):
        """Статичний метод, що оброблює три форми одразу
        і виводить повідомлення у разі їх некоректності"""
        for self in boxes:
            if not self.is_data_correct():
                error_text_rect = DrawInfo.VERY_SMALL_FONT.render(self.ERROR_TEXT, 1, DrawInfo.RED_COLOR)
                self.screen.blit(error_text_rect, (self.input_rect.x - 20, self.y + self.height + 5))

    @staticmethod
    def show(*boxes):
        """Статичний метод, що виводить одразу три форми"""
        for box in boxes:
            box.output_forms()

    @staticmethod
    def set_colors(values, *boxes):
        """Статичний метод, що приймає список значень які відповідають
        за (не) активність форм та відповідно змінює їх кольори"""
        i = 0
        for box in boxes:
            box.color = box.color_active if values[i] is True else box.color_passive
            i += 1

    @staticmethod
    def is_active(*boxes):
        """Статичний метод, що повертає список активності
        форм (завжди активне лише одна)"""
        return [box if box.color == box.color_active else False for box in boxes]


def generate_starting_list(n, min_val, max_val):
    """Генерація масиву, міняє місцями максимальне і
    мінімальне значення в разі необхідності"""
    lst = []
    if max_val < min_val:
        max_val, min_val = min_val, max_val
    for i in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst
