class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i

        print(seen)
        for i, value in enumerate(seen):
            valueToFind = target - value
            if(seen.get(valueToFind) and seen[valueToFind] != i):
                print(seen.get(valueToFind))
                return [i, seen.get(valueToFind, 0)]


        return []