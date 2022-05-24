from Draw_Info import DrawInfo


class MergeSort:
    """Сортування злиттям: формально не має перестановок,
    але можна підраховувати скільки разів поточний елемент
    замінявся на інший з лівої або правої частини
    відсортованого масиву при злитті"""
    __SORTING_ALG_NAME = "Merge sort"

    def __init__(self, lst_control, ascending):
        self.__count_of_comparisons = 0
        self.__count_of_swaps = 0
        self.__lst_control = lst_control
        self.__lst = self.__lst_control.get_lst()
        self.__ascending = ascending

    def sort(self, start, end):
        """Підсвічується поточний елемент: синім якщо він
        був у правій частині, червоним, якщо у лівій"""
        if end - start > 1:
            middle = (start + end) // 2
            yield from self.sort(start, middle)
            yield from self.sort(middle, end)
            left = self.__lst[start:middle]
            right = self.__lst[middle:end]

            a = 0
            b = 0
            c = start

            while a < len(left) and b < len(right):
                self.__count_of_comparisons += 1
                if left[a] < right[b] and self.__ascending or left[a] > right[b] and not self.__ascending:
                    self.__count_of_swaps += 1
                    self.__lst_control.draw_list({c: DrawInfo.RED_COLOR}, True)
                    self.__lst[c] = left[a]
                    yield self.__lst
                    a += 1
                else:
                    self.__lst_control.draw_list({c: DrawInfo.BLUE_COLOR}, True)
                    self.__count_of_swaps += 1
                    self.__lst[c] = right[b]
                    yield self.__lst
                    b += 1
                c += 1

            while a < len(left):
                self.__count_of_swaps += 1
                self.__lst_control.draw_list({c: DrawInfo.RED_COLOR}, True)
                self.__lst[c] = left[a]
                a += 1
                c += 1

            while b < len(right):
                self.__count_of_swaps += 1
                self.__lst_control.draw_list({c: DrawInfo.BLUE_COLOR}, True)
                self.__lst[c] = right[b]
                b += 1
                c += 1
            yield self.__lst

    @staticmethod
    def get_name():
        return MergeSort.__SORTING_ALG_NAME

    def get_swaps(self):
        return self.__count_of_swaps

    def get_comparisons(self):
        return self.__count_of_comparisons

    def get_list(self):
        return self.__lst
