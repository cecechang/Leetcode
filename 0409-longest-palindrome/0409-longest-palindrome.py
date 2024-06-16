class Solution(object):
    def longestPalindrome(self, s):
        char_dict = {}
        max_odd = 0
        total = 0
        for char in s:
            char_dict[char] = s.count(char)
        for key in char_dict.keys():
            if char_dict[key] %2 == 0:
                total += char_dict[key]
            elif char_dict[key]> max_odd:
                max_odd = char_dict[key]
        return total + max_odd

        