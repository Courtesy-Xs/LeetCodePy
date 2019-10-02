class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #solution 3
        if num1 == "0" or num2 == "0":
            return "0"
        result = "0"
        carry1 = -4
        iterLen1 = len(num1)//4+1 if len(num1)%4!=0 else len(num1)//4
        iterLen2 = len(num2)//4+1 if len(num2)%4!=0 else len(num2)//4
        num1 = num1[::-1]
        num2 = num2[::-1]
        for a in range(iterLen1):
            carry1 += 4
            carry2 = -4
            for b in range(iterLen2):
                carry2 += 4
                plus1,plus2 = (str(int(num1[a*4:(a+1)*4][::-1])*int(num2[b*4:(b+1)*4][::-1]))+\
                               "0"*(carry1+carry2))[::-1],result[::-1]
                len1,len2 = len(plus1),len(plus2)
                carryBit = "0"
                result,i = "",0
                while i < max(len1,len2):
                    if i < min(len1,len2):
                        sum = int(plus1[i])+int(plus2[i])+int(carryBit)
                    else:
                        #不存在等于的情况
                        if len1>len2:
                            sum = int(plus1[i])+int(carryBit)
                        else:
                            sum = int(plus2[i])+int(carryBit)
                    carryBit = str(sum//10)
                    result = str(sum)[-1]+result
                    i+=1
                if int(carryBit):
                    result = carryBit+result
        return result

        # solution 2
        # if num1 == "0" or num2 == "0":
        #     return "0"
        # result = "0"
        # carry1 = -1
        # for a in num1[::-1]:
        #     carry1+=1
        #     carry2 = -1
        #     for b in num2[::-1]:
        #         carry2+=1
        #         plus1,plus2 = (str(int(a)*int(b))+"0"*(carry1+carry2))[::-1],result[::-1]
        #         len1,len2 = len(plus1),len(plus2)
        #         carryBit = "0"
        #         result,i = "",0
        #         while i < max(len1,len2):
        #             if i < min(len1,len2):
        #                 sum = int(plus1[i])+int(plus2[i])+int(carryBit)
        #             else:
        #                 #不存在等于的情况
        #                 if len1>len2:
        #                     sum = int(plus1[i])+int(carryBit)
        #                 else:
        #                     sum = int(plus2[i])+int(carryBit)
        #             carryBit = str(sum//10)
        #             result = str(sum)[-1]+result
        #             i+=1
        #         if int(carryBit):
        #             result = carryBit+result
        # return result

        #solution1:
        # def multiply(self, num1: str, num2: str) -> str:
    #     result = "0"
    #     carry1 = -1
    #     for a in num1[::-1]:
    #         carry1+=1
    #         carry2 = -1
    #         for b in num2[::-1]:
    #             carry2+=1
    #             result = self.strPlus(result,str(int(a)*int(b))+"0"*(carry1+carry2))
    #     return result
    # def strPlus(self,num1,num2):
    #     len1 = len(num1)
    #     len2 = len(num2)
    #     num1 = num1[::-1]
    #     num2 = num2[::-1]
    #     carryBit = "0"
    #     result = ""
    #     i = 0
    #     while i < max(len1,len2):
    #         if i < min(len1,len2):
    #             sum = int(num1[i])+int(num2[i])+int(carryBit)
    #         else:
    #             #不存在等于的情况
    #             if len1>len2:
    #                 sum = int(num1[i])+int(carryBit)
    #             else:
    #                 sum = int(num2[i])+int(carryBit)
    #         carryBit = str(sum//10)
    #         result = str(sum)[-1]+result
    #         i+=1
    #     if int(carryBit):
    #         result = carryBit+result
    #     return result


if __name__ == '__main__':
    print(Solution().multiply("12345","12"))







