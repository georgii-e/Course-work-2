from Draw_Info import DrawInfo


def merge_sort(lst_control, ascending=True):
    lst = lst_control.lst

    def mergesort(start, end):
        """Підсвічується поточний елемент: синім якщо він
        був у правій частині, червоним, якщо у лівій"""
        if end - start > 1:
            middle = (start + end) // 2
            yield from mergesort(start, middle)
            yield from mergesort(middle, end)
            left = lst[start:middle]
            right = lst[middle:end]

            a = 0
            b = 0
            c = start

            while a < len(left) and b < len(right):
                if left[a] < right[b] and ascending or left[a] > right[b] and not ascending:
                    lst_control.draw_list({c: DrawInfo.RED_COLOR}, True)
                    lst[c] = left[a]
                    yield lst
                    a += 1
                else:
                    lst_control.draw_list({c: DrawInfo.BLUE_COLOR}, True)
                    lst[c] = right[b]
                    yield lst
                    b += 1
                c += 1

            while a < len(left):
                lst_control.draw_list({c: DrawInfo.RED_COLOR}, True)
                lst[c] = left[a]
                a += 1
                c += 1

            while b < len(right):
                lst_control.draw_list({c: DrawInfo.BLUE_COLOR}, True)
                lst[c] = right[b]
                b += 1
                c += 1
            yield lst

    return mergesort(0, len(lst))
