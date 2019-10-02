from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        candidates.sort()
        def backTrace(currSum,currList,mainList):
            for i in range(len(mainList)):
                if currSum+mainList[i]>target:
                    return
                elif currSum+mainList[i]==target:
                    if currList+[mainList[i]] not in solution:
                        solution.append(currList+[mainList[i]])
                    return
                else:
                    backTrace(currSum+mainList[i],currList+[mainList[i]],mainList[i+1:])
            return
        backTrace(0,[],candidates)
        return solution

