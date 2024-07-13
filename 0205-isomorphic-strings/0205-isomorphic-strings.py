class Solution(object):
    def isIsomorphic(self, s, t):
        char_map = {}
        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]]= t[i]
            else:
                if t[i]!=char_map[s[i]]:
                    return False
        return True

        