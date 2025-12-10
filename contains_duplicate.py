from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()
        for num in nums:
            dictionary[num] = 0

        for num in nums:
            dictionary[num] += 1
        
        for _, value in dictionary.items():
            if value > 1:
                return True
    
        return False