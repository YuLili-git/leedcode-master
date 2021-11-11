#找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#说明：
#所有数字都是正整数。
#解集不能包含重复的组合。 
#示例 1:
#输入: k = 3, n = 7
#输出: [[1,2,4]]
#示例 2:
#输入: k = 3, n = 9
#输出: [[1,2,6], [1,3,5], [2,3,4]]
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        def findAllPath(k, n, sum_num, start_index):
            if sum_num > n:
                return 
            if sum_num == n and len(path) == k:
                return res.append(path[:])
            for i in range(start_index, 9 - (k - len(path)) + 2):
                path.append(i)
                sum_num += i 
                findAllPath(k, n, sum_num, i + 1)
                sum_num -= i 
                path.pop()
        findAllPath(k, n, 0, 1)
        return res
