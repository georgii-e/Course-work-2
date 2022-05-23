from Draw_Info import DrawInfo


class QuickSort:
    """Швидке сортування, опорним обирається перший елемент масиву"""
    SORTING_ALG_NAME = "Quick sort"

    def __init__(self, lst_control, ascending):
        self.count_of_comparisons = 0
        self.count_of_swaps = 0
        self.lst_control = lst_control
        self.lst = self.lst_control.get_lst()
        self.ascending = ascending

    def sort(self, l, r):
        """Червоний - поточний (опорний елемент), синій та зелений - елементи,
        що міняються місцями, причому синій - покажчик що змінюється від опорного
        елемента до правого краю розглядувальної ділянки, а зелений - покажчик
        що відповідає кількості елементів менших за опорний"""
        if r == len(self.lst):
            r -= 1
        if l >= r:
            return
        x = self.lst[l]
        j = l
        for i in range(l + 1, r + 1):
            self.count_of_comparisons += 1
            if self.lst[i] <= x and self.ascending or self.lst[i] >= x and not self.ascending:
                j += 1
                if j != i:
                    self.count_of_swaps += 1
                self.lst[j], self.lst[i] = self.lst[i], self.lst[j]
                self.lst_control.draw_list({i: DrawInfo.BLUE_COLOR, l: DrawInfo.RED_COLOR, j: DrawInfo.GREEN_COLOR},
                                           True)
                yield self.lst
        if l != j:
            self.count_of_swaps += 1
        self.lst[l], self.lst[j] = self.lst[j], self.lst[l]
        self.lst_control.draw_list({l: DrawInfo.RED_COLOR, j: DrawInfo.GREEN_COLOR}, True)
        yield self.lst
        yield from self.sort(l, j - 1)
        yield from self.sort(j + 1, r)
