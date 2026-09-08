class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ''
        for num in digits:
            st += str(num)
        num = int(st) + 1
        return [int(digit) for digit in str(num)]