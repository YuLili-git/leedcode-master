#输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#示例 1：
#输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
#输出：[1,2,3,6,9,8,7,4,5]
#示例 2：
#输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#输出：[1,2,3,4,8,12,11,10,9,5,6,7]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        u = 0
        b = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        res = []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[u][i])
            u += 1
            if u > b:
                break
            for i in range(u, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if u > b:
                break
            for i in range(b, u - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res
