from math import log2, floor
from Draw_Info import DrawInfo
import time


class IntroSort:
    """Інтроспективне сортування: швидке сортування,
    яке перемикається на пірамідальне при досяжності
    max_depth = floor(log2(len(lst)))"""
    SORTING_ALG_NAME = "Intro sort"

    def __init__(self, lst_control, ascending):
        self.count_of_comparisons = 0
        self.count_of_swaps = 0
        self.lst_control = lst_control
        self.lst = self.lst_control.get_lst()
        self.ascending = ascending
        self.max_depth = floor(log2(len(self.lst)))

    def sort(self, start, end, max_depth_curr=None):
        if max_depth_curr is None:
            max_depth_curr = self.max_depth
        if end - start <= 1:
            return
        elif max_depth_curr == 0:
            yield from self.heapsort(start, end)
        else:
            p = self.partition(start, end)
            yield self.lst
            yield from self.sort(start, p + 1, max_depth_curr - 1)
            yield self.lst
            yield from self.sort(p + 1, end, max_depth_curr - 1)

    def partition(self, start, end):
        """Швидке сортування яке повертає індекс елемента,
        який розділяє масив на два: один з елементами
        меншими за опорний, інший з більшими"""
        pivot = self.lst[start]
        left = start - 1
        right = end

        while True:
            left = left + 1
            if self.ascending:
                while self.lst[left] < pivot:
                    self.count_of_comparisons += 1
                    left = left + 1
            else:
                while self.lst[left] > pivot:
                    self.count_of_comparisons += 1
                    left = left + 1
            right = right - 1
            if self.ascending:
                while self.lst[right] > pivot:
                    self.count_of_comparisons += 1
                    right = right - 1
            else:
                while self.lst[right] < pivot:
                    self.count_of_comparisons += 1
                    right = right - 1

            if left >= right:
                return right
            self.swap(left, right)

    def swap(self, i, j):
        """Функція для обміну елементів місцями. Оскільки швидке сортування в
        даній реалізації не дозволяє використовувати генератор для повернення
        проміжного вигляду масиву, то для забезпечення візуалізації кожного обміну
        використовується time.sleep(0.02). Час підібраний таким чином, щоб усі
        методи сортування виконувалися приблизно однаково, як і має бути враховуючи
        їх асимптотичну складність і щоб занадто частий виклик функції не спричиняв
        підвисання програми"""
        self.count_of_swaps += 1
        self.lst_control.draw_list({i: DrawInfo.GREEN_COLOR, j: DrawInfo.RED_COLOR}, True)
        time.sleep(0.015)
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]

    def heapsort(self, start, end):
        """Пірамідальне сортування певної частини масиву"""
        yield from self.build_heap(start, end)
        for i in range(end - 1, start, -1):
            self.swap(start, i)
            if self.ascending:
                yield from self.max_heapify(i=0, start=start, end=i)
            else:
                yield from self.min_heapify(i=0, start=start, end=i)

    def build_heap(self, start, end):
        """Створення купи"""
        length = end - start
        index = ((length - 1) - 1) // 2  # батько
        while index >= 0:
            if self.ascending:
                yield from self.max_heapify(index, start, end)
            else:
                yield from self.min_heapify(index, start, end)
            index -= 1

    def max_heapify(self, i, start, end):
        """Створення купи у якій нащадки не більші за предків"""
        size = end - start
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        self.count_of_comparisons += 2
        if l < size and self.lst[start + l] > self.lst[start + i]:
            largest = l
        if r < size and self.lst[start + r] > self.lst[start + largest]:
            largest = r
        if largest != i:
            self.swap(start + largest, start + i)
            yield from self.max_heapify(largest, start, end)

    def min_heapify(self, i, start, end):
        """Створення купи у якій нащадки не менші за предків"""
        size = end - start
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = i
        self.count_of_comparisons += 2
        if l < size and self.lst[start + l] < self.lst[start + i]:
            smallest = l
        if r < size and self.lst[start + r] < self.lst[start + smallest]:
            smallest = r
        if smallest != i:
            self.swap(start + smallest, start + i)
            yield from self.min_heapify(smallest, start, end)
