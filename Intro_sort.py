from math import log2, floor
import time


def intro_sort(draw_info, ascending=True):
    """Інтроспективне сортування: швидке сортування,
    яке перемикається на пірамідальне при досяжності
    max_depth = floor(log2(len(lst)))"""
    lst = draw_info.lst
    max_depth = floor(log2(len(lst)))

    def intro_sort_helper(start, end, max_depth_curr):
        if end - start <= 1:
            return
        elif max_depth_curr == 0:
            yield from heapsort(start, end)
        else:
            p = partition(start, end)
            yield lst
            yield from intro_sort_helper(start, p + 1, max_depth_curr - 1)
            yield lst
            yield from intro_sort_helper(p + 1, end, max_depth_curr - 1)

    def partition(start, end):
        """Швидке сортування яке повертає індекс елемента,
        який розділяє масив на два: один з елементами
        меншими за опорний, інший з більшими"""
        pivot = lst[start]
        left = start - 1
        right = end

        while True:
            left = left + 1
            if ascending:
                while lst[left] < pivot:
                    left = left + 1
            else:
                while lst[left] > pivot:
                    left = left + 1
            right = right - 1
            if ascending:
                while lst[right] > pivot:
                    right = right - 1
            else:
                while lst[right] < pivot:
                    right = right - 1

            if left >= right:
                return right
            swap(left, right)

    def swap(i, j):
        """Функція для обміну елементів місцями. Оскільки швидке сортування в
        даній реалізації не дозволяє використовувати генератор для повернення
        проміжного вигляду масиву, то для забезпечення візуалізації кожного обміну
        використовується time.sleep(0.02). Час підібраний таким чином, щоб усі
        методи сортування виконувалися приблизно однаково, як і має бути враховуючи
        їх асимптотичну складність і щоб занадто частий виклик функції не спричиняв
        підвисання програми"""
        draw_info.draw_list({i: draw_info.GREEN_COLOR, j: draw_info.RED_COLOR}, True)
        time.sleep(0.015)
        lst[i], lst[j] = lst[j], lst[i]

    def heapsort(start, end):
        """Пірамідальне сортування певної частини масиву"""
        yield from build_heap(start, end)
        for i in range(end - 1, start, -1):
            swap(start, i)
            if ascending:
                yield from max_heapify(i=0, start=start, end=i)
            else:
                yield from min_heapify(i=0, start=start, end=i)

    def build_heap(start, end):
        """Створення купи"""
        length = end - start
        index = ((length - 1) - 1) // 2  # батько
        while index >= 0:
            if ascending:
                yield from max_heapify(index, start, end)
            else:
                yield from min_heapify(index, start, end)
            index -= 1

    def max_heapify(i, start, end):
        """Створення купи у якій нащадки не більші за предків"""
        size = end - start
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if l < size and lst[start + l] > lst[start + i]:
            largest = l
        if r < size and lst[start + r] > lst[start + largest]:
            largest = r
        if largest != i:
            swap(start + largest, start + i)
            yield from max_heapify(largest, start, end)

    def min_heapify(i, start, end):
        """Створення купи у якій нащадки не менші за предків"""
        size = end - start
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = i
        if l < size and lst[start + l] < lst[start + i]:
            smallest = l
        if r < size and lst[start + r] < lst[start + smallest]:
            smallest = r
        if smallest != i:
            swap(start + smallest, start + i)
            yield from min_heapify(smallest, start, end)

    yield from intro_sort_helper(0, len(lst), max_depth)
