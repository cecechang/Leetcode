class Solution(object):
    def longestPalindrome(self, s):
        char_dict = {}
        odd_count_found = False
        total = 0
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        for count in char_dict.values():
            if count %2 == 0:
                total += count
            else:
                total += count -1
                odd_count_found = True

        if odd_count_found:
            total += 1
            
        return total

        