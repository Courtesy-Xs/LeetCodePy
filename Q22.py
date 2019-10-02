from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        S = set()
        templist = [""]
        for i in range(n):
            size = len(templist)
            for i in range(size):
                valList = list(templist[i])
                for i in range(len(valList)+1):
                    temp = valList[:]
                    temp.insert(i,"()")
                    resStr = "".join(temp)
                    if resStr not in templist:
                        templist.append("".join(temp))
            templist = templist[size:]
        for val in templist:
            S.add(val)
        return S

if __name__ == '__main__':
    print(Solution().generateParenthesis(4))
