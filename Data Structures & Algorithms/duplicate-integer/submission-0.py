class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = False
        arr = {}
        for i in range(len(nums)):
            arr[nums[i]] = arr.get(nums[i], 0) + 1
            if(arr[nums[i]] > 1):
                hasDuplicate = True
        
        return hasDuplicate