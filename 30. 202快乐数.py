#编写一个算法来判断一个数 n 是不是快乐数。
#「快乐数」定义为：
#对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
#然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
#如果 可以变为  1，那么这个数就是快乐数。
#如果 n 是快乐数就返回 true ；不是，则返回 false 。
#示例 1：
#输入：19
#输出：true
#解释：
#12 + 92 = 82
#82 + 22 = 68
#62 + 82 = 100
#12 + 02 + 02 = 1
#示例 2：
#输入：n = 2
#输出：false
########################### solution 1 ###########################
class Solution:
    def isHappy(self, n: int) -> bool:
        res = []
        while n < 2 ** 31:
            m = str(n)
            num = 0
            for i in m:
                num += int(i) ** 2
            res.append(num)
            if num == 1:
                return True
            if num in res[:-1]:
                return False
            n = num
        return False
########################### solution 2 ###########################
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy(num):
            sum_ = 0
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_
        record = set()
        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            if n in record:
                return False
            else:
                record.add(n)
