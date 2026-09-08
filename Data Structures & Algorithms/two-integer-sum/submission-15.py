class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            arr.append([i, num])
        arr.sort(key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while left < right:
            sum = arr[left][1] + arr[right][1]
            if sum == target:
                return [min(arr[left][0], arr[right][0]), max(arr[left][0], arr[right][0])]
            elif sum < target:
                left += 1
            else:
                right -= 1
        return []
