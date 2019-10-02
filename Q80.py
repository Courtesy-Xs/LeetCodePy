from typing import List
class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        L, j = len(n), 2
        for i in range(2,L):
            if n[i] > n[j-2]: n[j], j = n[i], j + 1
        return j

if __name__ == '__main__':
    print(Solution().removeDuplicates([1]))