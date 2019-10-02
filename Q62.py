import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n)//(math.factorial(m)*math.factorial(n))