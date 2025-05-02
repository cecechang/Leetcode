class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = set(nums)
        longest = 0
        for num in num_dict:
            if (num - 1) not in num_dict:
                length = 1
                while (num + length) in num_dict:
                    length += 1
                longest = max(length, longest)
        return longest

