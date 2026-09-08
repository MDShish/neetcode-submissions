class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0
        nums.sort()
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
            else:
                return True
        return False