def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def quicksort(draw_info, lst, l, r):
        """Червоний - поточний (опорний елемент), синій та зелений - елементи,
        що міняються місцями, причому синій - покажчик що змінюється від опорного
        елемента до правого краю розглядувальної ділянки, а зелений - покажчик
        що відповідає кількості елементів менших за опорний"""
        if l >= r:
            return
        x = lst[l]
        j = l
        for i in range(l + 1, r + 1):
            if lst[i] <= x and ascending or lst[i] >= x and not ascending:
                j += 1
                lst[j], lst[i] = lst[i], lst[j]
                draw_info.draw_list({i: draw_info.BLUE_COLOR, l: draw_info.RED_COLOR, j: draw_info.GREEN_COLOR}, True)
                yield lst
        lst[l], lst[j] = lst[j], lst[l]
        draw_info.draw_list({i: draw_info.GREEN_COLOR, l: draw_info.RED_COLOR, j: draw_info.GREEN_COLOR}, True)
        yield lst
        yield from quicksort(draw_info, lst, l, j - 1)
        yield from quicksort(draw_info, lst, j + 1, r)

    return quicksort(draw_info, lst, 0, len(lst) - 1)
