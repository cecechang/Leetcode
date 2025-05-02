class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lst2_dict = {item: index for index, item in enumerate(list2)}
        
        min_sum = len(list1) + len(list2)
        current_sum = 0
        result = []

        for i in range(len(list1)):
            if list1[i] in lst2_dict:
                current_sum = i + lst2_dict[list1[i]]

                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [list1[i]]
                elif current_sum == min_sum:
                    result.append(list1[i])
        
        return result

