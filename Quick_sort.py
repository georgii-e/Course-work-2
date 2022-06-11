from Base_sort import BaseSort
from Draw_Info import DrawInfo


class QuickSort(BaseSort):
    """Швидке сортування, опорним обирається перший елемент масиву"""
    SORTING_ALG_NAME = "Quick sort"

    def __init__(self, lst_control, ascending):
        super(QuickSort, self).__init__(lst_control, ascending)

    def sort(self, l, r):
        """Червоний - поточний (опорний елемент), синій та зелений - елементи,
        що міняються місцями, причому синій - покажчик що змінюється від опорного
        елемента до правого краю розглядувальної ділянки, а зелений - покажчик
        що відповідає кількості елементів менших за опорний"""
        if r == len(self._lst):
            r -= 1
        if l >= r:
            return
        x = self._lst[l]
        j = l
        for i in range(l + 1, r + 1):
            self._count_of_comparisons += 1
            if self._lst[i] <= x and self._ascending or self._lst[i] >= x and not self._ascending:
                j += 1
                if j != i:
                    self._count_of_swaps += 1
                    self._lst[j], self._lst[i] = self._lst[i], self._lst[j]
                self._lst_control.draw_list(
                    {i: DrawInfo.BLUE_COLOR, l: DrawInfo.RED_COLOR, j: DrawInfo.GREEN_COLOR}, True)
                yield self._lst
        if l != j:
            self._count_of_swaps += 1
            self._lst[l], self._lst[j] = self._lst[j], self._lst[l]
        self._lst_control.draw_list({l: DrawInfo.RED_COLOR, j: DrawInfo.GREEN_COLOR}, True)
        yield self._lst
        yield from self.sort(l, j - 1)
        yield from self.sort(j + 1, r)

