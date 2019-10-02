from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_nums = {2:["a","b","c"],3:["d","e","f"],4:["g","h","i"], \
                     5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"], \
                     8:["t","u","v"],9:["w","x","y","z"]}
        if len(digits)<1:
            return []
        strSet = [""]
        for a in digits:
            tempLen = len(strSet)
            for b in range(tempLen):
                for c in dict_nums[int(a)]:
                    tempStr = strSet[b]+c
                    strSet.append(tempStr)
            strSet = strSet[tempLen:]
        return strSet


if __name__ == '__main__':
    print(Solution().letterCombinations("234"))
