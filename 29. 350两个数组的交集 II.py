#给定两个数组，编写一个函数来计算它们的交集。
#示例 1：
#输入：nums1 = [1,2,2,1], nums2 = [2,2]
#输出：[2,2]
#示例 2:
#输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#输出：[4,9]
######################### solution 1 #########################
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) <= len(nums2):
            for i in nums1:
                if i in nums2:
                    res.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    res.append(i)
                    nums1.remove(i)
        return res
######################### solution 2 #########################
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = collections.Counter()
        
        for num in nums1:
            m[num] += 1
        
        res = list()
        for num in nums2:
            if (count := m.get(num, 0)) > 0:
                res.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        
        return res
