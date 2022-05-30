import copy
from Draw_Info import DrawInfo


class QuickSort:
    """Швидке сортування, опорним обирається перший елемент масиву"""
    __SORTING_ALG_NAME = "Quick sort"

    def __init__(self, lst_control, ascending):
        self.__count_of_comparisons = 0
        self.__count_of_swaps = 0
        self.__lst_control = lst_control
        self.__lst = self.__lst_control.get_lst()
        self.__initial_lst = copy.deepcopy(self.__lst)
        self.__ascending = ascending

    def sort(self, l, r):
        """Червоний - поточний (опорний елемент), синій та зелений - елементи,
        що міняються місцями, причому синій - покажчик що змінюється від опорного
        елемента до правого краю розглядувальної ділянки, а зелений - покажчик
        що відповідає кількості елементів менших за опорний"""
        if r == len(self.__lst):
            r -= 1
        if l >= r:
            return
        x = self.__lst[l]
        j = l
        for i in range(l + 1, r + 1):
            self.__count_of_comparisons += 1
            if self.__lst[i] <= x and self.__ascending or self.__lst[i] >= x and not self.__ascending:
                j += 1
                if j != i:
                    self.__count_of_swaps += 1
                    self.__lst[j], self.__lst[i] = self.__lst[i], self.__lst[j]
                self.__lst_control.draw_list(
                    {i: DrawInfo.BLUE_COLOR, l: DrawInfo.RED_COLOR, j: DrawInfo.GREEN_COLOR}, True)
                yield self.__lst
        if l != j:
            self.__count_of_swaps += 1
            self.__lst[l], self.__lst[j] = self.__lst[j], self.__lst[l]
        self.__lst_control.draw_list({l: DrawInfo.RED_COLOR, j: DrawInfo.GREEN_COLOR}, True)
        yield self.__lst
        yield from self.sort(l, j - 1)
        yield from self.sort(j + 1, r)

    @staticmethod
    def get_name():
        return QuickSort.__SORTING_ALG_NAME

    def get_swaps(self):
        return self.__count_of_swaps

    def get_comparisons(self):
        return self.__count_of_comparisons

    def get_list(self):
        return self.__lst

    def get_initial_list(self):
        return self.__initial_lst
