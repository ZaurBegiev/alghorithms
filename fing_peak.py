from typing import List

def find_peak_element(nums: List[int]) -> int:
        n = len(nums) - 1
        
        if n == 0:
            return 0
        
        left, right = 0, n

        while left <= right:
            middle = left + (right - left) // 2
            if middle == n:
                return n

            if nums[middle] > nums[middle + 1]:
                if middle == 0:
                    return 0
                if nums[middle] > nums[middle - 1]:
                    return middle
                right = middle - 1
            else:
                left = middle + 1

# Test cases
cases = [
    [0],
    [1, 2, 3, 5],
    [2,1],
    [2,2],
    [1, 5, 1, 0],
]

for case in cases:
    print(case, find_peak_element(case))
