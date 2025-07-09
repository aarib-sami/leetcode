class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1

        while top <= bot:
            mid = (top + bot) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if not (top <= bot):
            return False

        l, r = 0, len(matrix[0])-1
        while l <= r:
            val = (l + r) // 2
            if target == matrix[mid][val]:
                return True
            elif target > matrix[mid][val]:
                l = val + 1
            else:
                r = val - 1

        return False