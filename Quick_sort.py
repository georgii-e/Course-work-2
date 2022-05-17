import random


def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    return quicksort(draw_info, lst, 0, len(lst) - 1)

def quicksort(draw_info, a, l, r):
    if l >= r:
        return
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
            draw_info.draw_list({i: draw_info.GREEN_COLOR, l: draw_info.WHITE_COLOR, j: draw_info.RED_COLOR}, True)
        yield a
    a[l], a[j] = a[j], a[l]
    draw_info.draw_list({i: draw_info.GREEN_COLOR, j: draw_info.RED_COLOR}, True)
    yield a

    # yield from statement used to yield
    # the array after dividing
    yield from quicksort(draw_info, a, l, j - 1)
    yield from quicksort(draw_info, a, j + 1, r)
