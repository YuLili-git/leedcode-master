#给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
#进阶：不要 使用任何内置的库函数，如  sqrt 。
#示例 1：
#输入：num = 16
#输出：true
#示例 2：
#输入：num = 14
#输出：false
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        i = 0
        j = num // 2
        while i < j:
            m = i + (j - i + 1) // 2
            if m * m > num:
                j = m - 1
            elif m * m < num:
                i = m
            else:
                return True
        return False
