class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0
        res, l = 0, 0
        for r in range(len(arr)):
            curr_sum += arr[r]
            if r - l + 1 > k:
                curr_sum -= arr[l]
                l += 1
            if r - l + 1 == k and curr_sum / k >= threshold:
                res += 1
        return res