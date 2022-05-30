from Quick_sort import QuickSort
from Intro_sort import IntroSort
from Merge_sort import MergeSort

n = 150  # початкова кількість елементів
min_v = -100  # межі генерації
max_v = 100  # випадкових чисел
sorting_algorithm = QuickSort  # алгоритм сортування за умовчання
path = "output.txt"  # шлях до файлу для запису вихідних даних
MAX_AMOUNT_TO_VIS = 500  # максимальна кількість елементів, сортування яких буде візуалізуватися
FPS = 75  # кількість оновлень головного циклу в секунду
SOUNDS_ON = True  # увімкнення звуків
