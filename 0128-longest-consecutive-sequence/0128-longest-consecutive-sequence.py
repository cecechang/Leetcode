class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = set(nums)
        cur_count = 0
        max_count = 0
        for num in num_dict:
            if (num - 1) in num_dict:
                continue
            cur_count = 1
            cur_num = num
            while cur_num + 1 in num_dict:
                cur_num += 1
                cur_count += 1
            max_count = max(cur_count, max_count)
        return max_count

