class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1,word2 = sorted(list(s)), sorted(list(t))

        if(word1 == word2):
            return True
        return False