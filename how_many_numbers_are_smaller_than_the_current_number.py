class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_arr = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
                
            count_arr.append(count)
        
        return count_arr
        