class Solution:
    def romanToInt(self, s: str) -> int:
        dict_Romen = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        resultInt = 0
        for i in range(len(s)-1):
            if dict_Romen[s[i]]<dict_Romen[s[i+1]]:
                resultInt-=dict_Romen[s[i]]
            else:
                resultInt+=dict_Romen[s[i]]
        resultInt+=dict_Romen[s[len(s)-1]]
        return resultInt

