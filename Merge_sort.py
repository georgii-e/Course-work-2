def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def mergesort(start, end):
        """Червоний - поточний елемент, зелений - той що ставиться на його місце при злитті"""
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
                if left[a] < right[b]:
                    lst[c] = left[a]
                    draw_info.draw_list({a: draw_info.GREEN_COLOR, c: draw_info.RED_COLOR}, True)
                    yield lst
                    a += 1
                else:
                    lst[c] = right[b]
                    draw_info.draw_list({len(left)+b: draw_info.GREEN_COLOR, c: draw_info.RED_COLOR}, True)
                    yield lst
                    b += 1
                c += 1

            while a < len(left):
                lst[c] = left[a]
                a += 1
                c += 1

            while b < len(right):
                lst[c] = right[b]
                b += 1
                c += 1
            draw_info.draw_list({start: draw_info.GREEN_COLOR, middle: draw_info.RED_COLOR, end: draw_info.GREEN_COLOR},
                                True)
            yield lst

    return mergesort(0, len(lst))
