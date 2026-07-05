class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsecutifOne = 0
        tempMaxConsecutifOne = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tempMaxConsecutifOne += 1

            if tempMaxConsecutifOne > maxConsecutifOne:
                maxConsecutifOne = tempMaxConsecutifOne

            if nums[i] != 1:
                tempMaxConsecutifOne = 0

        return maxConsecutifOne
