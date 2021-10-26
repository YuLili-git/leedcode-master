#给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
#0 <= a, b, c, d < n
#a、b、c 和 d 互不相同
#nums[a] + nums[b] + nums[c] + nums[d] == target
#你可以按 任意顺序 返回答案 。
#示例 1：
#输入：nums = [1,0,-1,0,-2,2], target = 0
#输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#示例 2：
#输入：nums = [2,2,2,2,2], target = 8
#输出：[[2,2,2,2]]
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                p = j + 1
                q = n - 1
                while p < q:
                    if nums[i] + nums[j] + nums[p] + nums[q] < target:
                        p += 1
                    elif nums[i] + nums[j] + nums[p] + nums[q] > target:
                        q -= 1
                    else:
                        res.append([nums[i], nums[j], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]:
                            p += 1
                        while p < q and nums[q] == nums[q - 1]:
                            q -= 1
                        p += 1
                        q -= 1
        return res
