"""
Бинарный поиск - алгоритм поиска в отсортированном массиве, где массив делиться пополам
"""
# дан отсортированный массив
m = [1, 3, 5, 7, 9, 11, 13, 15, 17]


def binary_search(massive, value):
    # минимальное значение в отсортированном списке всегда имеет индекс 0
    low = 0
    # максимальное будет иметь последний индекс в массиве
    high = len(massive) - 1

    while low <= high:
        # поиск среднего значения
        middle = int((low + high) / 2)
        result = massive[middle]
        if result == value:
            return middle
        elif result > value:
            high = middle - 1
        else:
            low = middle + 1
    return None


print(binary_search(m, 11))
