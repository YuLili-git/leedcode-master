#给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#示例 1：
#输入：n = 3
#输出：[[1,2,3],[8,9,4],[7,6,5]]
#示例 2：
#输入：n = 1
#输出：[[1]]
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        number = 1
        while left < right and up < down:
            for i in range(left, right):
                matrix[up][i] = number
                number += 1
            for i in range(up, down):
                matrix[i][right] = number
                number += 1
            for i in range(right, left, -1):
                matrix[down][i] = number
                number += 1
            for i in range(down, up, -1):
                matrix[i][left] = number
                number += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        if n % 2:
            matrix[n // 2][n // 2] = number
        return  matrix
