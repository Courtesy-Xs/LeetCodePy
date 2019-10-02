from typing import List
import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #return [list(val) for val in itertools.combinations([i for i in range(n)],k)]
        if k==0:
            return [[]]
        return [j+[i] for i in range(k,n+1) for j in self.combine(i-1,k-1)]

        #为什么不能像之前 https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python
        #一样写成一行代码，因为这不是全排或者全组合（没意义），所以迭代到最后，依然还有值可取，不像之前全排列数组空了，最后等于0直接返回空数组，因此可以连写成一行代码
        #题目具体不同，也不要强求，就比如这个为例子，最后每次递归都会返回一个非空数组，因为i一直存在

if __name__ == '__main__':
    print(Solution().combine(4,2))




