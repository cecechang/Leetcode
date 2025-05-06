class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        set_3 = set(nums3)
        res = set()

        for num in set_1:
            if num in set_2 or num in set_3:
                res.add(num)

        for num in set_2:
            if num in set_1 or num in set_3:
                res.add(num)

        for num in set_3:
            if num in set_1 or num in set_2:
                res.add(num)
        
        return list(res)

        