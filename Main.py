import time

from Gen_Secondary import generate_starting_list, SecondaryElements
from Draw_Info import DrawInfo
from Intro_sort import intro_sort
from Quick_sort import quick_sort
from Merge_sort import merge_sort
import pygame
import sys

pygame.init()
n = 150
min_v = -100
max_v = 100
lst = generate_starting_list(n, min_v, max_v)
draw_info = DrawInfo(lst)
running = True
sorting = False
is_sorted = False
ascending = True
sorting_algorithm = quick_sort
sorting_alg_name = "Quick Sort"
clock = pygame.time.Clock()
box1 = SecondaryElements("Size:", DrawInfo.SIDE_PAD / 2, 170, draw_info.screen)
box2 = SecondaryElements("Max value:", DrawInfo.WIDTH / 2 - 100, 170, draw_info.screen)
box3 = SecondaryElements("Min value:", DrawInfo.WIDTH - 3 * DrawInfo.SIDE_PAD, 170, draw_info.screen)

while running:
    clock.tick(DrawInfo.FPS)
    if sorting:
        try:
            next(sorting_algorithm_generator)
        except StopIteration:
            is_sorted = True
            sorting = False
    else:
        draw_info.draw(sorting_alg_name, ascending)  # обнуляє фон та малює заголовки
        SecondaryElements.show(box1, box2, box3)  # малює прямокутники та текст до них
        SecondaryElements.draw_error(box1, box2, box3)  # залежить від .show
        draw_info.draw_list()  # малює стовпці, другий аргумент оновлює екран
    if is_sorted:
        SecondaryElements.output_success(draw_info.screen)  # напис про успішне сортування
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if box1.input_rect.collidepoint(event.pos):
                SecondaryElements.set_colors([True, False, False], box1, box2, box3)  # встановлює колір на рамку, True- активний
            elif box2.input_rect.collidepoint(event.pos):
                SecondaryElements.set_colors([False, True, False], box1, box2, box3)
            elif box3.input_rect.collidepoint(event.pos):
                SecondaryElements.set_colors([False, False, True], box1, box2, box3)
            else:
                SecondaryElements.set_colors([False, False, False], box1, box2, box3)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                is_sorted = False
                sorting = False
                if box1.is_data_correct():
                    n = int(box1.user_text)
                if box2.is_data_correct():
                    max_v = int(box2.user_text)
                if box3.is_data_correct():
                    min_v = int(box3.user_text)
                draw_info.lst = generate_starting_list(n, min_v, max_v)  # аргументи або залишаться за замовч або ні
                draw_info.set_lst(draw_info.lst)
            elif all([event.key == pygame.K_SPACE, not sorting]):
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif all([event.key == pygame.K_a, not ascending, not sorting]):
                ascending = True
            elif all([event.key == pygame.K_d, ascending, not sorting]):
                ascending = False
            elif all([event.key == pygame.K_q, not sorting]):
                sorting_algorithm = quick_sort  # назва функції для генератора
                sorting_alg_name = "Quick sort"  # назва алгоритму для вивода на екран
            elif all([event.key == pygame.K_m, not sorting]):
                sorting_algorithm = merge_sort
                sorting_alg_name = "Merge sort"
            elif all([event.key == pygame.K_i, not sorting]):
                sorting_algorithm = intro_sort
                sorting_alg_name = "Intro sort"
            elif event.key in SecondaryElements.ALLOWED_BUTTONS and any(
                    SecondaryElements.is_active(box1, box2, box3)):  # чи є активна комірка
                self = [x for x in SecondaryElements.is_active(box1, box2, box3) if x is not False]  # пошук активної комірки
                self[0].user_text += event.unicode if len(
                    self[0].user_text) < 5 else ""  # додавання символу якщо він не п'ятий і >
            elif event.key == pygame.K_BACKSPACE and any(SecondaryElements.is_active(box1, box2, box3)):
                self = [x for x in SecondaryElements.is_active(box1, box2, box3) if
                        x is not False]  # аналогічне видалення символу
                self[0].user_text = self[0].user_text[:-1]
