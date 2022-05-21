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
    MIN_ADMISSIBLE_AMOUNT_OF_ELEMENTS = 50  # допустимі межі розміру
    MAX_ADMISSIBLE_AMOUNT_OF_ELEMENTS = 50000  # масиву згідно з варіантом

    def __init__(self, text, x, y, screen):
        """Оголошення розмірів, координат та кольору другорядного тексту і форм введення"""
        self.__width = 60
        self.__height = 45
        self.__user_text = ""
        self.__text = text
        self.__text_rect = DrawInfo.SMALL_FONT.render(self.__text, 1, DrawInfo.BLACK_COLOR)
        self.__color_passive = DrawInfo.FORM_COLOR_PASSIVE
        self.__color_active = DrawInfo.FORM_COLOR_ACTIVE
        self.__text_color = DrawInfo.ADDITIONAL_TEXT_COLOR
        self.__screen = screen
        self.__x = x
        self.__y = y
        self.__color = self.__color_passive

    def get_user_text(self):
        return self.__user_text

    def set_user_text(self, text):
        self.__user_text = text

    def add_user_text(self, text):
        self.__user_text += text

    def output_forms(self):
        """Виведення тексту і форм"""
        users_text_rect = DrawInfo.SMALL_FONT.render(self.__user_text, 1, DrawInfo.BLACK_COLOR)
        self.__input_rect = pygame.Rect(self.__x + self.__text_rect.get_width(), self.__y + 5,
                                        max(self.__width, users_text_rect.get_width()), self.__height)
        pygame.draw.rect(self.__screen, self.__color, self.__input_rect, 2)
        self.__screen.blit(self.__text_rect, (self.__x, self.__y))
        self.__screen.blit(users_text_rect, (self.__input_rect.x, self.__y + 2))

    def get_rect_size(self):
        return self.__input_rect

    def is_data_correct(self):
        """Перевірка коректності введених даних"""
        if self.__text == "Size:":
            if not (self.__user_text.isdigit() and int(self.__user_text) in range(
                    self.MIN_ADMISSIBLE_AMOUNT_OF_ELEMENTS,
                    self.MAX_ADMISSIBLE_AMOUNT_OF_ELEMENTS)):
                return False
            return True
        if self.__text == "Max value:" or self.__text == "Min value:":
            is_digit = lambda x: x.isdigit() if x[:1] != '-' else x[1:].isdigit()
            if not is_digit(self.__user_text):
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
                self.__screen.blit(error_text_rect, (self.__input_rect.x - 20, self.__y + self.__height + 5))

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
            box.__color = box.__color_active if values[i] is True else box.__color_passive
            i += 1

    @staticmethod
    def is_active(*boxes):
        """Статичний метод, що повертає список активності
        форм (завжди активне лише одна)"""
        return [box if box.__color == box.__color_active else False for box in boxes]
