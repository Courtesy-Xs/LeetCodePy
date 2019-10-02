from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten = []
        for row in matrix:
            flatten += row

        return target in set(flatten)