class Solution(object):
    def topKFrequent(self, words, k):
        word_dict = {}
        result = []
        for word in words:
            if word not in word_dict:
                word_dict[word]=1
            else:
                word_dict[word]+=1
        
        sorted_keys = sorted(word_dict.keys(), key=lambda x: (-word_dict[x], x))
        return sorted_keys[:k]


       

        