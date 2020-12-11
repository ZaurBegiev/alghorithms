from typing import List

def merge(left: List, right: List):
    n = len(left) + len(right)
    result = []

    while len(result) != n:
        if not (left and right):
            return result + left + right
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result


def merge_sort(L: List) -> List:
    if len(L) < 2:
        return L
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


case_1 = []
case_2 = [1]
case_3 = [1, 3, 54215, 2, 4, 245, 12, 51, 8, 51, 6, 4, 3]

for case in (case_1, case_2, case_3)
    print(merge_sort(case))
