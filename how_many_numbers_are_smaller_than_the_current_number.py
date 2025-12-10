from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_arr = sorted(nums)
        d = {}

        for i,num in enumerate(sorted_arr):
            if num not in d:
                d[num] = i
        
        output_arr = []
        for num in nums:
            output_arr.append(d[num])
        
        return output_arr