from Draw_Info import DrawInfo


def quick_sort(lst_control, ascending=True):
    lst = lst_control.get_lst()

    def quicksort(l, r):
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
                lst_control.draw_list({i: DrawInfo.BLUE_COLOR, l: DrawInfo.RED_COLOR, j: DrawInfo.GREEN_COLOR}, True)
                yield lst
        lst[l], lst[j] = lst[j], lst[l]
        lst_control.draw_list({l: DrawInfo.RED_COLOR, j: DrawInfo.GREEN_COLOR}, True)
        yield lst
        yield from quicksort(l, j - 1)
        yield from quicksort(j + 1, r)

    return quicksort(0, len(lst) - 1)
