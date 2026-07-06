class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        
        for operation in operations:
            match operation:
                case 'C':
                    score.pop()
                case '+':
                    score.append(score[-1] + score[-2])
                case 'D':
                    score.append(score[-1] * 2)
                case _:
                    score.append(int(operation))

        return sum(score)