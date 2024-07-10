class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        substrings = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in substrings:
                substrings.remove(s[l])
                l += 1

            substrings.add(s[r])
            max_len = max(max_len, r-l+1)
        
        return max_len
        