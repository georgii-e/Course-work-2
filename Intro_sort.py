from math import log2, floor
from Base_sort import BaseSort
from Draw_Info import DrawInfo
import Config
import time


class IntroSort(BaseSort):
    """Інтроспективне сортування: швидке сортування,
    яке перемикається на пірамідальне при досяжності
    max_depth = floor(log2(len(lst)))"""
    SORTING_ALG_NAME = "Intro sort"

    def __init__(self, lst_control, ascending):
        super(IntroSort, self).__init__(lst_control, ascending)
        self.__max_depth = floor(log2(len(self._lst)))

    def sort(self, start, end, max_depth_curr=None):
        if max_depth_curr is None:
            max_depth_curr = self.__max_depth
        if end - start <= 1:
            return
        elif max_depth_curr == 0:
            yield from self.heapsort(start, end)
        else:
            p = self.partition(start, end)
            yield self._lst
            yield from self.sort(start, p + 1, max_depth_curr - 1)
            yield self._lst
            yield from self.sort(p + 1, end, max_depth_curr - 1)

    def partition(self, start, end):
        """Швидке сортування яке повертає індекс елемента,
        який розділяє масив на два: один з елементами
        меншими за опорний, інший з більшими"""
        pivot = self._lst[start]
        left = start - 1
        right = end

        while True:
            left += 1
            if self._ascending:
                while self._lst[left] < pivot:
                    self._count_of_comparisons += 1
                    left += 1
            else:
                while self._lst[left] > pivot:
                    self._count_of_comparisons += 1
                    left += 1
            right -= 1
            if self._ascending:
                while self._lst[right] > pivot:
                    self._count_of_comparisons += 1
                    right -= 1
            else:
                while self._lst[right] < pivot:
                    self._count_of_comparisons += 1
                    right -= 1

            if left >= right:
                return right
            self.swap(left, right)

    def swap(self, i, j):
        """Функція для обміну елементів місцями. Оскільки швидке сортування в
        даній реалізації не дозволяє використовувати генератор для повернення
        проміжного вигляду масиву, то для забезпечення візуалізації кожного обміну
        використовується time.sleep(0.01)"""
        self._count_of_swaps += 1
        self._lst_control.draw_list({i: DrawInfo.GREEN_COLOR, j: DrawInfo.RED_COLOR}, True)
        if len(self._lst) < Config.MAX_AMOUNT_TO_VIS:
            time.sleep(0.01)
        self._lst[i], self._lst[j] = self._lst[j], self._lst[i]

    def heapsort(self, start, end):
        """Пірамідальне сортування певної частини масиву"""
        yield from self.build_heap(start, end)
        for i in range(end - 1, start, -1):
            self.swap(start, i)
            if self._ascending:
                yield from self.max_heapify(i=0, start=start, end=i)
            else:
                yield from self.min_heapify(i=0, start=start, end=i)

    def build_heap(self, start, end):
        """Створення купи"""
        length = end - start
        index = ((length - 1) - 1) // 2  # батько
        while index >= 0:
            if self._ascending:
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
        self._count_of_comparisons += 2
        if l < size and self._lst[start + l] > self._lst[start + i]:
            largest = l
        if r < size and self._lst[start + r] > self._lst[start + largest]:
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
        self._count_of_comparisons += 2
        if l < size and self._lst[start + l] < self._lst[start + i]:
            smallest = l
        if r < size and self._lst[start + r] < self._lst[start + smallest]:
            smallest = r
        if smallest != i:
            self.swap(start + smallest, start + i)
            yield from self.min_heapify(smallest, start, end)

