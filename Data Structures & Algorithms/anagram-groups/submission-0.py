class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = {}
        for i, value in enumerate(strs):
            arr["".join(sorted(value))] = []
        
        for i, value in enumerate(strs):
            if "".join(sorted(value)) in arr:
                arr["".join(sorted(value))].append(value)

        return list(arr.values())