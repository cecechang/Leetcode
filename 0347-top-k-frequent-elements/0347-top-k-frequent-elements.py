class Solution(object):
    def topKFrequent(self, nums, k):
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num]+=1
            else:
                num_dict[num]=1

        sorted_dict = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
        top_k_keys = [key for key, value in sorted_dict[:k]]

        return top_k_keys
        