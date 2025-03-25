class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1List = list(word1)
        word2List = list(word2)
        resultList = []
        i = 0
        j = 0
        counter = 0

        while i < len(word1) or j < len(word2):
            if counter % 2 == 0 and i < len(word1):
                resultList.append(word1List[i])
                i += 1
            elif counter % 2 == 1 and j < len(word2):
                resultList.append(word2List[j])
                j += 1

            counter += 1

        return "".join(resultList)
