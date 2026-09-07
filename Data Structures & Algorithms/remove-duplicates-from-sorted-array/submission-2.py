class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res1 = set(nums)
        nums[:] = sorted(list(res1))
        return len(nums)