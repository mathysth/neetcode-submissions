class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        arrLength, res, tempMaxVal = len(arr), [], 0
        for i in range(arrLength):
            tempMaxVal = 0
            for j in range(i + 1, arrLength):
                if arr[j] > tempMaxVal:
                    tempMaxVal = arr[j]

            if(i == (arrLength-1)):
                res.append(-1)
            else:
                print('maxval', tempMaxVal)
                res.append(tempMaxVal)

        return res