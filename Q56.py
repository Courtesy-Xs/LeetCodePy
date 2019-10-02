from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        if len(intervals)<=1:
            return intervals
        result = [intervals[0]]
        for val in intervals:
            if val[0]<=result[-1][-1]:
                result[-1][-1] = max(val[1],result[-1][-1])
            else:
                result.append(val)
        return result





if __name__ == '__main__':
    nums = [[1,3],[0,2],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]]
    print(Solution().merge(nums))
