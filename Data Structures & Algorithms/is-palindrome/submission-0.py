class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = "".join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(v) - 1
        while l < r:
            if v[l] != v[r]:
                return False
            l += 1
            r -= 1
        return True