from Base_sort import BaseSort
from Draw_Info import DrawInfo


class MergeSort(BaseSort):
    """Сортування злиттям: формально не має перестановок,
    але можна підраховувати скільки разів поточний елемент
    замінявся на інший з лівої або правої частини
    відсортованого масиву при злитті"""
    SORTING_ALG_NAME = "Merge sort"

    def __init__(self, lst_control, ascending):
        super(MergeSort, self).__init__(lst_control, ascending)

    def sort(self, start, end):
        """Підсвічується поточний елемент: синім якщо він
        був у правій частині, червоним, якщо у лівій"""
        if end - start > 1:
            middle = (start + end) // 2
            yield from self.sort(start, middle)
            yield from self.sort(middle, end)
            left = self._lst[start:middle]
            right = self._lst[middle:end]

            a = 0
            b = 0
            c = start

            while a < len(left) and b < len(right):
                self._count_of_comparisons += 1
                if left[a] < right[b] and self._ascending or left[a] > right[b] and not self._ascending:
                    self._count_of_swaps += 1
                    self._lst_control.draw_list({c: DrawInfo.RED_COLOR}, True)
                    self._lst[c] = left[a]
                    yield self._lst
                    a += 1
                else:
                    self._lst_control.draw_list({c: DrawInfo.BLUE_COLOR}, True)
                    self._count_of_swaps += 1
                    self._lst[c] = right[b]
                    yield self._lst
                    b += 1
                c += 1

            while a < len(left):
                self._count_of_swaps += 1
                self._lst_control.draw_list({c: DrawInfo.RED_COLOR}, True)
                self._lst[c] = left[a]
                a += 1
                c += 1

            while b < len(right):
                self._count_of_swaps += 1
                self._lst_control.draw_list({c: DrawInfo.BLUE_COLOR}, True)
                self._lst[c] = right[b]
                b += 1
                c += 1
            yield self._lst

