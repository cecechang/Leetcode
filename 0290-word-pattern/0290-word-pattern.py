class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        pattern_to_word = {}

        word_set = set()
        for i, c in enumerate(pattern):
            word = words[i]
            if c not in pattern_to_word:
                if word in word_set:
                    return False
                pattern_to_word[c] = word
            else:
                if pattern_to_word[c] != word:
                    return False
        
        return True
            


        