class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i,j])

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):  #enumerate -> returns index and value
            if target - num in seen:
                return([seen][target - num], i)
            elif num not in seen:
                seen[num] = i 