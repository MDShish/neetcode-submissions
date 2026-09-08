class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
            else:
                return True
        return False