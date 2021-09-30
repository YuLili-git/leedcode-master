#给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#如果数组中不存在目标值 target，返回 [-1, -1]。
#进阶：
#你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#示例 1：
#输入：nums = [5,7,7,8,8,10], target = 8
#输出：[3,4]
#示例 2：
#输入：nums = [5,7,7,8,8,10], target = 6
#输出：[-1,-1]
#示例 3：
#输入：nums = [], target = 0
#输出：[-1,-1]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                while i <= j and nums[j] != nums[m]:
                    j -= 1
                while i <= j and nums[i] != nums[m]:
                    i += 1
                return [i, j]
        return [-1, -1]
