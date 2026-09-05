class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hsh = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                hsh.remove(nums[l])
                l += 1
            if nums[r] in hsh:
                return True
            hsh.add(nums[r])
        return False