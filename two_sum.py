class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            df = target - nums[i]
            if df in seen:
                return [seen[df], i]
            seen[nums[i]] = i
        
        return None
        