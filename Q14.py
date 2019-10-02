from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        resultStr = strs[0]
        minLength = len(strs[0])
        for j in range(1,len(strs)):
            if minLength >len(strs[j]):
                minLength = len(strs[j])
            resultStr = resultStr[0:minLength]
            for k in range(minLength):
                if resultStr[k] == strs[j][k]:
                    continue
                else:
                    resultStr = resultStr[0:k]
                    minLength = k
                    break
        return resultStr if len(resultStr)>0 else ""

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))