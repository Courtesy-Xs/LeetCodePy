import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # result = list(permutations([str(i) for i in range(1,n+1)],n))
        # return "".join(result[k-1])

        if n==0:
            return ""
        if n==1:
            return "1"
        result = ""
        arr = [i for i in range(1,n+1)]
        k-=1
        le = math.factorial(n-1)
        for i in range(1,n):
            result+=str(arr[k//le])
            del arr[k//le]
            k%=le
            le//=(n-i)
        result+=str(arr[0])
        return result






if __name__ == '__main__':
    print(Solution().getPermutation(3,3))
