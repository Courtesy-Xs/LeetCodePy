class Solution:
    def intToRoman(self, num: int) -> str:
        dict_Romen = [["I","V"],["X","L"],["C","D"],["M",""]]
        i = 0
        ant = ""
        while num>0:
            digit=num%10
            if digit<4:
                ant=dict_Romen[i][0]*digit+ant
            elif digit<9:
                ant=dict_Romen[i][0]*(5-digit)+dict_Romen[i][1]+dict_Romen[i][0]*(digit-5)+ant
            else:
                ant=dict_Romen[i][0]+dict_Romen[i+1][0]+ant
            num//=10
            i+=1
        return ant
                