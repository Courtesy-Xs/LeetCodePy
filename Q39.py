from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        def backTrace(currSum,currList,mainList):
            for i in range(len(mainList)):
                if currSum+mainList[i] == target:
                    tempList = currList+[mainList[i]]
                    tempList.sort()
                    if tempList not in solution:
                        solution.append(tempList)
                    continue
                elif currSum+mainList[i] > target:
                    continue
                else:
                    backTrace(currSum+mainList[i],currList+[mainList[i]],mainList)
            return

        backTrace(0,[],candidates)
        return solution

if __name__ == '__main__':
    print(Solution().combinationSum([8,7,4,3],11))
