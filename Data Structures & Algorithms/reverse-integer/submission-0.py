class Solution:
    def reverse(self, x: int) -> int:
        store = x
        x = abs(x)
        res = int(str(x)[::-1])
        if store < 0: res *= -1
        if res > 2**31 or res < -2 ** 31: return 0
        return res