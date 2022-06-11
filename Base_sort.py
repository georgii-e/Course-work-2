import copy


class BaseSort:
    """Базовий клас для всіх методів сортування"""
    def __init__(self, lst_control, ascending):
        self._count_of_comparisons = 0
        self._count_of_swaps = 0
        self._lst_control = lst_control
        self._lst = self._lst_control.get_lst()
        self._initial_lst = copy.deepcopy(self._lst)
        self._ascending = ascending

    def get_swaps(self):
        """Функція, що повертає кількість перестановок,
        що відбулись при сортуванні"""
        return self._count_of_swaps

    def get_comparisons(self):
        """Функція, що повертає кількість порівнянь,
        що відбулись при сортуванні"""
        return self._count_of_comparisons

    def get_list(self):
        """Функція, що повертає поточний масив"""
        return self._lst

    def get_initial_list(self):
        """Функція, що повертає початковий масив"""
        return self._initial_lst

