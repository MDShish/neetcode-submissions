from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    # n = 0
    # while nums:
    #     n += 1
    # i = 0
    # while i < n:
    #     if nums[i] == target:
    #         return i
    for i, n in enumerate(nums):
        if n == target:
            return i


# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

