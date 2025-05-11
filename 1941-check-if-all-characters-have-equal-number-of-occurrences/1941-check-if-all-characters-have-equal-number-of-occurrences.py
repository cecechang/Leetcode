class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        count_set = set(count.values())
        return len(count_set) == 1
        