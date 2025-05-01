class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (1 + n) * n / 2
        actual_sum = sum(nums)
        return int(expected_sum - actual_sum)

