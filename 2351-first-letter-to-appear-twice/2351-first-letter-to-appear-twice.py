class Solution(object):
    def repeatedCharacter(self, s):
        seen_char = set()
        for char in s:
            if char in seen_char:
                return char
            else: seen_char.add(char)
        