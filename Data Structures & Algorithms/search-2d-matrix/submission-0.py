class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch(row, target):
            left = 0
            right = len(row) - 1

            while left <= right:
                mid = (left + right) // 2

                if row[mid] == target:
                    return True
                elif target < row[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return False

        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return binarysearch(matrix[i], target)

        return False