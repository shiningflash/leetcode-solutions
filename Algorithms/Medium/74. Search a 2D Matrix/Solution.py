class Solution:
    def binarySearchLowerBound(self, matrix: List[List[int]], target: int) -> int:
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][-1] < target:
                low = mid + 1
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                return mid
        return low
    
    def binarySearch(self, matrix: List[List[int]], target: int, row: int) -> int:
        if row >= len(matrix):
            return False
        
        low = 0
        high = len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.binarySearchLowerBound(matrix, target)
        return self.binarySearch(matrix, target, row)
        
        