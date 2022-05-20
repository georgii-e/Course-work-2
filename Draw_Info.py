import pygame

pygame.init()


class DrawInfo:
    """Клас з константами для малювання та функціями
    виведення на екран головних написів"""
    BLACK_COLOR = 0, 0, 0
    WHITE_COLOR = 255, 255, 255
    RED_COLOR = 255, 0, 0
    GREEN_COLOR = 0, 255, 0
    BLUE_COLOR = 0, 0, 255
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
    SMALL_FONT = pygame.font.SysFont('comicsans', 36)
    VERY_SMALL_FONT = pygame.font.SysFont('comicsans', 15)
    FONT = pygame.font.SysFont('comicsans', 40)
    LARGE_FONT = pygame.font.SysFont('comicsans', 75)

    def __init__(self):
        """Встановлення головного екрану та стовпців"""
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Course work Yehor Vasyliev")
        pygame.display.set_icon(pygame.image.load("media/icon.png"))

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
