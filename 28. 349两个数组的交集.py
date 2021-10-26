#给定两个数组，编写一个函数来计算它们的交集。
#示例 1：
#输入：nums1 = [1,2,2,1], nums2 = [2,2]
#输出：[2]
#示例 2：
#输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#输出：[9,4]
######################### solution 1 #########################
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp = []
        for i in nums1:
            if i in nums2 and i not in tmp:
                tmp.append(i)
        return tmp
######################### solution 2 #########################
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
