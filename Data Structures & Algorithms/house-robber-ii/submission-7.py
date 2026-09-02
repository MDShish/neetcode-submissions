class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper(self, nums: list[int])->int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0],dp[1]=nums[0],max(nums[0],nums[1])
        for _ in range(2,len(nums)):
            dp[_]=max(dp[_-2]+nums[_],dp[_-1])
        return dp[-1]