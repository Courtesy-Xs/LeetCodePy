class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(val) for val in a[::-1]]
        b = [int(val) for val in (b[::-1])]
        result = []
        carryBit = 0
        i,j = 0,0
        while i<len(a) and j<len(b):
            result.insert(0,str((a[i]+b[j]+carryBit)%2))
            carryBit = (a[i]+b[j]+carryBit)//2
            i+=1
            j+=1

        while i<len(a):
            result.insert(0,str((a[i]+carryBit)%2))
            carryBit = (a[i]+carryBit)//2
            i+=1
        while j<len(b):
            result.insert(0,str((b[j]+carryBit)%2))
            carryBit = (b[j]+carryBit)//2
            j+=1
        if carryBit:
            result.insert(0,str(carryBit))

        return "".join(result)

if __name__ == '__main__':
    a = "1"
    b = "111"
    print(Solution().addBinary(a,b))