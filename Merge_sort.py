from Draw_Info import DrawInfo


class MergeSort:
    """Сортування злиттям: формально не має перестановок,
    але можна підраховувати скільки разів поточний елемент
    замінявся на інший з лівої або правої частини
    відсортованого масиву при злитті"""
    SORTING_ALG_NAME = "Merge sort"

    def __init__(self, lst_control, ascending):
        self.count_of_comparisons = 0
        self.count_of_swaps = 0
        self.lst_control = lst_control
        self.lst = self.lst_control.get_lst()
        self.ascending = ascending

    def sort(self, start, end):
        """Підсвічується поточний елемент: синім якщо він
        був у правій частині, червоним, якщо у лівій"""
        if end - start > 1:
            middle = (start + end) // 2
            yield from self.sort(start, middle)
            yield from self.sort(middle, end)
            left = self.lst[start:middle]
            right = self.lst[middle:end]

            a = 0
            b = 0
            c = start

            while a < len(left) and b < len(right):
                self.count_of_comparisons += 1
                if left[a] < right[b] and self.ascending or left[a] > right[b] and not self.ascending:
                    self.count_of_swaps += 1
                    self.lst_control.draw_list({c: DrawInfo.RED_COLOR}, True)
                    self.lst[c] = left[a]
                    yield self.lst
                    a += 1
                else:
                    self.lst_control.draw_list({c: DrawInfo.BLUE_COLOR}, True)
                    self.count_of_swaps += 1
                    self.lst[c] = right[b]
                    yield self.lst
                    b += 1
                c += 1

            while a < len(left):
                self.count_of_swaps += 1
                self.lst_control.draw_list({c: DrawInfo.RED_COLOR}, True)
                self.lst[c] = left[a]
                a += 1
                c += 1

            while b < len(right):
                self.count_of_swaps += 1
                self.lst_control.draw_list({c: DrawInfo.BLUE_COLOR}, True)
                self.lst[c] = right[b]
                b += 1
                c += 1
            yield self.lst
