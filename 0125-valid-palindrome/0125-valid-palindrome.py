class Solution(object):
    def isPalindrome(self, s):
        alphabet_list = [char for char in s if char.isalpha() or char.isdigit()]
        new_s = ''.join(alphabet_list)
        if new_s.lower() == new_s[::-1].lower():
            return True
        else:
            return False
        