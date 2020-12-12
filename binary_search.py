from typing import List


def binary_search(L: List, val: int) -> int:
    left, right = 0, len(L) - 1

    while left <= right:
        middle = right - int((right - left) / 2)
        if L[middle] == val:
            return middle
        elif L[middle] < val:
            left = middle + 1
        else:
            right = middle + 1
    return -1


case = [1, 2, 3, 4, 5, 6, 7, 8]

print(binary_search(case, 3))