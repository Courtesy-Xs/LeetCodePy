from typing import  List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryBit = (digits[-1]+1)//10
        digits[-1] = (digits[-1]+1)%10
        for i in range(len(digits)-2,-1,-1):
            sum = digits[i] + carryBit
            carryBit = sum//10
            digits[i] = sum%10
        if carryBit:
            digits.insert(0,carryBit)
        return digits


if __name__ == '__main__':
    print(Solution().plusOne([9,9]))