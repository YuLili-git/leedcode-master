#给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
#示例 1：
#输入：nums = [-4,-1,0,3,10]
#输出：[0,1,9,16,100]
#解释：平方后，数组变为 [16,1,0,9,100]
#排序后，数组变为 [0,1,9,16,100]
#示例 2：
#输入：nums = [-7,-3,2,3,11]
#输出：[4,9,9,49,121]
############################# solution 1 #############################
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            res.append(i * i)
        res.sort()
        return res
############################# solution 1 #############################
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j, k = 0, n - 1, n - 1
        ans = [-1] * n 
        while i <= j:
            lm = nums[i] * nums[i]
            rm = nums[j] * nums[j]
            if lm > rm:
                ans[k] = lm
                i += 1
            else:
                ans[k] = rm
                j -= 1
            k -= 1
        return ans
