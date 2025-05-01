class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr_int = ''
        for digit in digits:
            arr_int = arr_int + str(digit)
        result = str(int(arr_int) + 1)
        return [int(digit) for digit in result]