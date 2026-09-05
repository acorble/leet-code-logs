"""74. Search a 2D Matrix

https://leetcode.com/problems/search-a-2d-matrix/
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        totalNumber = len(matrix) * len(matrix[0])
        left, right = 0, totalNumber - 1

        while left <= right:
            middle = left + (right - left) // 2
            row = middle // len(matrix[0])
            col = middle % len(matrix[0])

            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = middle - 1
            else:
                left = middle + 1

        return False
